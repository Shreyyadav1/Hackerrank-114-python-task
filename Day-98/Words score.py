def score_words(words):
    score = 0
    vowels = "aeiouy"

    # Check every word
    for word in words:

        # Count vowels in current word
        num_vowels = 0

        for letter in word:
            if letter in vowels:
                num_vowels += 1

        # Even vowels = 2 points
        if num_vowels % 2 == 0:
            score += 2

        # Odd vowels = 1 point
        else:
            score += 1

    return score


# -------- Main Program --------

# Number of words
n = int(input("Enter number of words: "))

# Input words
words = input("Enter words separated by space: ").split()

# Check if user entered correct number of words
if len(words) != n:
    print("Warning: Number of words does not match the value of n.")

# Print final score
print("Score =", score_words(words))