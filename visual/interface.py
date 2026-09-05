import tkinter as tk
import random
import time
from logica.ai import TicTacToeAI

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Velha")
        self.root.geometry("700x850")
        self.root.configure(bg="#FFD1DC")
        self.board = [' '] * 9
        self.current_player = 'X'
        self.mode = None
        self.difficulty = 'Impossível'
        self.ai = TicTacToeAI(ai_player='O')
        self.font_title = ('Comic Sans MS', 24, 'bold')
        self.font_btn = ('Comic Sans MS', 14, 'bold')
        self.build_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children(): widget.destroy()

    def build_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="✨ Jogo da Velha ✨", font=self.font_title, bg="#FFD1DC", fg="#FF1493").pack(pady=40)
        
        btn_config = {'width': 25, 'height': 2, 'font': self.font_btn, 'relief': 'ridge', 'bd': 5}
        tk.Button(self.root, text=" Jogar contra Robô", bg="#87CEFA", fg="black", command=self.build_difficulty_menu, **btn_config).pack(pady=15)
        tk.Button(self.root, text=" Jogar contra Amigo", bg="#98FB98", fg="black", command=lambda: self.start_game('friend'), **btn_config).pack(pady=15)
        tk.Button(self.root, text=" Testar Robô 100 vezes", bg="#FFFACD", fg="black", command=self.run_tests, **btn_config).pack(pady=15)

        def set_difficulty_and_play(self, diff):
        # Verifica a dificuldade escolhida e inicia o jogo
        self.difficulty = diff
        self.start_game('robot')

    def start_game(self, mode):
        # Configura as variáveis iniciais da nova partida 
        self.mode = mode               # Define se o modo é contra amigo ou IA 
        self.board = [' '] * 9         # Cria a lógica do tabuleiro: uma lista com 9 espaços vazios
        self.current_player = 'X'      # O jogador 'X' semprecomeça
        self.build_board()             # Chama a função responsável por desenhar a tela do jogo

    def build_board(self):
        # Apaga o que estava na tela para desenhar o novo tabuleiro
        self.clear_screen()
        
        # Cria e posiciona um botão de "Voltar" no canto superior esquerdo
        tk.Button(self.root, text="⬅ Voltar", font=self.font_btn, bg="#FFB6C1", command=self.build_menu).pack(anchor='nw', padx=10, pady=10)
        
        # Cria o texto superior que avisa de quem é a vez e a dificuldade 
        diff_text = f" - Dificuldade: {self.difficulty}" if self.mode == 'robot' else ""
        self.status_label = tk.Label(self.root, text=f"Vez do Jogador: {self.current_player}{diff_text}", font=('Comic Sans MS', 18, 'bold'), bg="#FFD1DC", fg="#4B0082")
        self.status_label.pack(pady=10)

        # Cria uma moldura (frame) que vai segurar os 9 botões do jogo em formato de grade
        grid_frame = tk.Frame(self.root, bg="#FFEB3B", bd=10, relief="sunken")
        grid_frame.pack(expand=True)

        self.buttons = [] # Lista que vai guardar as referências visuais dos 9 botões
        
        # Laço de repetição para criar os 9 botões (posições de 0 a 8)
        for i in range(9):
            # lambda idx=i: faz com que cada botão "lembre" da sua própria posição quando clicado
            btn = tk.Button(grid_frame, text=" ", font=('Comic Sans MS', 36, 'bold'), width=4, height=1, bg="white", activebackground="#F0F8FF",
                            command=lambda idx=i: self.make_move(idx))
            
            # Posiciona o botão na grade: i//3 define a linha (0, 1 ou 2) e i%3 define a coluna (0, 1 ou 2)
            btn.grid(row=i//3, column=i%3, padx=8, pady=8) 
            self.buttons.append(btn)

    def make_move(self, idx):
        # Regra de bloqueio
        if self.board[idx] != ' ' or self.ai.check_winner(self.board): return
        
        # Executa a jogada na posição clicada com o jogador atual
        self.execute_move(idx, self.current_player)
        
        # Verifica se essa jogada terminou o jogo. Se sim, encerra a função
        if self.check_game_end(): return

        # Se for modo de 2 jogadores, troca o turno (de X para O e O para X)
        if self.mode == 'friend':
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Vez do Jogador: {self.current_player}")
            
        # Se for contra o robô, a interface avisa que a IA está pensando
        elif self.mode == 'robot':
            self.status_label.config(text="Robô pensando... ")
            self.root.update() # Força a tela a atualizar para mostrar o texto antes da IA "pensar"
            self.robot_turn()  # Chama a jogada do robô

    def execute_move(self, idx, player):
        # Atualiza a lista lógica por trás do tabuleiro
        self.board[idx] = player
        
        # Define a cor da letra (Laranja para X, Azul para O)
        color = "#FF4500" if player == 'X' else "#1E90FF"
        
        # Atualiza o visual do botão, colocando a letra (X ou O) e a cor correspondente
        self.buttons[idx].config(text=player, fg=color, bg="#F0F8FF")

    def robot_turn(self):
        # Cria uma pausa para dar a sensação de que o robô está pensando
        time.sleep(0.3) 
        
        # Lista as posições que ainda estão vazias no tabuleiro
        empty_spots = self.ai.get_empty(self.board)
        
        # Lógica de inteligência baseada na dificuldade
        if self.difficulty == 'Fácil':
            move = random.choice(empty_spots) # Pega uma casa vazia qualquer (joga aleatoriamente)
        elif self.difficulty == 'Médio':
            # 50/50 ou a IA faz a melhor jogada ou faz uma aleatória 
            move = self.ai.get_best_move(self.board) if random.random() > 0.5 else random.choice(empty_spots)
        else: # Dificuldade "Difícil"
            move = self.ai.get_best_move(self.board) # Sempre procura a melhor jogada matematicamente (Minimax)
            
        # O robô executa a jogada dele (sempre joga como 'O')
        self.execute_move(move, 'O')
        
        # Se o jogo não acabou, avisa que o turno voltou para o usuário
        if not self.check_game_end():
            self.status_label.config(text=f"Sua vez (X) - Dificuldade: {self.difficulty}")

    def check_game_end(self):
        # Verifica com a IA se já existe uma linha, coluna ou diagonal vencedora
        winner = self.ai.check_winner(self.board)
        
        if winner:
            self.status_label.config(text=f" Vencedor: {winner}! ")
            self.show_victory_screen(winner) # Chama a tela de vitória
            return True
        elif ' ' not in self.board: # deu velha (empate)
            self.status_label.config(text="Empate! ")
            self.show_victory_screen("Empate")
            return True
        return False

    # Mostra a tela de Fim de Jogo
    def show_victory_screen(self, result):
        # Cria uma nova janela para mostrar o resultado da partida
        popup = tk.Toplevel(self.root)
        popup.title("Fim de Jogo!")
        popup.geometry("500x450")
        popup.configure(bg="#FFD1DC")
        popup.transient(self.root) 
        popup.grab_set() 

        x = self.root.winfo_x() + (self.root.winfo_width() // 2) - 250
        y = self.root.winfo_y() + (self.root.winfo_height() // 2) - 225
        popup.geometry(f"+{x}+{y}")

        canvas = tk.Canvas(popup, width=500, height=300, bg="#FFD1DC", highlightthickness=0)
        canvas.pack(pady=10)

        colors = ["#FF1493", "#FF4500", "#1E90FF", "#32CD32", "#FFD700", "#8A2BE2"]
        
        if result == "Empate":
            canvas.create_text(250, 150, text="Empate! 🤝\nFoi por pouco!", font=('Comic Sans MS', 30, 'bold'), fill="#4B0082", justify="center")
        else:
            text_id = canvas.create_text(250, 150, text=f"🎉 {result} VENCEU! 🎉", font=('Comic Sans MS', 40, 'bold'), fill="#FF1493")
            
            particles = []
            for _ in range(80):
                px = random.randint(0, 500)
                py = random.randint(-300, 0)
                size = random.randint(8, 16)
                color = random.choice(colors)
                shape = canvas.create_oval(px, py, px+size, py+size, fill=color, outline="") if random.random() > 0.5 else canvas.create_rectangle(px, py, px+size, py+size, fill=color, outline="")
                speed_y = random.randint(3, 10)
                speed_x = random.choice([-3, -2, -1, 0, 1, 2, 3])
                particles.append({'id': shape, 'dx': speed_x, 'dy': speed_y})

            # Controla a animação da tela
            def animate():
                # Verifica se a janela ainda existe ou se ela foi fechada, para a animação
                if not popup.winfo_exists(): return
                # Pega a cor atual do texto e muda para a próxima cor da lista
                current_color = canvas.itemcget(text_id, "fill")
                next_color = colors[(colors.index(current_color) + 1) % len(colors)] if current_color in colors else colors[0]
                canvas.itemconfig(text_id, fill=next_color)

                # Percorre todas as partículas e movimenta cada uma de acordo com sua velocidade (dx e dy)
                for p in particles:
                    canvas.move(p['id'], p['dx'], p['dy'])
                    coords = canvas.coords(p['id'])
                    if coords and coords[1] > 350:
                        canvas.move(p['id'], 0, -400) 

                popup.after(80, animate)
            
            animate() # inicia a animação

        btn_frame = tk.Frame(popup, bg="#FFD1DC")
        btn_frame.pack(pady=10)
        
        btn_config = {'font': ('Comic Sans MS', 12, 'bold'), 'relief': 'ridge', 'bd': 5}
        tk.Button(btn_frame, text="🔄 Jogar Novamente", bg="#98FB98", command=lambda: [popup.destroy(), self.start_game(self.mode)], **btn_config).pack(side='left', padx=10)
        tk.Button(btn_frame, text="🏠 Menu Principal", bg="#87CEFA", command=lambda: [popup.destroy(), self.build_menu()], **btn_config).pack(side='left', padx=10)
