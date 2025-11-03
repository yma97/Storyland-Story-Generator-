from story_generator import StoryGenerator

def main():
    """
    Main function to interact with the user, collect inputs, and generate a story.
    """
    print("Welcome to the Story Generator!")
    
    # Collect user inputs
    first_char_name = input("What is the name of the first character? ").strip()
    second_char_name = input("What is the name of the second character: ").strip()
    available_themes = ["adventure", "romance", "mystery", "fantasy", "sci-fi"]
    print("\nhat would be the theme of the story? Available themes:")
    for i, theme in enumerate(available_themes, 1):
        print(f"{i}. {theme.capitalize()}")
    
    # Prompt user to select a theme
    while True:
        try:
            theme_choice = int(input(f"Choose a theme by entering the number (1-{len(available_themes)}): ").strip())
            if 1 <= theme_choice <= len(available_themes):
                theme = available_themes[theme_choice - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(available_themes)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    main_storyline = input("What kind of story line you have in mind (optional, press Enter to skip): ").strip()
    
    # If the user skips the storyline, set it to None
    main_storyline = main_storyline if main_storyline else None

    # Initialize the StoryGenerator
    generator = StoryGenerator()

    # Generate the story
    print("\n📖 Generating your personalized story...\n")
    story = generator.generate_story(first_char_name, second_char_name, theme, main_storyline)

    # Display the generated story
    print("Here is your story:\n")
    print(story)
    print("\n✨ Sweet dreams! 🌙")

if __name__ == "__main__":
    main()