import random
import os

def number_guessing_game():
    print("\n--- Number Guessing Game ---")
    target = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("I have picked a number between 1 and 100. You have 10 attempts!")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
            
        attempts += 1
        
        if guess < target:
            print("Too low!")
        elif guess > target:
            print("Too high!")
        else:
            score = max(100 - (attempts - 1) * 10, 10)
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
            print(f"Your Score: {score} points")
            return
            
    print(f"Game Over! The correct number was {target}.")

def word_counter_tool():
    print("\n--- Text File Word Counter ---")
    filename = input("Enter the path/name of the text file to analyze (e.g., sample.txt): ").strip()
    
    if not os.path.exists(filename):
        print(f"File '{filename}' not found. Creating a sample file for demonstration...")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("Python is an amazing programming language. Python is widely used for automation, data science, and web development.")
            print(f"'{filename}' created successfully with sample text.")
        except Exception as e:
            print(f"Error creating file: {e}")
            return

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        words = content.lower().split()
        total_words = len(words)
        
        word_freq = {}
        for word in words:
            cleaned_word = ''.join(char for char in word if char.isalnum())
            if cleaned_word:
                word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1
                
        print(f"\nTotal words in file: {total_words}")
        print("Top Word Frequencies:")
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        for word, freq in sorted_words[:5]:
            print(f"  - '{word}': {freq} time(s)")
            
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    while True:
        print("\n--- Project 02: Number Guessing Game & Word Counter ---")
        print("1. Play Number Guessing Game")
        print("2. Run Text File Word Counter")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ").strip()
        
        if choice == '1':
            number_guessing_game()
        elif choice == '2':
            word_counter_tool()
        elif choice == '3':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
