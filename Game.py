from random import randrange

# data
rock = {1: "lose", 2: "win"}
paper = {0: "win", 2: "lose"}
scissors = {0: "lose", 1: "win"}

items = {0: "Rock", 1: "Paper", 2: "Scissors"}
pack = (rock, paper, scissors)

# end data

def play():
    result = False
    while result != True:
        player_1_num = pack.index(pack[randrange(len(pack))])  # индекс этого словаря в списке
        player_2_num = pack.index(pack[randrange(len(pack))])  # индекс этого словаря в списке

        if player_1_num == player_2_num:
            print("Tie\n", f"Player 1 choose :({items[player_1_num]})\n", f"Player 2 choose :({items[player_2_num]})\n")
        else:
            print("Player 1: ", pack[player_1_num][player_2_num], f"({items[player_1_num]})\n", "Player 2: ",
                  pack[player_2_num][player_1_num], f"({items[player_2_num]})\n")
            result = True


play()
