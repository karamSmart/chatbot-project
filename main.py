import random

def play_game():
    secret_number = random.randint(1, 10)
    attempts = 3

    print("🎮 Welcome to Guess Game!")

    while attempts > 0:
        guess = input("Guess a number (1-10): ")

        if not guess.isdigit():
            print("❌ Please enter a number!")
            continue

        guess = int(guess)

        if guess == secret_number:
            print("🎉 You win!")
            return
        elif guess < secret_number:
            print("📉 Too low!")
        else:
            print("📈 Too high!")

        attempts -= 1
        print("Attempts left:", attempts)

    print("💀 You lost! The number was:", secret_number)


# 🔁 حلقة إعادة اللعب
while True:
    play_game()

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        print("👋 Thanks for playing!")
        break