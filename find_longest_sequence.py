import check_new_sequence as cns


def find_longest_sequence(self):
    """Method to find the longest sequence in the initial array"""
    # created 3 variables that will be used for tracking purposes; i will be a pointer used for indexing;
    # character_count will be used to store the number of characters in a sequence;
    # number_of_sequences will be used to store the total number of possible sequences in the initial array;
    # data is an empty list to which we'll add the start and end indexes of a sequence and its length
    i, character_count, number_of_sequences, data = 0, 0, 0, []
    length = len(self.balls_array)

    # if less than 3 balls in the array then we can't create any sequences and the game is stopped;
    # because recursion is used, added condition to check if the number_of_sequences is 0
    if length < 3 and self.number_of_sequences == 0:
        print("The initial array doesn't have enough balls to form a valid sequence!")
        return False

    while i in range(length - 3):
        # checking if 3 balls in a row have the same color
        if self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2]:
            # if yes we compare the 3rd and 4th one as well and increment the value of i by 2
            # and the character count by 1
            if self.balls_array[i + 2] == self.balls_array[i + 3]:
                i += 2
                character_count += 1
            # if the 3rd and 4th ball don't have the same color,
            # we determine the start and end index of the sequence and its length and append the values to
            # the empty data list; we reset the character count and increment i by 3
            else:
                index_start = i - 2 * character_count
                index_end = i + 3
                sequence_length = len(self.balls_array[index_start:index_end])
                data.append([index_start, index_end, sequence_length])
                character_count = 0
                i += 3
        # corner case where 4 or more balls have the same color but the last in the sequence doesn't have the same
        # color as the next ball in the array; we increment i by 2 this time and reset the character count
        elif self.balls_array[i] == self.balls_array[i + 1] != self.balls_array[i + 2] and character_count > 0:
            index_start = i - 2 * character_count
            index_end = i + 2
            sequence_length = len(self.balls_array[index_start:index_end])
            data.append([index_start, index_end, sequence_length])
            character_count = 0
            i += 2
        else:
            i += 1

    else:
        # corner case where the last 3 elements don't have the same color and the first 2 are part of a sequence
        if i == length - 3 and self.balls_array[i] == self.balls_array[i + 1] != self.balls_array[i + 2] and \
                character_count > 0:
            index_start = i - 2 * character_count
            index_end = i + 2
            sequence_length = len(self.balls_array[index_start:index_end])
            data.append([index_start, index_end, sequence_length])
        # corner case where the last 3 elements have the same color
        elif i == length - 3 and self.balls_array[i] == self.balls_array[i + 1] == self.balls_array[i + 2]:
            index_start = i - 2 * character_count
            index_end = i + 3
            sequence_length = len(self.balls_array[index_start:index_end])
            data.append([index_start, index_end, sequence_length])
        # corner case where the last 2 elements have the same color and are part of a sequence
        elif i == length - 2 and self.balls_array[i] == self.balls_array[i + 1] and character_count > 0:
            index_start = i - 2 * character_count
            index_end = i + 2
            sequence_length = len(self.balls_array[index_start:index_end])
            data.append([index_start, index_end, sequence_length])
        # corner case where the last 2 elements don't have the same color but the first one is part of a sequence
        elif i == length - 2 and self.balls_array[i] != self.balls_array[i + 1] and character_count > 0:
            index_start = i - 2 * character_count
            index_end = i + 1
            sequence_length = len(self.balls_array[index_start:index_end])
            data.append([index_start, index_end, sequence_length])

    # if the length of the data list is more than 1, we search for the max length in its elements and
    # determine the start and end indexes for the longest sequence
    if len(data) > 1:
        self.number_of_sequences += 1
        max_length = max([data[i][2] for i in range(len(data))])
        index_start, index_end = 0, 0
        for i in range(len(data)):
            if max_length in data[i]:
                index_start, index_end = data[i][:2]
                data.remove(data[i])
                break

    elif len(data) == 1:
        self.number_of_sequences += 1
        index_start, index_end, max_length = data[0]
        data.remove(data[0])
        # if the max length is equal to the initial array's length it means that
        # there was only 1 sequence and the game is stopped
        if max_length == len(self.balls_array):
            self.balls_array = []
            if self.number_of_sequences == 1:
                print('There was only 1 sequence in the initial array and no balls remained!')
                return False
        else:
            if self.number_of_sequences == 1:
                # if the length of the remaining array is 1 and the number of sequences is equal to 1,
                # it means that there was only 1 sequence and 1 ball remained;
                # the game is stopped because a new sequence cannot be created
                if len(self.balls_array) == 1:
                    print('There was only 1 sequence in the initial array and 1 ball remained: {}'
                          .format(self.balls_array))
                    return False
                # if the length of the remaining array is 2 and the number of sequences is equal to 1,
                # it means that there was only 1 sequence and 2 balls remained;
                # the game is stopped because a new sequence cannot be created
                elif len(self.balls_array) == 2:
                    print('There was only 1 sequence in the initial array and 2 balls remained: {}'
                          .format(self.balls_array))
                    return False
    else:
        # if the data list is empty and the number of sequences is 0 it means that there were no sequences
        # in the initial array and the game is stopped
        if self.number_of_sequences == 0:
            print('There were no available sequences in the initial array and {} balls remained: {}'
                  .format(len(self.balls_array), self.balls_array))
            return False
        else:
            return False

    removed_sequence_length = max_length
    self.balls_array = self.balls_array[:index_start] + self.balls_array[index_end:]
    useful_variables = index_start, index_end, removed_sequence_length

    # used recursion to return the check_new_sequence method from the module with the same name
    return cns.check_new_sequence(self, useful_variables)
