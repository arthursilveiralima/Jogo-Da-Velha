import math

class TicTacToeAI:
    def __init__(self, ai_player='O'):
        # a IA vai receber 'O'
        self.ai_player = ai_player
        # garantindo que o Jogador não receba o mesmo marcador da IA
        self.human_player = 'X' if ai_player == 'O' else 'O'

    # Procura casas vazias no tabuleiro
    def get_empty(self, board):
        return [i for i, x in enumerate(board) if x == ' ']

    # Verifica se alguem venceu utilizando as possiveis combinações de vitoria
    def check_winner(self, board):
        win_states = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        # verifica se as posições possuem o mesmo simbolo e exclui o simbolo vazio e retorna o vencedor se tiver
        for state in win_states:
            if board[state[0]] == board[state[1]] == board[state[2]] and board[state[0]] != ' ':
                return board[state[0]]
        return None

    def evaluate(self, board):
        winner = self.check_winner(board)
        if winner == self.ai_player: return 10
        elif winner == self.human_player: return -10
        return 0
