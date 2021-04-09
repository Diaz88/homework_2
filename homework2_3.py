class Word:
    def __init__(self, word, help):
        self.word = word
        self.help = help

    def check_letter(self, letter):
        return f'{self.word}, {self.help}'

    def __str__(self):
        return f'hidden words: {self.word}\nhints: {self.help}'

arr = ['hanger','airplane', 'earth']
arr1 = ['h....r', 'a......e', 'e...h']
a = Word(arr, arr1)
print(a)

class Game:
    # 1 - 3hp, 2  - 2hp, 3 - 1hp
    def __init__(self, round, dif):
        self.round_num = round
        self.hp = dif

    def play(self):
        return f'the game has begun'


diff = input('Select the difficulty level:')
round_num = input('Next round:')

g = Game(round_num, diff)
print(g.play())