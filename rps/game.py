# Write your code here
import random


class Game:
    def __init__(self):
        self.element_dict = dict()
        self.score = Score()

    def game(self, user_pick):
        computer_pick = random.choice(list(self.element_dict.keys()))
        if user_pick == computer_pick:  # tie
            print(f"There is a draw ({computer_pick})")
            return 0
        elif computer_pick not in self.element_dict[user_pick]:
            print(f"Well done. Computer chose {computer_pick} and failed")  # you win
            return 1
        else:
            print(f"Sorry, but computer chose {computer_pick}")  # you lose
            return -1

    def game_result(self, user_pick):
        rate = 0
        result = self.game(user_pick)
        if result == 0:
            rate += 50
        elif result == 1:
            rate += 100
        return rate

    def which_game(self, user_pick_list):
        # if the input is empty ---> simple game["scissors", "rock", "paper"]
        if user_pick_list == [""]:
            user_pick_list = ["scissors", "rock", "paper"]
        # if the input isn't empty  ---> complex game
        list_len = len(user_pick_list) // 2
        for i in range(list_len + 1):
            self.element_dict[user_pick_list[i]] = user_pick_list[i + 1: i + 1 + list_len]
        for i in range(list_len + 1, len(user_pick_list)):
            end = user_pick_list[i + 1:]
            start = user_pick_list[:list_len - len(user_pick_list) + i + 1]
            self.element_dict[user_pick_list[i]] = end + start
        return user_pick_list, self.element_dict

    def run(self):
        self.score.read_from_file()
        user_name = input("Enter your name:")
        print(f"Hello, {user_name}")
        self.score.user_rating(user_name)
        user_pick_list = input().replace(" ", "").split(',')
        user_pick_list, element_dict = self.which_game(user_pick_list)
        print("Okay, let's start")
        while True:
            user_pick = input()
            if user_pick == "!exit":
                print("Bye!")
                self.score.write_to_file()
                return
            elif user_pick == "!rating":
                print("Your rating: " + str(self.score.scores[user_name]))
            elif user_pick not in user_pick_list:
                print("Invalid input")
            else:
                rate = self.game_result(user_pick)
                self.score.scores[user_name] += rate


class Score:
    def __init__(self):
        self.scores = dict()

    def write_to_file(self):
        file = open('rating.txt', 'w')
        for key, value in self.scores.items():
            print(f'{key} {value}', file=file, flush=True)
        file.close()

    def read_from_file(self):
        file = open('rating.txt', 'r')
        for line in file:
            name = line.split(" ")[0]
            rate = int(line.split(" ")[1])
            self.scores[name] = rate
        file.close()

    def user_rating(self, user_name):
        if user_name not in self.scores.keys():
            self.scores[user_name] = 0


if __name__ == '__main__':
    game = Game()
    game.run()
