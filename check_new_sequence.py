import find_longest_sequence as fls


def check_new_sequence(self, useful_variables):
    """Method to check if a new sequence is created after removing the longest sequence"""

    if useful_variables is False:
        return False
    else:
        start_index, end_index, removed_sequence_length = useful_variables

    # created 3 variables that will be used for tracking purposes; i will be a pointer used for indexing;
    # sequence_length will be used to store the length of a sequence;
    # is_empty will be used to determine if the array has any elements left in it;
    i, sequence_length, is_empty = 0, 0, False
    length = len(self.balls_array)

    # calculating the value of i after the initial sequence is removed
    i = start_index - removed_sequence_length + 1
    if i < 1:
        i = 0

    while i < length - 3 and not is_empty:
        # checking if a new sequence is created after the removal of the initial one
        if self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2]:
            self.number_of_sequences += 1
            # created a while loop in case that the new sequence is the only one left available
            while sequence_length <= length - 3 and i < length - 3:
                if self.balls_array[i + 2] == self.balls_array[i + 3]:
                    sequence_length += 1
                    i += 1
                else:
                    start_index = i - sequence_length
                    if start_index < 0:
                        start_index = 0
                    end_index = i + 3
                    removed_sequence_length = len(self.balls_array[start_index:end_index])
                    self.balls_array = self.balls_array[:start_index] + self.balls_array[end_index:]
                    length -= removed_sequence_length
                    if length == 0:
                        is_empty = True
                        break
                    i = start_index - removed_sequence_length + 1
                    if i < 1:
                        i = 0
                    sequence_length = 0
                    break
            else:
                # corner case where the last 3 elements are part of the new sequence that needs to be removed
                if i == length - 3 and self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2]:
                    self.balls_array = []
                    break
        else:
            i += 1

    else:
        if i == length - 3:
            # corner case where the last 3 balls are of the same color and part of a sequence
            if self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2] and sequence_length != 0:
                start_index = i - sequence_length
                self.balls_array = self.balls_array[:start_index]
            # corner case where the last 3 balls are of the same color but not part of a sequence
            elif self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2] and sequence_length == 0:
                self.balls_array = self.balls_array[:i]
                self.number_of_sequences += 1
            # corner case where the last ball is not of the same color as the
            # previous 2 and these 2 are part of a sequence
            elif self.balls_array[i] == self.balls_array[i + 1] != self.balls_array[i + 2] and sequence_length != 0:
                start_index = i - sequence_length
                end_index = i + 2
                self.balls_array = self.balls_array[:start_index] + self.balls_array[end_index:]

    # after I've checked if a new sequence is created by removing the longest one,
    # I used recursion to return the find_longest_sequence method from the module with the same name,
    # if the length of the remaining array is at least equal to 3
    if len(self.balls_array) >= 3:
        fls.find_longest_sequence(self)
