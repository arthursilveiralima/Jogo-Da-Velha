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
        tk.Button(self.root, text="🤖 Jogar contra Robô", bg="#87CEFA", fg="black", command=self.build_difficulty_menu, **btn_config).pack(pady=15)
        tk.Button(self.root, text="😎 Jogar contra Amigo", bg="#98FB98", fg="black", command=lambda: self.start_game('friend'), **btn_config).pack(pady=15)
        tk.Button(self.root, text="🚀 Testar Robô 100 vezes", bg="#FFFACD", fg="black", command=self.run_tests, **btn_config).pack(pady=15)