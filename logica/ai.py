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

    # Verifica o estado atual do jogo
    def evaluate(self, board):
        # descobre se alguém já ganhou (alinhamento 3 símbolos iguais)
        winner = self.check_winner(board)
        
        # caso IA tenha ganhado retorno positivo
        if winner == self.ai_player: return 10
        # caso Humano tenha ganhado retorno negativo
        elif winner == self.human_player: return -10
       
        return 0  # empate ou ainda na partida
        
    def minimax(self, board, depth, is_max, alpha, beta):
    # Analisa a vitória, derrota ou empate
    score = self.evaluate(board)
    if score == 10: return score - depth   # A IA ganhou
    if score == -10: return score + depth  # O usuário ganhou
    if not self.get_empty(board): return 0 # O jogo deu empate

    # Vez da IA, usa o MAX
    if is_max:
        best = -math.inf
        for i in self.get_empty(board):
            board[i] = self.ai_player
            best = max(best, self.minimax(board, depth + 1, False, alpha, beta))
            board[i] = ' '                 # Usa o Backtracking para desfazer a jogada
            alpha = max(alpha, best)
            if beta <= alpha: break        # Corta o Alpha-Beta
        return best

    # Vez do usuário, usa o MIN
    else:
        best = math.inf
        for i in self.get_empty(board):
            board[i] = self.human_player
            best = min(best, self.minimax(board, depth + 1, True, alpha, beta))
            board[i] = ' '                 # Usa o Backtracking paradesfazer a jogada
            beta = min(beta, best)
            if beta <= alpha: break        # Corta Alpha-Beta
        return best
    #Retorna a melhor jogada possivel para a (IA)
    def get_best_move(self, board):
        best_val = -math.inf
        best_move = -1
        for i in self.get_empty(board):
            board[i] = self.ai_player
            move_val = self.minimax(board, 0, False, -math.inf, math.inf)
            board[i] = ' '
            if move_val > best_val:
                best_move = i
                best_val = move_val
        return best_move
