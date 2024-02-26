import random

class CrosswordPuzzle:
    def __init__(self):
        self.grid = [['_' for _ in range(10)] for _ in range(10)]
        self.words = ['PYTHON', 'CROSSWORD', 'PUZZLE', 'GAME', 'DEVELOPMENT']
        random.shuffle(self.words)

    def create_puzzle(self):
        for word in self.words:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                x = random.randint(0, 10 - len(word))
                y = random.randint(0, 9)
                for i, letter in enumerate(word):
                    self.grid[y][x + i] = letter
            else:
                x = random.randint(0, 9)
                y = random.randint(0, 10 - len(word))
                for i, letter in enumerate(word):
                    self.grid[y + i][x] = letter

    def play(self):
        print("Bienvenue dans le jeu de mots croisés!")
        self.display_grid()
        while True:
            guess = input("Entrez un mot ou 'q' pour quitter: ").upper()
            if guess == 'Q':
                break
            if guess in self.words:
                print("Mot trouvé!")
                self.words.remove(guess)
            else:
                print("Mot incorrect. Réessayez.")
            if not self.words:
                print("Félicitations! Vous avez trouvé tous les mots.")
                break

    def display_grid(self):
        for row in self.grid:
            print(' '.join(row))

if __name__ == "__main__":
    main()
