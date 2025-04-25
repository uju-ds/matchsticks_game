def main():
    num_sticks = 21
    players = ["Player 1", "Player 2"]
    current_player_index = 0

    print("Game of sticks")
    for moves in range(1000):
        valid_input = False
        while not valid_input:
            try:
                num_input = int(input(f"{players[current_player_index]} enter how many sticks to remove: "))
                if 1 <= num_input <= 3 :
                    valid_input = True
                else:
                    print("Must remove between 1-3 sticks!")
            except ValueError:
                print("Invalid input. Please enter a number.")

        num_sticks -= num_input

        if num_sticks <= 0:
            print(f"{players[current_player_index]} lost the game!")
            break
        else:
            print(f"There are {num_sticks} sticks left")

        current_player_index = (current_player_index + 1) % 2

if __name__ == "__main__":
    main()
