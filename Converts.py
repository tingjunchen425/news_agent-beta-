import google.generativeai as generativeai
import os
import dotenv

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class Convert:
    def __init__(self):
        system_prompts = f"""You are a news agent. You should convert the news content to a readable format"""
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-pro-exp-02-05",
            system_instruction=system_prompts
        )

    def convert(self,news_content):
        response = self.model.generate_content(news_content)
        return response.text