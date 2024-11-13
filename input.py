import numpy as np

class InputBase:
    def __init__(self):
        self.auto_mode = True
        #für Zeittests
        self.number_of_pieces_auto = 3
        #alle Teile/Legeflächen sind gespeichert
        piece01 = np.array([
            [[1,1,1],[0,1,0],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece02 = np.array([
            [[1,1,1],[1,0,0],[0,0,0]],
            [[0,0,1],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece03 = np.array([
            [[1,1,0],[1,0,0],[0,0,0]],
            [[0,1,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece04 = np.array([
            [[1,1,1],[1,0,1],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece05 = np.array([
            [[1,1,1],[0,0,1],[0,0,0]],
            [[0,0,0],[0,0,1],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece06 = np.array([
            [[0,1,1],[1,1,0],[0,0,0]],
            [[0,0,0],[1,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece07 = np.array([
            [[1,1,1],[0,0,0],[0,0,0]],
            [[1,1,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece08 = np.array([
            [[1,1,0],[0,0,0],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece09 = np.array([
            [[1,1,0],[1,1,0],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece10 = np.array([
            [[1,1,0],[0,1,0],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece11 = np.array([
            [[1,1,1],[0,0,1],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece12 = np.array([
            [[0,1,1],[0,0,0],[0,0,0]],
            [[1,1,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece13 = np.array([
            [[1,1,0],[0,1,1],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece14 = np.array([
            [[1,1,1],[1,0,0],[0,0,0]],
            [[0,0,0],[1,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece15 = np.array([
            [[1,1,1],[0,0,0],[0,0,0]],
            [[0,1,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])
        piece16 = np.array([
            [[1,1,1],[0,0,0],[0,0,0]],
            [[1,0,0],[0,0,0],[0,0,0]],
            [[0,0,0],[0,0,0],[0,0,0]]
        ])

        self.piecelist = [piece01, piece02, piece03, piece04, piece05, piece06, piece07, piece08, piece09, piece10, piece11, piece12, piece13, piece14, piece15, piece16]

        board1a = np.array([
            [[0,0,0,0],[1,1,0,0],[1,1,1,0]],
            [[0,0,0,0],[1,1,0,0],[1,1,1,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board1b = np.array([
            [[1,1,0,1],[0,0,0,1],[1,0,0,0]],
            [[1,1,0,1],[0,0,0,1],[1,0,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board2a = np.array([
            [[0,0,0,0],[1,1,0,0],[1,1,0,1]],
            [[0,0,0,0],[1,1,0,0],[1,1,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board2b = np.array([
            [[1,0,1,1],[0,0,0,1],[1,0,0,0]],
            [[1,0,1,1],[0,0,0,1],[1,0,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board3a = np.array([
            [[1,1,0,0],[1,0,0,1],[0,0,0,1]],
            [[1,1,0,0],[1,0,0,1],[0,0,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board3b = np.array([
            [[1,0,0,1],[0,0,0,1],[1,1,0,0]],
            [[1,0,0,1],[0,0,0,1],[1,1,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board4a = np.array([
            [[1,0,0,1],[0,0,0,0],[1,1,0,1]],
            [[1,0,0,1],[0,0,0,0],[1,1,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board4b = np.array([
            [[1,0,0],[0,0,0],[0,1,0]],
            [[1,0,0],[0,0,0],[0,1,0]],
            [[1,1,1],[1,1,1],[1,1,1]]
        ])
        board5b = np.array([
            [[0,0,0,0],[1,0,0,1],[1,1,0,1]],
            [[0,0,0,0],[1,0,0,1],[1,1,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board6a = np.array([
            [[1,0,1,1],[0,0,0,0],[0,0,1,1]],
            [[1,0,1,1],[0,0,0,0],[0,0,1,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board6b = np.array([
            [[0,0,0],[0,0,0],[0,1,1]],
            [[0,0,0],[0,0,0],[0,1,1]],
            [[1,1,1],[1,1,1],[1,1,1]]
        ])
        board7a = np.array([
            [[0,0,1],[0,0,0],[0,1,1]],
            [[0,0,1],[0,0,0],[0,1,1]],
            [[1,1,1],[1,1,1],[1,1,1]]
        ])
        board7b = np.array([
            [[0,0,0,1],[1,0,0,0],[1,1,1,0]],
            [[0,0,0,1],[1,0,0,0],[1,1,1,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board8b = np.array([
            [[0,0,0,0],[0,0,0,1],[1,1,1,1]],
            [[0,0,0,0],[0,0,0,1],[1,1,1,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board9b = np.array([
            [[0,0,0],[0,0,0],[1,0,1]],
            [[0,0,0],[0,0,0],[1,0,1]],
            [[1,1,1],[1,1,1],[1,1,1]]
        ])
        board4p1a = np.array([
            [[1,0,1,1],[1,0,0,0],[0,0,0,1],[0,1,0,1]],
            [[1,0,1,1],[1,0,0,0],[0,0,0,1],[0,1,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        
        board4p1b = np.array([
            [[0,0,0,0,1],[1,0,0,0,0],[1,1,0,1,1]],
            [[0,0,0,0,1],[1,0,0,0,0],[1,1,0,1,1]],
            [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
        ])
        board4p2a = np.array([
            [[1,0,0,1],[1,0,0,1],[0,0,0,0]],
            [[1,0,0,1],[1,0,0,1],[0,0,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])

        board4p2b = np.array([
            [[1,1,1,0],[1,0,0,0],[0,0,0,0]],
            [[1,1,1,0],[1,0,0,0],[0,0,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board4p3a = np.array([
            [[1,1,1,0],[1,1,0,0],[1,0,0,0],[0,0,0,1]],
            [[1,1,1,0],[1,1,0,0],[1,0,0,0],[0,0,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])

        board4p3b = np.array([
            [[0,0,0,0],[0,0,0,0],[1,1,0,1]],
            [[0,0,0,0],[0,0,0,0],[1,1,0,1]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])
        board4p4a = np.array([
            [[0,0,1,1],[0,0,0,1],[1,0,0,0],[1,1,1,0]],
            [[0,0,1,1],[0,0,0,1],[1,0,0,0],[1,1,1,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])

        board4p4b = np.array([
            [[1,1,0,1],[0,0,0,1],[0,0,0,0]],
            [[1,1,0,1],[0,0,0,1],[0,0,0,0]],
            [[1,1,1,1],[1,1,1,1],[1,1,1,1]]
        ])

        if self.number_of_pieces_auto ==3:
            #zu jeder Liste zweiten Grades gehört eine Legefläche
            self.all_boards = [board1a, board1b, board2a, board2b, board3a, board3b, board4a, board4b, board5b, board6a, board6b, board7a, board7b, board8b, board9b]
            self.board_pieces = [[[7,3,5],[11,16,9],[11,16,7],[7,14,10],[16,7,2],[1,16,7],[9,16,1],[7,12,1]],
                        [[7,10,9],[5,16,7],[2,5,10],[3,9,13],[16,11,5],[2,16,5],[16,14,11],[6,9,16]],
                        [[7,10,5],[14,7,3],[2,9,16],[3,5,11],[5,9,16],[2,14,10],[6,16,7],[15,7,13]],
                        [[2,16,4],[4,14,3],[9,1,10],[4,16,9],[4,5,10],[7,15,1],[1,7,3],[1,16,7]],
                        [[10,14,9],[9,3,6],[3,9,1],[14,10,7],[7,16,6],[14,13,3],[9,11,12],[16,13,7]],
                        [[3,6,5],[10,2,9],[14,13,10],[3,14,9],[14,10,9],[10,5,9],[15,9,6],[5,3,11]],
                        [[3,9,14],[13,10,7],[5,1,3],[7,10,6],[3,13,7],[16,9,13],[4,10,11],[10,5,9]],
                        [[16,9,13],[14,16,6],[6,16,9],[13,7,16],[10,9,14],[16,13,5],[7,12,6],[14,15,9]],
                        [[9,16,2],[13,10,9],[3,9,1],[7,13,3],[12,9,2],[10,7,6],[7,3,6],[16,11,9]],
                        [[7,11,10],[6,10,7],[7,2,3],[7,9,16],[9,14,16],[1,16,9],[5,9,16],[2,9,15]],
                        [[3,9,5],[9,16,14],[14,10,9],[10,7,1],[3,2,7],[16,2,13],[6,10,5],[5,16,1]],
                        [[10,2,8],[8,10,1],[8,14,10],[6,15,8],[8,5,3],[12,16,10],[8,3,14],[15,13,8]],
                        [[3,13,7],[10,14,9],[3,7,1],[13,9,16],[6,9,16],[13,14,16],[3,5,9],[5,16,6]],
                        [[9,5,10],[6,3,9],[13,9,16],[16,7,13],[1,13,3],[10,6,9],[14,9,16],[14,7,16]],
                        [[14,16,9],[1,4,3],[10,6,1],[9,10,5],[3,9,5],[1,5,16],[10,2,7],[6,4,10]]]
        elif self.number_of_pieces_auto ==4:
            self.all_boards = [board4p1a,board4p1b,board4p2a,board4p2b,board4p3a,board4p3b,board4p4a,board4p4b]
            self.board_pieces = [[[9,5,8,6],[3,9,16,11],[16,6,3,14],[3,16,11,6],[2,8,7,14]],
                            [[2,8,7,9],[5,7,11,8],[15,9,3,5],[14,8,9,4],[9,13,3,15]],
                            [[16,8,14,10],[10,5,12,8],[14,8,16,12],[2,10,8,15],[16,8,3,14]],
                            [[8,15,16,2],[10,3,8,7],[16,13,15,8],[10,3,8,1],[8,15,6,10]],
                            [[7,3,1,16],[4,10,12,2],[13,7,15,10],[12,16,1,7],[13,16,3,6]],
                            [[16,14,2,10],[3,10,13,9],[5,10,7,3],[4,9,15,3],[13,10,12,1]],
                            [[14,3,13,10],[9,6,13,8],[3,14,13,12],[13,9,12,16],[9,14,16,10]],
                            [[3,10,8,5],[10,11,16,8],[8,16,6,3],[8,5,16,12],[14,10,8,3]]]

    def get_values(self, board_number, task_number):
        list_of_pieces = []
        if self.auto_mode:
            #alle zur Aufgabe gehörigen Teile werden einer Liste angehängt.
            for i in range(self.number_of_pieces_auto):
                list_of_pieces.append(self.piecelist[self.board_pieces[board_number][task_number][i]-1])

            board = self.all_boards[board_number]

            board = board[:2, :, :]

        if self.auto_mode == False:
            number_of_pieces = int(input("Bitte geben Sie die Anzahl an Teilen an (3 oder 4)  "))
            for i in range(number_of_pieces):
                piecenumber = int(input("Bitte geben Sie die Nummer Ihres Teils an  "))
                list_of_pieces.append(self.piecelist[piecenumber -1])
                
            x = int(input("Bitte geben Sie die Länge in horizontaler Richtung an (mind. 3)  "))
            #Damit der 3x3x3 Block immer platziert werden kann
            if x < 3:
                x = 3
            y = int(input("Bitte geben Sie die Länge in vertikaler Richtung an (mind. 3)  "))
            if y < 3:
                y = 3

            list_board = []
            for i in range(y):
                list_board.append([])
            for h in range(y):
                for i in range(x):
                    text = "Ist Feld ", i + 1, " auf der linken Seite in der Reihe ", h + 1, " weiss (Eingabe: Für Ja geben Sie 0 ein, für Nein geben Sie 1 ein)  "
                    square = int(input(text))
                    list_board[h].append(square)
            #Grundfläche wird auf zwei Lagen erweitert
            list_board = [list_board, list_board]
            #aus der Liste wird ein Array erzeugt
            board = np.array(list_board)

        

        return list_of_pieces, board, len(list_of_pieces)
    
    #in dieser Klasse wird keine Sortierung vorgenommen.
    def order(self, board_number, task_number):
        return self.get_values(board_number, task_number)

        

class InputHeuristics(InputBase):
    def __init__(self) -> None:
        super().__init__()
     #Sortierung nach der Grösse
    def order(self, board_number, task_number):
        list_of_pieces, board, number_of_pieces = self.get_values(board_number, task_number)
        list_of_pieces.sort(key=self.complexity, reverse=True)
        return list_of_pieces, board, number_of_pieces
    
    def complexity(self, piece):
        return np.count_nonzero(piece)
    
class InputHeuristics_surface(InputHeuristics):
    def __init__(self) -> None:
        super().__init__()

    #Sortierung nach Grösse und Oberfläche
    def order(self, board_number, task_number):
        list_of_pieces, board, number_of_pieces = self.get_values(board_number, task_number)
        list_of_pieces.sort(key=self.size, reverse=True)
        list_of_pieces.sort(key=self.calculate_surface_area, reverse=True)
        return list_of_pieces, board, number_of_pieces
    
    def size(self, piece):
        cubes = np.count_nonzero(piece)
        return cubes 
    def calculate_surface_area(self, piece):
        # Get the shape of the piece
        z_dim, y_dim, x_dim = piece.shape
        surface_area = 0

        # Loop through each voxel in the 3D array
        for z in range(z_dim):
            for y in range(y_dim):
                for x in range(x_dim):
                    if piece[z, y, x] == 1:  # If the voxel is part of the piece
                        # Check all 6 neighbors (above, below, left, right, front, back)
                        # and count surfaces that are exposed to air (0 or out of bounds)
                        if z == 0 or piece[z-1, y, x] == 0:  # Below
                            surface_area += 1
                        if z == z_dim - 1 or piece[z+1, y, x] == 0:  # Above
                            surface_area += 1
                        if y == 0 or piece[z, y-1, x] == 0:  # Left
                            surface_area += 1
                        if y == y_dim - 1 or piece[z, y+1, x] == 0:  # Right
                            surface_area += 1
                        if x == 0 or piece[z, y, x-1] == 0:  # Front
                            surface_area += 1
                        if x == x_dim - 1 or piece[z, y, x+1] == 0:  # Back
                            surface_area += 1
                            
        return surface_area