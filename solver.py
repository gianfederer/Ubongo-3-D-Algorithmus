import time
import input
import generate_compact
import tester

def solve(board_number, task_number):
    counter = [0,0,0,0] #speichert die Variante für jedes Teil
    block_counter = [0,0,0,0] #speichert die aktuelle Position auf dem Feld für jede aktuelle Variante
    inputtaker = input.InputBase()
    piece_list, board0, number_of_pieces = inputtaker.order(board_number, task_number) #Daten werden erfasst
    start_time = time.perf_counter()
    base_generator = generate_compact.GenerateOptimizedHash_with_cut_yield()
    #second generator is only used when yield is active, dieser ist da, da nur das erste Teil stückweise erzeugt wird
    second_generator = generate_compact.GenerateOptimizedHash_with_cut()
    if isinstance(base_generator, generate_compact.GenerateOptimizedHash_with_cut_yield):
        yield_is_used = True
    else:
        yield_is_used = False
    list_all_pieces = []
    #alle Teile ausser das erste werden generiert
    for i in range(number_of_pieces-1):
        if yield_is_used:
            list_all_pieces.append(second_generator.piece_in_block(piece_list[i+1]))
        else:
            list_all_pieces.append(base_generator.piece_in_block(piece_list[i+1]))
    if not yield_is_used:
        list_all_pieces.insert(0,base_generator.piece_in_block(piece_list[0])) #alle Varianten des ersten Teiles werden hinzugefügt, weil yield nicht benutzt wird
    if yield_is_used:
        piece_gen = base_generator.piece_in_block(piece_list[0])   
        initial_piece = next(piece_gen)
        initial_piece = next(piece_gen)
        #die ersten zwei varianten des ersten Teiles werden erzeugt. Es sind zwei, da es sonst am Ende einen Fehler gibt.
        list_all_pieces.insert(0,initial_piece)

    boards = [board0, None, None, None, None]
    #first should stay, the second is the current successful board etc.

    board_dimensions = board0.shape

    solved = False
    piece_nr = 1

    while solved == False and counter[0] < len(list_all_pieces[0]):#bricht ab, wenn die Aufgabe gelöst ist oder alle Kombinationen durchprobiert wurden
        while True:
            piece_list = list_all_pieces[piece_nr - 1]
            piece_to_place = piece_list[counter[piece_nr - 1]]
            # Calculate `a` and `b` based on the current piece's dimensions
            current_a = board_dimensions[2] - piece_to_place.shape[2]
            current_b = board_dimensions[1] - piece_to_place.shape[1]

            result, boards[piece_nr], testing_class_type = tester.test(current_a,current_b,board_dimensions, boards, list_all_pieces[piece_nr -1], counter, block_counter, piece_nr)
            if result == "Not done":
                piece_nr += 1
                continue
                #die neue Legefläche wird gespeichert und ein neues Teil wird eingesetzt
            if (result == "Mistake" and counter[piece_nr -1] != len(list_all_pieces[piece_nr -1])-1):
                counter[piece_nr -1] += 1
                if piece_nr == 1 and yield_is_used:
                    try:
                        next_piece = next(piece_gen)
                        list_all_pieces[0]= next_piece
                    except StopIteration:
                        pass 
                block_counter[piece_nr -1] = 0
                #Teil kann nicht platziert werden, es wird eine neue Variante des Legeteiles genommen
            elif result == "Mistake" and counter[piece_nr -1] >= len(list_all_pieces[piece_nr -1])-1:
                block_counter[piece_nr -1] = 0
                counter[piece_nr -1] = 0
                piece_nr = piece_nr -1
                if piece_nr == 0:
                    end_time = time.perf_counter()
                    elapsed_time = end_time - start_time
                    return "Not solved", None, elapsed_time, type(inputtaker).__name__, type(base_generator).__name__, testing_class_type
                break
                #Teil kann nicht eingesetzt werden und es gibt keine neue Variante, beim ersten Teil, kann die Aufgabe nicht mehr gelöst werden
            
            if result == "Solved":
                end_time = time.perf_counter()
                elapsed_time = end_time - start_time
                piece_nr = 0
                return "Solved", boards, elapsed_time, type(inputtaker).__name__, type(base_generator).__name__, testing_class_type
                #die Aufgabe wurde gelöst, die Zeit etc. wird zurückgegeben
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    return "Not solved", None, elapsed_time,  type(inputtaker).__name__, type(base_generator).__name__, testing_class_type

#alte Version gespeichert um 16:31