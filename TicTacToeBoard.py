class TicTacToeBoard:
    def __init__(self):
        self.COLUMN_NUMBER = 3
        self.board_size = 9
        self.board = [0] * self.board_size
        self.initialise_board()
        self.human_player = "X"
        self.ai_player = "O"
        self.current_player = self.human_player  # Human starts first

    def initialise_board(self):
        # Initialize all slots as empty
        for index in range(self.board_size):
            self.board[index] = "-"

    def check_if_won(self):
        # Check all possible win conditions
        if self.check_columns():
            return True
        if self.check_rows():
            return True
        if self.check_diagonals():
            return True
        return False

    def check_rows(self):
        for row in range(3):
            start_index = row * 3
            if (self.board[start_index] != "-" and 
                self.board[start_index] == self.board[start_index + 1] == self.board[start_index + 2]):
                return True
        return False

    def check_columns(self):
        for col in range(3):
            if (self.board[col] != "-" and 
                self.board[col] == self.board[col + 3] == self.board[col + 6]):
                return True
        return False

    def check_diagonals(self):
        # Top-left to bottom-right
        if self.board[0] != "-" and self.board[0] == self.board[4] == self.board[8]:
            return True
        # Top-right to bottom-left
        if self.board[2] != "-" and self.board[2] == self.board[4] == self.board[6]:
            return True
        return False

    def is_board_full(self):
        return "-" not in self.board

    def get_available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == "-"]

    def make_move(self, position, player):
        if self.is_move_possible(position):
            self.board[position] = player
            return True
        return False

    def display_tictactoe_board(self):
        for i in range(self.board_size):
            print(self.board[i], end=' ')
            if (i + 1) % self.COLUMN_NUMBER == 0:
                print()

    def is_move_possible(self, position):
        return self.board[position] == "-"

    # Minimax Algorithm Implementation
    def minimax(self, depth, is_maximizing):
        # Base cases
        if self.check_if_won() and is_maximizing:
            return -10 + depth  # Prefer faster wins
        elif self.check_if_won() and not is_maximizing:
            return 10 - depth    # Prefer slower losses
        elif self.is_board_full():
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for move in self.get_available_moves():
                self.board[move] = self.ai_player
                score = self.minimax(depth + 1, False)
                self.board[move] = "-"
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in self.get_available_moves():
                self.board[move] = self.human_player
                score = self.minimax(depth + 1, True)
                self.board[move] = "-"
                best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = -float('inf')
        best_move = None
        for move in self.get_available_moves():
            self.board[move] = self.ai_player
            score = self.minimax(0, False)
            self.board[move] = "-"
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

    def play_ai_turn(self):
        if not self.check_if_won() and not self.is_board_full():
            best_move = self.find_best_move()
            self.make_move(best_move, self.ai_player)
            self.current_player = self.human_player
            print(f"AI plays at position {best_move}")
            return True
        return False

    def play_human_turn(self, position):
        if self.current_player == self.human_player and self.make_move(position, self.human_player):
            self.current_player = self.ai_player
            return True
        return False

    def reset_board(self):
        self.initialise_board()
        self.current_player = self.human_player


# Main game loop
def play_game():
    game = TicTacToeBoard()
    print("Welcome to Unbeatable Tic-Tac-Toe!")
    print("You are X, AI is O")
    print("Positions are 0-8 (left to right, top to bottom)")

    while True:
        game.display_tictactoe_board()
        
        if game.current_player == game.human_player:
            try:
                position = int(input("Your move (0-8): "))
                if position < 0 or position > 8:
                    print("Please enter a number between 0-8")
                    continue
                if not game.play_human_turn(position):
                    print("Invalid move, try again")
                    continue
            except ValueError:
                print("Please enter a number")
                continue
        else:
            print("AI is thinking...")
            game.play_ai_turn()

        # Check game status
        if game.check_if_won():
            game.display_tictactoe_board()
            winner = "AI" if game.current_player == game.human_player else "You"
            print(f"{winner} won!")
            break
        elif game.is_board_full():
            game.display_tictactoe_board()
            print("It's a draw!")
            break

    play_again = input("Play again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_game()