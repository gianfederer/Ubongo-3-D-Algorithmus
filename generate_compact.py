import numpy as np
import time
import hashlib

class GenerateBase:
    def __init__(self):
        pass

    def rotate(self, piece, direction1,direction2,axis1,axis2):
        #Zwei Dreheungen werden durchgeführt
        new_piece = np.rot90(piece, direction1, axis1)
        if direction2 != 0:
            new_piece = np.rot90(new_piece, direction2, axis2)
            
        if np.all(new_piece[2] == 0):
            #das Teil liegt in den untersten beiden Schichten, nicht muss gemacht werden
            pass
        else:   
            #das Teil befindet sich auch in der obersten Schicht
            if np.all(new_piece[0] == 0):
                #die unterste Schicht ist leer, es kann also problemlos nach unten verschoben werden.
                new_piece = np.roll(new_piece, -1, 0)

            else:
                #es befindet sich in allen Schichten, somit wird es nicht in das Spielfeld (Höhe =2) passen
                return
            
        return new_piece

    def available_directions(self, piece):
        #alle Richtungen werden überprüft. ....2 ist True wenn es um zwei Blöcke verschoben werden kann
        posx2 = True if np.all(piece[:, 1, :] == 0) and np.all(piece[:, 2, :] == 0) else False
        posx1 = True if np.all(piece[:, 2, :] == 0) else False
        negx2 = True if np.all(piece[:, 0, :] == 0) and np.all(piece[:, 1, :] == 0) else False
        negx1 = True if np.all(piece[:, 0, :] == 0) else False
        posy2 = True if np.all(piece[:, :, 1] == 0) and np.all(piece[:, :, 2] == 0) else False
        posy1 = True if np.all(piece[:, :, 2] == 0) else False
        negy2 = True if np.all(piece[:, :, 0] == 0) and np.all(piece[:, :, 1] == 0) else False
        negy1 = True if np.all(piece[:, :, 0] == 0) else False
        posz = True if np.all(piece[1] == 0) else False
        negz = True if np.all(piece[0] == 0) else False

        return posx2, negx2, posy2, negy2, posx1, negx1, posy1, negy1, posz, negz

    def move_piece(self, shift, axis, piece):
        shifted_piece = np.roll(piece, shift, axis)
        #axis: 0 = z, 1 = x, 2 = y
        return shifted_piece
    
    def piece_in_block(self, piece, use_hash=False, optimized=False):
        list_of_shifted_pieces = []
        list_of_hashed_pieces = []

        for h in range(24):
            #Schleife, die alle Orientierungen eines Legeteiles erstellt
            first_rotationaxis = (0, 1) if h <= 15 else (1, 2)
            first_direction = int(h / 4)
            if first_direction == 4:
                first_direction = 1
            elif first_direction == 5:
                first_direction = 3

            rotated_piece = self.rotate(piece, first_direction, h % 4, first_rotationaxis, (0, 2))

            shifted_piece1 = None
            shifted_piece2 = None
            shifted_piece3 = None
            if np.any(rotated_piece is not None):
                av_dir = self.available_directions(rotated_piece)
                axis_counter = 0
                for i in range(3):
                    #Schleife die alle Verschiebeungen in der z-Achse erstellt
                    if i == 0 and av_dir[9] == 1:
                        shifted_piece1 = self.move_piece(-1, 0, rotated_piece)
                        axis_counter = 1
                    elif i == 1:
                        shifted_piece1 = rotated_piece
                        axis_counter = 1
                    elif i == 2 and av_dir[8] == 1:
                        shifted_piece1 = self.move_piece(1, 0, rotated_piece)
                        axis_counter = 1

                    if axis_counter == 1:
                        for k in range(5):
                            if k == 0 and av_dir[1] == 1:
                                shifted_piece2 = self.move_piece(-2, 1, shifted_piece1)
                                axis_counter = 2
                            elif k == 1 and av_dir[0] == 1:
                                shifted_piece2 = self.move_piece(2, 1, shifted_piece1)
                                axis_counter = 2
                            elif k == 2:
                                shifted_piece2 = shifted_piece1
                                axis_counter = 2
                            elif k == 3 and av_dir[5] == 1:
                                shifted_piece2 = self.move_piece(-1, 1, shifted_piece1)
                                axis_counter = 2
                            elif k == 4 and av_dir[4] == 1:
                                shifted_piece2 = self.move_piece(1, 1, shifted_piece1)
                                axis_counter = 2

                            if axis_counter == 2:
                                for j in range(5):
                                    if j == 0 and av_dir[3] == 1:
                                        shifted_piece3 = self.move_piece(-2, 2, shifted_piece2)
                                        axis_counter = 3
                                    elif j == 1 and av_dir[2] == 1:
                                        shifted_piece3 = self.move_piece(2, 2, shifted_piece2)
                                        axis_counter = 3
                                    elif j == 2:
                                        shifted_piece3 = shifted_piece2
                                        axis_counter = 3
                                    elif j == 3 and av_dir[7] == 1:
                                        shifted_piece3 = self.move_piece(-1, 2, shifted_piece2)
                                        axis_counter = 3
                                    elif j == 4 and av_dir[6] == 1:
                                        shifted_piece3 = self.move_piece(1, 2, shifted_piece2)
                                        axis_counter = 3

                                    if np.any(shifted_piece3 is not None) and axis_counter == 3:
                                        shifted_piece3 = shifted_piece3[:2, :, :]
                                        
                                        if use_hash:
                                            hashed_piece = np.ascontiguousarray(shifted_piece3)
                                            hashed_piece = hashlib.sha256(hashed_piece).hexdigest()
                                            if list_of_shifted_pieces != []:
                                                for l in range(len(list_of_shifted_pieces)):
                                                    if hashed_piece == list_of_hashed_pieces[l]:
                                                        if np.array_equal(list_of_shifted_pieces[l], shifted_piece3):
                                                            break
                                                    elif l == len(list_of_shifted_pieces) -1:
                                                        list_of_shifted_pieces.append(shifted_piece3)
                                                        list_of_hashed_pieces.append(hashed_piece)
                                                        axis_counter = 2
                                            else:
                                                list_of_shifted_pieces.append(shifted_piece3)
                                                list_of_hashed_pieces.append(hashed_piece)
                                                axis_counter = 2
                                            

                                        elif optimized:
                                            if list_of_shifted_pieces != []:
                                                for l in range(len(list_of_shifted_pieces)):
                                                    if np.array_equal(list_of_shifted_pieces[l], shifted_piece3):
                                                        break
                                                    elif l == len(list_of_shifted_pieces) -1:
                                                        list_of_shifted_pieces.append(shifted_piece3)
                                                        axis_counter = 2
                                            else:
                                                list_of_shifted_pieces.append(shifted_piece3)
                                                axis_counter = 2
                                        else:
                                            list_of_shifted_pieces.append(shifted_piece3)
                                        axis_counter = 2
                                    else:
                                        axis_counter = 0
                            else:
                                axis_counter = 0
                    else:
                        axis_counter = 0
        return list_of_shifted_pieces

