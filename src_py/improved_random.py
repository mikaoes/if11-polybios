"""
Verbesserte Version der Polybios-Verschlüsselung, bei der die
Buchstaben des Alphabets zufällig auf ein Quadrat verteilt werden.
Damit beim Empfänger die Nachricht wieder entschlüsselt werden kann,
wird ein Seed für die Zufallsfunktion verwendet, der dem Empfänger
mitgeteilt werden muss.

"""

import numpy as np
import random

class chiffre:
    def __init__(self, size, key="", seed=None) -> None:
        self.square = np.zeros((size, size), dtype=str)
        self.key = key
        self.size = size

        for i in range(len(self.key)):
            self.square[i // len(self.square)][i % len(self.square)] = self.key[i]
        abc = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!?,"
        abc = "".join([x for x in abc if x not in self.key])
        if seed !=None:
            random.seed(seed)
            abc = "".join(random.sample(abc, len(abc)))
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

    def encrypt(self, text):
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
        return coordinates
    
    def decrypt(self, coordinates):
        text = ""
        for coordinate in coordinates:
            text += self.square[coordinate[0]][coordinate[1]]
        return text