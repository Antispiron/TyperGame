import random
import time
import word_bank

def play_round(words, seconds):
    """Returns True if the user successfully completed the round."""
    start = time.time()
    response = input("(" + str(seconds) + " seconds) " + words + "\n")
    stop = time.time()

    within_time_limit = stop - start < seconds
    return response == words and within_time_limit

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words."""
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def pick_random_words(num_words, word_length):
    """Returns a random phrase containing the given number of words."""
    words = ""
    for word in range(num_words):
        word = get_random_word(word_length)
        words = words + " " + word

    return words.strip()

def get_random_word(mode):
    """Returns a random word with a word length based on the given mode."""
    if mode == "hard":
        words = word_bank.hard_words
    elif mode == "medium":
        words = word_bank.medium_words
    else:
        words = word_bank.easy_words

    return random.choice(words)


def generate_words(round_num, difficulty):
    """Generate words based on the round number and difficulty."""
    if difficulty == "easy":
        return pick_random_words(round_num, 5, 10)
    elif difficulty == "medium":
        return pick_random_words(round_num, 6, 8)
    elif difficulty == "hard":
        return pick_random_words(round_num, 7, 6)
    elif difficulty == "expert":
        return pick_random_words(round_num, random.randint(5, 8), random.randint(3, 5))
    elif difficulty == "insane":
        return pick_random_words(round_num, random.randint(5, 10), random.randint(2, 4))

def calculate_time_limit(difficulty):
    """Calculate the time limit based on the difficulty."""
    if difficulty == "easy":
        return 10
    elif difficulty == "medium":
        return 8
    elif difficulty == "hard":
        return 6
    elif difficulty == "expert":
        return 5
    elif difficulty == "insane":
        return 4

def calculate_score(time_left, num_words):
    """Calculate the score based on the time left and number of words."""
    return (time_left * 10) + (num_words * 5)

def generate_words(round_num, difficulty):
    """Generate words based on the round number and difficulty."""
    if difficulty == "easy":
        return pick_random_words(round_num, "easy")
    elif difficulty == "medium":
        return pick_random_words(round_num, "medium")
    elif difficulty == "hard":
        return pick_random_words(round_num, "hard")
    elif difficulty == "expert":
        return pick_random_words(round_num, "hard")  # Assuming expert level should use hard difficulty words
    elif difficulty == "insane":
        return pick_random_words(round_num, "medium")  # Example, using medium difficulty for insane level

    return random.choice(words)
