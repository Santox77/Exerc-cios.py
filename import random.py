
import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo de Adivinhação")

        self.numero = random.randint(1, 10)
        self.attempts = 0

        self.label = tk.Label(root, text="Adivinhe um número entre 1 e 10")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Adivinhar", command=self.check_guess)
        self.button.pack()

    def check_guess(self):
        guess = int(self.entry.get())
        self.attempts += 1

        if guess == self.numero:
            messagebox.showinfo("Resultado", f"Parabéns! Você acertou em {self.attempts} tentativas.")
            self.root.destroy()
        else:
            messagebox.showerror("Resultado", "Ah, você errou. Tente novamente.")

if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
