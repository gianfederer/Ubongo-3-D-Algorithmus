import numpy as np
import time

def place_piece(b,a,board_dimensions,board, piece_to_place):
    #b = offset in x direction, a = offset in y direction
    #all zero array is created that has the dimensions of the board
    expanded_piece = np.zeros(board_dimensions, dtype=int)
    #piece is placed on expanded piece at the desired posititon
    shape_of_piece = piece_to_place.shape
    expanded_piece[:,b:shape_of_piece[1]+b,a:a+shape_of_piece[2]] = piece_to_place
    returning_board = board+expanded_piece
    return returning_board

class Check_np_funtion:
    def __init__(self):
        pass

    def check_board(self, board):
        if np.any(board >= 2):
            return "Mistake"
        elif np.any(board == 0):
            return "Not done"
        elif np.all(board == 1):
            return "Solved"

class Check_count_zeros:
    def __init__(self):
        pass

    def check_board(self, board):
        count_zeros = np.count_nonzero(board == 0)
        count_twos_or_more = np.count_nonzero(board >= 2)
        
        if count_twos_or_more > 0:
            return "Mistake"
        elif count_zeros > 0:
            return "Not done"
        return "Solved"
    
class Check_isolated_squares:
    #the code for this class was writen by ChatGPT (based on the class above [writen by myself])
    def __init__(self):
        pass

    def check_board(self, board):
        count_zeros = np.count_nonzero(board == 0)
        count_twos_or_more = np.count_nonzero(board >= 2)
        
        if count_twos_or_more > 0:
            return "Mistake"
        elif count_zeros > 0:
            shape = board.shape
            
            # Check for isolated 1x1x1 cubes and isolated empty spaces
            for z in range(shape[0]):
                for y in range(shape[1]):
                    for x in range(shape[2]):
                        
                        # Check for isolated empty spaces (value 0 surrounded by 1s)
                        if board[z, y, x] == 0:
                            neighbors = []
                            
                            if z > 0: neighbors.append(board[z-1, y, x])  # below
                            if z < shape[0]-1: neighbors.append(board[z+1, y, x])  # above
                            if y > 0: neighbors.append(board[z, y-1, x])  # left
                            if y < shape[1]-1: neighbors.append(board[z, y+1, x])  # right
                            if x > 0: neighbors.append(board[z, y, x-1])  # front
                            if x < shape[2]-1: neighbors.append(board[z, y, x+1])  # back
                            
                            # If all neighbors are 1, the empty space is isolated
                            if all(n == 1 for n in neighbors):
                                return 
            return "Not done"
        
        return "Solved"


class Check_isolated_squares_2:
    def __init__(self):
        pass

    def check_board(self, board):
        count_zeros = np.count_nonzero(board == 0)
        count_twos_or_more = np.count_nonzero(board >= 2)
        
        if count_twos_or_more > 0:
            return "Mistake"
        elif count_zeros > 0:
            shape = board.shape
            
            # Directions for neighbor search: (z, y, x)
            directions = [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]
            
            # Check for isolated 1x1x1 cubes and isolated 2-cube spaces
            for z in range(shape[0]):
                for y in range(shape[1]):
                    for x in range(shape[2]):
                        
                        # Check for isolated empty spaces (value 0 surrounded by 1s)
                        if board[z, y, x] == 0:
                            neighbors = []
                            empty_neighbors = []
                            
                            # Collect all neighbors and keep track of empty spaces
                            for dz, dy, dx in directions:
                                nz, ny, nx = z + dz, y + dy, x + dx
                                if 0 <= nz < shape[0] and 0 <= ny < shape[1] and 0 <= nx < shape[2]:
                                    neighbors.append(board[nz, ny, nx])
                                    if board[nz, ny, nx] == 0:
                                        empty_neighbors.append((nz, ny, nx))
                            
                            # If all neighbors are 1, it's an isolated single cube
                            if all(n == 1 for n in neighbors):
                                return "Unsolvable (isolated single cube)"
                            
                            # Check for isolated 2-cube space (exactly 1 empty neighbor)
                            if len(empty_neighbors) == 1:
                                nz, ny, nx = empty_neighbors[0]  # Second cube coordinates
                                
                                # Check the neighbors of the second cube
                                second_cube_neighbors = []
                                for dz, dy, dx in directions:
                                    nnz, nny, nnx = nz + dz, ny + dy, nx + dx
                                    if 0 <= nnz < shape[0] and 0 <= nny < shape[1] and 0 <= nnx < shape[2]:
                                        if (nnz, nny, nnx) != (z, y, x):  # Exclude the original cube
                                            second_cube_neighbors.append(board[nnz, nny, nnx])
                                
                                # If all neighbors of the second cube are 1, it's an isolated 2-cube space
                                if all(n == 1 for n in second_cube_neighbors):
                                    return "Unsolvable (isolated space of size 2)"
            
            return "Not done"
        
        return "Solved"
    
def test(a, b, board_dimensions, boards, list_piece, counter, block_counter, piece_nr):
    testing_class = Check_np_funtion()
    for i in range(b + 1):
        for j in range(a + 1):
            if block_counter[piece_nr-1] == (i*(a+1)+j):
                board_with_piece = place_piece(i,j,board_dimensions,boards[piece_nr-1],list_piece[counter[piece_nr-1]])
                status = testing_class.check_board(board_with_piece)
                block_counter[piece_nr -1] += 1
                if status == "Not done":
                    return status , board_with_piece, type(testing_class).__name__
                if status == "Solved":
                    return status, board_with_piece, type(testing_class).__name__
                if status == "Mistake" and i == b and j == a:
                    return status, None, type(testing_class).__name__
                #Der Wert des Brettes spielt keine Rolle, da dieser sowieso wieder überschrieben wird
         
    status = "Mistake"
    return status, None, type(testing_class).__name__
    #Der Wert des Brettes spielt keine Rolle, da dieser sowieso wieder überschrieben wird