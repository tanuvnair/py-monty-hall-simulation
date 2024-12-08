import random

def random_exclude(min_val, max_val, excludes):
    while True:
        num = random.randint(min_val, max_val)
        if num not in excludes:
            return num

def monty_hall(isSwitching):
    doors = [0, 0, 0]
    random_index = random.randint(0, 2)
    doors[random_index] = 1

    initial_guess = random.randint(0, 2)
    revealed_door = random_exclude(0, 2, {initial_guess, random_index})

    if isSwitching:
        final_door = [i for i in range(3) if i != initial_guess and i != revealed_door][0]
    else:
        final_door = initial_guess

    if doors[final_door] == 1:
        return True
    else:
        return False

def print_results(title, result_dict):
    win_percentage = (result_dict["win"] / (result_dict["win"] + result_dict["loss"])) * 100
    loss_percentage = 100 - win_percentage

    print(f"\n{'='*40}")
    print(f"{title}")
    print(f"{'-'*40}")
    print(f"Total Wins: {result_dict['win']} ({win_percentage:.2f}%)")
    print(f"Total Losses: {result_dict['loss']} ({loss_percentage:.2f}%)")
    print(f"{'='*40}\n")

def main():
    n = 1000

    player_did_switch = {"win": 0, "loss": 0}
    for num in range(n):
        if (monty_hall(True)):
            player_did_switch["win"] += 1
        else:
            player_did_switch["loss"] += 1
    print_results("Player who switched doors", player_did_switch)

    player_did_not_switch = {"win": 0, "loss": 0}
    for num in range(n):
        if (monty_hall(False)):
            player_did_not_switch["win"] += 1
        else:
            player_did_not_switch["loss"] += 1
    print_results("Player who did not switch doors", player_did_not_switch)

main()