class GenerateUnoptimized(GenerateBase):
    def __init__(self):
        super().__init__()

    def piece_in_block(self, piece):
        return super().piece_in_block(piece, use_hash=False, optimized=False)

class GenerateOptimizedHash(GenerateBase):
    def __init__(self):
        super().__init__()

    def piece_in_block(self, piece):
        return super().piece_in_block(piece, use_hash=True, optimized=False)

class GenerateOptimized(GenerateBase):
    def __init__(self):
        super().__init__()

    def piece_in_block(self, piece):
        return super().piece_in_block(piece, use_hash=False, optimized=True)

class GenerateOptimizedHash_with_cut(GenerateBase):
    def __init__(self):
        super().__init__()

    def cut(self, piece):
        av_dir = self.available_directions(piece)
        x = -(av_dir[0]+av_dir[4])
        y = -(av_dir[2]+av_dir[6])
        if x < 0:
            piece = piece[:,:x,:]
        if y < 0:
            piece = piece[:,:,:y]
        return piece

    def piece_in_block(self, piece):
        list_of_shifted_pieces = []
        list_of_hashed_pieces = []

        for h in range(24):
            first_rotationaxis = (0, 1) 
            if h <= 15:
                first_rotationaxis = (1,2)

            first_direction = int(h / 4)
            if first_direction == 4:
                first_direction = 1
            elif first_direction == 5:
                first_direction = 3

            rotated_piece = self.rotate(piece, first_direction, h % 4, first_rotationaxis, (0, 2))
            if np.any(rotated_piece is None):
                continue
            av_dir = self.available_directions(rotated_piece)
            for i in range(1+av_dir[8]+av_dir[9]):
                if i > 0:
                    if av_dir[8] == av_dir[9]:
                        if i == 1:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                    else:
                        if av_dir[8]:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                else:
                    shifted_piece = rotated_piece


                if np.any(rotated_piece is not None):
                    av_dir_corner = self.available_directions(shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[1] + av_dir_corner[5]),1, shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[3] + av_dir_corner[7]),2, shifted_piece)
                    shifted_piece = self.cut(shifted_piece)
                    if np.any(shifted_piece != None):
                        shifted_piece = shifted_piece[:2, :, :]
                        hashed_piece = np.ascontiguousarray(shifted_piece)
                        hashed_piece = hashlib.sha256(hashed_piece).hexdigest()
                        if list_of_shifted_pieces != []:
                            for l in range(len(list_of_shifted_pieces)):
                                if hashed_piece == list_of_hashed_pieces[l]:
                                    if np.array_equal(list_of_shifted_pieces[l], shifted_piece):
                                        break
                                elif l == len(list_of_shifted_pieces) -1:
                                    list_of_shifted_pieces.append(shifted_piece)
                                    list_of_hashed_pieces.append(hashed_piece)
                        else:
                            list_of_shifted_pieces.append(shifted_piece)
                            list_of_hashed_pieces.append(hashed_piece)
        return list_of_shifted_pieces


