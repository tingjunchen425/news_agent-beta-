import google.generativeai as generativeai
import os
import dotenv

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Extractor:
    def __init__(self):
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction="You should extract the news content from the file text.Make sure the output is in a readable format.If there are different news, separate them with a line break.",
        )
        self.file_path = './txt/browser.txt'

    def extract(self,prompts):
        self.client = generativeai.upload_file(self.file_path)
        response = self.model.generate_content([self.client,prompts])
        return response.text