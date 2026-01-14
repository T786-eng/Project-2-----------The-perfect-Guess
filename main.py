import random

n = random.randint(1, 100)
guesses = 0
a = None

while a != n:
    try:
        a = int(input("Guess the number: ").strip())
        guesses += 1
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if a < n:
        print("Try a higher number.")
    elif a > n:
        print("Try a lower number.")

print(f"You guessed the number {n} correctly in {guesses} attempts.")
