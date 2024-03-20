def game_start():
    print(r"""
             _____ ___ ____   _____  _    ____   _____ ___  _____
    |_   _|_ _/ ___| |_   _|/ \  / ___| |_   _/ _ \| ____|
      | |  | | |       | | / _ \| |       | || | | |  _|
      | |  | | |___    | |/ ___ \ |___    | || |_| | |___
      |_| |___\____|   |_/_/   \_\____|   |_| \___/|_____|
      """)
    selection = True
    while selection:
        player_1_marker = input("Welcome to the Tic Tac Toe Game.\n\nYou will be the Player-1.\n\nPlease choose your "
                                "marker 'X' or 'O'. ").upper()
        if player_1_marker in ['X', 'O']:
            player_2_marker = 'O' if player_1_marker == 'X' else 'X'
            print(f'{player_1_marker}, {player_2_marker}')
            return player_1_marker, player_2_marker
        else:
            print('Please select "O" or "X".')


class TicTacGame:
    def __init__(self, player_1_marker, player_2_marker):
        self.player_1_marker = player_1_marker
        self.player_2_marker = player_2_marker
        self.player1 = True
        self.move_count = 0
        self.board = [' '] * 9
        self.score_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.winning_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

    def show_board(self):
        print('\n')
        print('\t    |    |')
        print(f'\t {self.board[0]}  | {self.board[1]}  |  {self.board[2]}')
        print('\t____|____|____')
        print('\t    |    |')
        print(f'\t {self.board[3]}  | {self.board[4]}  |  {self.board[5]}')
        print('\t____|____|____')
        print('\t    |    |')
        print(f'\t {self.board[6]}  | {self.board[7]}  |  {self.board[8]}')

    def play(self):
        while self.move_count < 9:
            mark = input('Player 1, Please select the cell number to put your mark ' if self.player1 else
                         'Player 2, Please select the cell number to put your mark ')
            if not mark.isdigit() or int(mark) not in range(1, 10):
                print('Please input a number between 1 to 9.')
                continue
            mark = int(mark) - 1
            if self.board[mark] != ' ':
                print('That position is already taken. Please choose another position.')
                continue
            self.board[mark] = self.player_1_marker if self.player1 else self.player_2_marker
            self.move_count += 1
            self.show_board()
            if self.check_winner():
                print("Player 1 has won!" if self.player1 else "Player 2 has won!")
                return
            self.player1 = not self.player1
        print("Match Draw")

    def check_winner(self):
        for condition in self.winning_conditions:
            if (self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]]) and (
                    self.board[condition[0]] != ' '):
                return True
        return False


if __name__ == '__main__':
    player_1_marker, player_2_marker = game_start()
    game = TicTacGame(player_1_marker, player_2_marker)
    game.show_board()
    game.play()
