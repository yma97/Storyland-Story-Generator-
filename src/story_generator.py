from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class StoryGenerator:
    def __init__(self):
        """
        Initialize the StoryGenerator class by setting up the OpenAI client.
        """
        self.client = OpenAI(
            api_key = os.getenv("DEEPSEEK_API_KEY"),
            base_url="https://api.deepseek.com"
        )
    
    def _create_prompt(self, first_char_name, second_char_name, theme, main_storyline):
        """
        Create a prompt for the story generation based on user inputs.

        Args:
            first_char_name (str): The name of the first character.
            second_char_name (str): The name of the second character.
            theme (str): The theme of the story.
            main_storyline (str, optional): The main storyline or plot. Defaults to None.
        
        """
        try:
            prompt = (
                f"Create a captivating story with the following details:\n"
                f"First Character Name: {first_char_name}\n"
                f"Second Character Name: {second_char_name}\n"
                f"Theme: {theme}\n"
            )
            
            if main_storyline:
                prompt += f"Main Storyline: {main_storyline}\n\n"
            else:
                prompt += "\n"

            prompt += """The story should be engaging and imaginative.
            Important: Please respond in the SAME LANGUAGE as this request. 
            If the name, theme, or main storyline are in Chinese, write the story in Chinese. 
            If they are in English, write in English."""
            return prompt
        except Exception as e:
            return f"An error occurred while creating the prompt: {e}"

    def generate_story(self, first_char_name, second_char_name, theme, main_storyline, max_token):
        """
        Generate a personalized story based on the given inputs.

        Args:
            first_char_name (str): The name of the first character.
            second_char_name (str): The name of the second character.
            theme (str): The theme of the story.
            main_storyline (str, optional): The main storyline or plot. Defualts to None.

        Returns:
            str: The generated story.
        """
        prompt = self._create_prompt(first_char_name, second_char_name, theme, main_storyline)

        try:
            response = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[ {"role": "system", "content": "You are a creative storyteller who writes warm, engaging, healing stories."},
                        {"role": "user", "content": prompt}],
                max_tokens=max_token,
                temperature=0.5
            )
            story = response.choices[0].message.content
            return story
        except Exception as e:
            return f"An error occurred: {e}"