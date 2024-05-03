# Importing py. Vars
import typer
import time


# Def Function 1
def play_game():
    print("Welcome to the Speed Typing Game!")
    total_score = 0

    # Levels Define to the Console
    levels = [
        {"difficulty": "easy", "num_rounds": 3},
        {"difficulty": "medium", "num_rounds": 4},
        {"difficulty": "hard", "num_rounds": 4},
        {"difficulty": "expert", "num_rounds": 5},
        {"difficulty": "insane", "num_rounds": 5}
    ]
    # For Command filter
    for level_num, level_info in enumerate(levels, start=1):
        print("\nLevel " + str(level_num) + ": " + level_info["difficulty"].capitalize())

        for round_num in range(1, level_info["num_rounds"] + 1):
            print("\nRound " + str(round_num))

            words_to_type = typer.generate_words(round_num, level_info["difficulty"])
            time_limit = typer.calculate_time_limit(level_info["difficulty"])

            print("Type the following words within " + str(time_limit) + " seconds:")
            print(words_to_type)

            start_time = time.time()
            response = input(">> ")
            end_time = time.time()
            # conditional between timer and typing time
            if response == words_to_type and end_time - start_time <= time_limit:
                time_left = time_limit - (end_time - start_time)
                score = typer.calculate_score(time_left, len(words_to_type.split()))
                print("Good job! Score for this round:", score)
                total_score += score
            else:
                print("Oops! You made a mistake or ran out of time.")
                print("Game over!")
                print("Total score:", total_score)
                return
    # Final Game over statement
    print("\nCongratulations! You completed all levels!")
    print(f"Final score: {total_score}")


play_game()
