import google.generativeai as generativeai
import os
import dotenv

dotenv.load_dotenv()
api = os.getenv('gemini_api')
generativeai.configure(api_key=api)

class PromptsGenerate:
    def __init__(self):
        self.history = []
        adjustments = """
        1. return the full text of the article
        2. return only text, without any video
        3. return no URL links in the content
        """
        system_prompts = f"""You are going to generate a search querys for tavily API to search.There should only be a single query in the content
        If there are multiple queries,compare the results of each query and return the most relevant one.
        The query should meet several adjustments:
        {adjustments}
        The return type should be a string.
        """
        self.model = generativeai.GenerativeModel(
            model_name="gemini-2.0-flash-thinking-exp-01-21",
            system_instruction=system_prompts
        )

    def generate(self):
        prompts = f"""Search for international news in the past 24 hours from CNN, BBC,DW and Al Jazeera."""
        chat = self.model.start_chat()
        response = chat.send_message(prompts)
        self.set_history("model",response.text)
        return response.text
    
    def set_history(self,role,text):
        self.history.append({
            "role": role,
            "parts": [
                text,
            ],
        })

