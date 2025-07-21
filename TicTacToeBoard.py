class TicTacToeBoard:
    def __init__(self):
        
        self.board_size = 9
        self.board = [0] * self.board_size
        self.initialise_board()

    def initialise_board(self):
        # Make all the board slots as empty
        self.board = ['O', 'O', 'X', 'O', 'O', 'X', 'O', 'O', 'X' ]
        # for index in range(self.board_size):
        #     self.board[index] = "-"
    def check_if_won(self):
        self.check_columns()
        pass

    def check_columns(self):
        number_of_x = 0
        number_of_o = 0
        count = 0
        while count != 3:
            number_of_o= 0
            number_of_x = 0

            for i in range(self.board_size):
                #
                if i == (0 + count) or i == (count + 3) or i == (count + 6):
                    if self.board[i] == "X":
                        number_of_x += 1
                        print(self.board[i] + " " + str(i))

                    if self.board[i] == "O":
                        print(self.board[i] + " " + str(i))
                        number_of_o += 1
                if number_of_o == 3:
                    print("O won Game Won!")
                if number_of_x == 3:
                    print("X won Game Won!")
                    
            count += 1
            print("Count is "  + str(count))
        
        return


    def display_tictactoe_title(self):
        print("==========================")
        print("Printing Tic Tac Toe Board")
        print("==========================")

    def display_tictactoe_board(self):
        # It will print in a pretty manner
        # TODO - I want it so that any board size is compatible with this function.
        counter = 0

        for index in range(self.board_size):
            print(self.board[index], end=' ')
            if counter == 2 or counter == 5 or counter ==8: 
                print("")
            counter+=1
    
    def apply_algorithm(self):
        # Get all the combination
        
        pass

    def is_move_possible(self, user_input_position_number):
        # Checks if the user can input any X or O into a slot
        if self.board[user_input_position_number] == "-":
            return True
        return False
    
    def apply_move_to_board(self, user_input_position_number):
        self.check_if_won()
        if not self.is_move_possible(user_input_position_number):
            return "Position is not empty! Please select an empty position!"
        self.board[user_input_position_number] = "X"
        return "Move successfully applied"
    
    def reset_board(self):
        self.initialise_board()
    


t = TicTacToeBoard()
print(t.apply_move_to_board(0))
print(t.apply_move_to_board(0))
t.display_tictactoe_board()
# t.display_tictactoe_board()