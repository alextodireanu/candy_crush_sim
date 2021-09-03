# Candy Crush sim
# There are a number of n colored balls on the screen; the colors are number coded.
# A substring of at least 3 balls having the same color is called a sequence.
# By shooting in a balls that’s part of a sequence, the whole sequence will be removed and
# the right side of the string will shift to the left to fill the gap.
# If a new sequence is created by this move, it will be removed as well and the process repeats
# itself until no new sequence is created.
# Mechanics: the player will always shoot first in a ball that’s part of the longest sequence available;
# if there are more of the same length then the one to the left is selected.
# Example: 5 1 3 3 2 2 2 2 3 1 1 5 6 4 4 4 4 7; first the 2 sequence is removed and we’re left with
# 5 1 3 3 3 1 1 5 6 4 4 4 4 7; the 3 sequence is removed and we’re left with 5 1 1 1 5 6 4 4 4 4 7;
# the 1 sequence is removed and we’re left with 5 5 6 4 4 4 4 7 and lastly the 4 sequence is removed
# and were left with 5 5 6 7; these no longer form a sequence so the game is stopped.
# Task: knowing the number of balls and their color, output the following:
# 1: the number of sequences that were initially available
# 2: the number of balls (if any) that remain

import find_longest_sequence as fls
import output_message as om


class CandyCrush:
    """Class used to represent the game"""

    def __init__(self, balls_array):
        """Init method"""
        self.balls_array = balls_array
        self.number_of_sequences = 0

    def run_game(self):
        """Method to start the game"""
        if fls.find_longest_sequence(self) is False:
            return
        else:
            om.output_message(self)


if __name__ == '__main__':
    arr = [2, 2, 2, 3, 4, 5, 6, 7, 8, 9]
    cc = CandyCrush(arr)
    cc.run_game()
