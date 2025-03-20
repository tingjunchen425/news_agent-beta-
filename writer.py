import google.generativeai as generativeai
import os
import dotenv

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Writer:
    def __init__(self):
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-pro-exp-02-05",
            system_instruction="""You are a news agent. You should convert the news content to a readable format.Use zh-TW as the target language.Use markdown format.
            If there is news on the same topic, merge them into one.
            The end of the news content should be marked with '\n'."""
        )
        self.thinking = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction="You are a news agent. You should convert the news content to a readable format."
        )
        self.file_path = './txt/news.txt'
        with open(self.file_path, 'w', encoding='utf-8') as f:
            f.write("")

    def pre_write(self):
        self.prompts = "Translate every international news into a readable format for the public."
        self.client = generativeai.upload_file(self.file_path)
        response = self.thinking.generate_content([self.client, self.prompts])
        with open('./txt/prewrite.txt', 'w', encoding='utf-8') as f:
            f.write(response.text)
        self.client = generativeai.upload_file('./txt/prewrite.txt')

    def write(self):
        self.prompts = "translate the news content into a readable format for the public."
        response = self.model.generate_content([self.client, self.prompts])
        return response.text
