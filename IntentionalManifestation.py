datetime.date.today() - {gratitude}
print("Gratitude recorded!")

def main():
    """Main function to run the app."""
    while True:
        print("\nManifest App Menu:")
        print("1. Set Intention")
        print("2. Visualize")
        print("3. Create Affirmation")
        print("4. Repeat Affirmations")
        print("5. Express Gratitude")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '6':
            print("\nCongratulations on completing your manifestational attempt!")
            print("Remember, consistency is key. Keep manifesting your dreams!")
            break