import numpy as np

class chiffre:
    def __init__(self, key="", size=10) -> None:
        self.square = np.zeros((size, size), dtype=str)
        self.key = key
        self.size = size

        for i in range(len(self.key)):
            self.square[i // len(self.square)][i % len(self.square)] = self.key[i]
        abc = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?,"
        abc = "".join([x for x in abc if x not in self.key])
        if len(abc) > len(self.square) ** 2: print("Warning: not all letters of abc are used in square!")
        # for letter in abc: put on first free spot in square
        for letter in abc:
            for i in range(self.size):
                for j in range(self.size):
                    if self.square[i][j] == "":
                        self.square[i][j] = letter
                        break
                else:
                    continue
                break

    def encrypt(self, text, string=False):
        # make list of coordinates of letters in text
        coordinates = []
        for letter in text:
            for i in range(self.size):
                for j in range(self.size):
                    if self.square[i][j] == letter:
                        coordinates.append((i, j))
                        break
                else:
                    continue
                break
        if string:
            return "".join([str(x[0]) + str(x[1]) for x in coordinates])
        return coordinates
    
    def decrypt(self, coordinates):
        if type(coordinates) == str:
            coordinates = [(int(coordinates[i]), int(coordinates[i+1])) for i in range(0, len(coordinates), 2)]

        text = ""
        for coordinate in coordinates:
            text += self.square[coordinate[0]][coordinate[1]]
        return text