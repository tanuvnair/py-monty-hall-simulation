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

def main():
    n = 1000

    player_did_switch = {"win": 0, "loss": 0}
    for num in range(n):
        if (monty_hall(True)):
            player_did_switch["win"] += 1
        else:
            player_did_switch["loss"] += 1
    print(player_did_switch)

    player_did_not_switch = {"win": 0, "loss": 0}
    for num in range(n):
        if (monty_hall(False)):
            player_did_not_switch["win"] += 1
        else:
            player_did_not_switch["loss"] += 1
    print(player_did_not_switch)

main()
