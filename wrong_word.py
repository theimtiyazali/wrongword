import difflib

# List of valid words
valid_words = ["apple", "banana", "orange", "grape", "strawberry", "blueberry"]

# Function to check if a word is valid
def check_word(word, valid_words):
    if word in valid_words:
        print(f"'{word}' is a valid word.")
        return True
    else:
        close_matches = difflib.get_close_matches(word, valid_words)
        raise ValueError(f"'{word}' is not available. Did you mean: {', '.join(close_matches) if close_matches else 'No suggestions available'}?")

# Function to handle word input and error tracking
def word_input_handler():
    wrong_words = []
    consecutive_wrong = 0

    while True:
        word = input("Enter a word: ").strip().lower()

        try:
            check_word(word, valid_words)
            consecutive_wrong = 0  # Reset consecutive wrong counter on valid input
        except ValueError as e:
            wrong_words.append(word)
            consecutive_wrong += 1
            print(e)
            
            if consecutive_wrong >= 2:
                wrong_word_list = ', '.join(wrong_words)
                print(f"Consecutively entered wrong words: {wrong_word_list}")
                for wrong_word in wrong_words:
                    close_matches = difflib.get_close_matches(wrong_word, valid_words)
                    print(f"Suggestions for '{wrong_word}': {', '.join(close_matches) if close_matches else 'No suggestions available'}")

                # Reset the list of wrong words
                wrong_words = []

if __name__ == "__main__":
    word_input_handler()
