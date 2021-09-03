def output_message(self):
    if self.number_of_sequences > 1 and len(self.balls_array) == 0:
        message = 'There were {} sequences in the initial array and no balls remained!'.format(self.number_of_sequences)
    elif self.number_of_sequences > 1 and len(self.balls_array) == 1:
        message = 'There were {0} sequences in the initial array and 1 ball remained: {1}.'. \
                        format(self.number_of_sequences, self.balls_array)
    elif self.number_of_sequences == 1 and len(self.balls_array) == 1:
        message = 'There was 1 sequence in the initial array and 1 ball remained: {}'.format(self.balls_array)
    elif self.number_of_sequences == 1 and len(self.balls_array) > 1:
        message = 'There was 1 sequence in the initial array and {} balls remained: {}'\
            .format(len(self.balls_array),self.balls_array)
    else:
        message = 'There were {0} sequences in the initial array and {1} balls remained: {2}.'. \
                        format(self.number_of_sequences, len(self.balls_array), self.balls_array)
    print(message)
