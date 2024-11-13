import solver
import numpy as np
import input
import generate_compact
import tester
import cProfile
import pstats
import pandas as pd
import os
from openpyxl import load_workbook
    
def main():
    times_solved = 0
    total_time = []
    avg_time = []
    rounds = 5
    #round = Anzahl Datensätze, die gelöst werden
    avg_time_number = 0
    avg_time_trimed = []

    inputtaker = input.InputBase()

    if inputtaker.auto_mode == False:
        endresult, boards, time_taken, input_class_type, generate_class_type, testing_class_type = solver.solve(0, 0)

        #alle Zwischenstände werden addiert, somit kann bei der Ausgabe jede Teil unterschieden werden.
        if np.any(boards[4] != None):
            output = 4 * boards[4] - boards[3] - boards[2] - boards[1] - boards[0]
        else:
            output = 3 * boards[3] - boards[2] - boards[1] - boards[0]

        print(endresult)
        print("untere Schicht:", "\n", output[0], "\n", "\n", "obere Schicht", "\n", output[1], "\n", "\n", "Das Lösen des Puzzles hat", time_taken, "Sekunden gedauert")

    if inputtaker.auto_mode:
        for i in range(rounds):
            for board_number in range(len(inputtaker.all_boards)):
                for task_number in range(len(inputtaker.board_pieces[board_number])):
                    #solve wird ausgeführt und die Resultate (Zeitmessung, verwendete Klassen) kommen zurück
                    endresult, boards, time_taken, input_class_type, generate_class_type, testing_class_type = solver.solve(board_number, task_number)
                    if endresult == "Solved":
                        times_solved += 1
                    if endresult == "Not solved":
                        print("Not solved")
                    total_time.append(time_taken)
            print(sum(total_time))
            print(times_solved)
            avg_time.append(sum(total_time))
            total_time = []
        lenght = len(avg_time)
        avg_time = sorted(avg_time)
        if len(avg_time) >= 4:
            avg_time_trimed = avg_time[len(avg_time)//4:len(avg_time)-len(avg_time)//4]
            avg_time_number = sum(avg_time_trimed)/len(avg_time_trimed)*lenght
        print("average time per round was: ", avg_time_number/rounds)

        save_to_excel(avg_time, avg_time_number/rounds, rounds, input_class_type, generate_class_type, testing_class_type)

def save_to_excel(avg_times, average_per_round, rounds, input_class, base_generator_class, testing_class, excel_file_path='output_times.xlsx'):
    # Create a DataFrame to store the average times and overall average per round
    data = {
        "Round": list(range(1, len(avg_times) + 1)),
        "Avg_Time_Per_Round": avg_times
    }
    
    time_df = pd.DataFrame(data)
    
    class_data = {
            'Type': ['Inputtaker_type', 'Base_generator', 'Checker'],
            'Class Name': [input_class, base_generator_class, testing_class]
        }
    # Create a DataFrame for the class names
    class_df = pd.DataFrame(class_data)

    time_df.loc[len(time_df)] = ["Overall Average (twice the middle 50 percent)", average_per_round]

    # Check if the file already exists
    if os.path.exists(excel_file_path):
        # Load the existing workbook
        book = load_workbook(excel_file_path)
        
        # Use the ExcelWriter and load the workbook correctly
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            # Find the next available column by checking the existing data
            existing_df = pd.read_excel(excel_file_path)
            startcol = existing_df.shape[1]  # Start after the last column
            
            # Write the new class data next to the existing data
            class_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=0, startcol=startcol)

            # Write the new timing data next to the class data, below the class info
            time_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=5, startcol=startcol)

    else:
        # If the file does not exist, start at the beginning (column 0)
        with pd.ExcelWriter(excel_file_path, engine='openpyxl', mode='w') as writer:
            startcol = 0

            # Write the new class data
            class_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=0, startcol=startcol)

            # Write the new timing data below the class info
            time_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=5, startcol=startcol)

    print(f"Data appended to {excel_file_path}")

if __name__ == "__main__":
    # Profile the main function
    profiler = cProfile.Profile()
    profiler.enable()

    main()

    profiler.disable()
    profiler.dump_stats("profile_output.prof")

    with open("profile_output.txt", "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats("tottime")
        stats.print_stats()

#the profiling with cProfile and the code the save the times to excel were writen by ChatGPT