class GenerateOptimizedHash_with_cut_yield(GenerateOptimizedHash_with_cut):
    def __init__(self):
        super().__init__()

    def piece_in_block(self, piece):
        list_of_shifted_pieces = []
        list_of_hashed_pieces = []

        for h in range(24):
            first_rotationaxis = (0, 1) 
            if h <= 15:
                first_rotationaxis = (1,2)

            first_direction = int(h / 4)
            if first_direction == 4:
                first_direction = 1
            elif first_direction == 5:
                first_direction = 3

            rotated_piece = self.rotate(piece, first_direction, h % 4, first_rotationaxis, (0, 2))
            if np.any(rotated_piece is None):
                continue
            av_dir = self.available_directions(rotated_piece)
            for i in range(1+av_dir[8]+av_dir[9]):
                if i > 0:
                    if av_dir[8] == av_dir[9]:
                        if i == 1:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                    else:
                        if av_dir[8]:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                else:
                    shifted_piece = rotated_piece


                if np.any(rotated_piece is not None):
                    av_dir_corner = self.available_directions(shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[1] + av_dir_corner[5]),1, shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[3] + av_dir_corner[7]),2, shifted_piece)
                    shifted_piece = self.cut(shifted_piece)
                    if np.any(shifted_piece != None):
                        shifted_piece = shifted_piece[:2, :, :]
                        hashed_piece = np.ascontiguousarray(shifted_piece)
                        hashed_piece = hashlib.sha256(hashed_piece).hexdigest()
                        if list_of_shifted_pieces != []:
                            for l in range(len(list_of_shifted_pieces)):
                                if hashed_piece == list_of_hashed_pieces[l]:
                                    if np.array_equal(list_of_shifted_pieces[l], shifted_piece):
                                        break
                                elif l == len(list_of_shifted_pieces) -1:
                                    list_of_shifted_pieces.append(shifted_piece)
                                    list_of_hashed_pieces.append(hashed_piece)
                                    yield list_of_shifted_pieces
                        else:
                            list_of_shifted_pieces.append(shifted_piece)
                            list_of_hashed_pieces.append(hashed_piece)
                            yield list_of_shifted_pieces

class Generate_only_cut(GenerateBase):
    def __init__(self):
        super().__init__()

    def cut(self, piece):
        av_dir = self.available_directions(piece)
        x = -(av_dir[0]+av_dir[4])
        y = -(av_dir[2]+av_dir[6])
        if x < 0:
            piece = piece[:,:x,:]
        if y < 0:
            piece = piece[:,:,:y]
        return piece

    def piece_in_block(self, piece):
        list_of_shifted_pieces = []
        for h in range(24):
            first_rotationaxis = (0, 1) 
            if h <= 15:
                first_rotationaxis = (1,2)

            first_direction = int(h / 4)
            if first_direction == 4:
                first_direction = 1
            elif first_direction == 5:
                first_direction = 3

            rotated_piece = self.rotate(piece, first_direction, h % 4, first_rotationaxis, (0, 2))
            if np.any(rotated_piece is None):
                continue
            av_dir = self.available_directions(rotated_piece)
            for i in range(1+av_dir[8]+av_dir[9]):
                if i > 0:
                    if av_dir[8] == av_dir[9]:
                        if i == 1:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                    else:
                        if av_dir[8]:
                            shifted_piece = self.move_piece(1, 0, rotated_piece)
                        else:
                            shifted_piece = self.move_piece(-1, 0, rotated_piece)
                else:
                    shifted_piece = rotated_piece


                if np.any(rotated_piece is not None):
                    av_dir_corner = self.available_directions(shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[1] + av_dir_corner[5]),1, shifted_piece)
                    shifted_piece = self.move_piece(-(av_dir_corner[3] + av_dir_corner[7]),2, shifted_piece)
                    shifted_piece = self.cut(shifted_piece)
                    if np.any(shifted_piece != None):
                        shifted_piece = shifted_piece[:2, :, :]
                        list_of_shifted_pieces.append(shifted_piece)
        return list_of_shifted_pieces

 