from tavily import TavilyClient
import os
import dotenv
import time
from prompts_generate import PromptsGenerate
from writer import Writer
import json

dotenv.load_dotenv()
tavily_api = os.getenv("tavily_api")
client = TavilyClient(api_key=tavily_api)
writer = Writer()
PromptsGenerator = PromptsGenerate()

class news_agent:
    def __init__(self):
        self.query = PromptsGenerator.generate()
        self.params = {
            "search_depth": "advanced",
            "topic": "news",
            "include_raw_content": True,
            "include_images": False
        }
        print("News Agent Initialized!")

    def search(self):
        print("Start Searching...")
        with open("./txt/news.txt", "a", encoding="utf-8") as f:
            f.write("")
        
        for i in range(1, 6):
            self.response = client.search(self.query, **self.params)
            result = self.response["results"]
            self.search_result = []
            for news  in result:
                rouud_result = []
                title = news["title"]
                score = news["score"]
                date = news["published_date"]
                content = news["raw_content"]
                resp = f"Title: {title}\nScore: {score}"
                rouud_result.append(resp) 
                with open("./txt/news.txt", "a", encoding="utf-8") as f:
                    f.write(f"\n# {title}\n")
                    f.write(f"- Published Date: {date}\n\n")
                    f.write(f"{content}\n")
                    f.write("---\n\n")
                    time.sleep(2)
            self.search_result.append(f"search result:{rouud_result}")
            print(f"searching round {i} done!")
            PromptsGenerator.set_history("user",str(self.search_result))
            self.query = PromptsGenerator.generate()
        with open("./history.json", "w", encoding="utf-8") as f:
            history = PromptsGenerator.history
            history = json.dumps(history, indent=4)
            f.write(history)
        print("Searching Done!")
        

    def write(self):
        print("Start Writing...")
        with open("./news.md", "w", encoding="utf-8") as f:
            f.write("")
        print("Pre-writing...")
        writer.pre_write()
        print("Writing...")
        news = writer.write()
        with open("./news.md", "w", encoding="utf-8") as f:
            f.write(news)
        print("Writing Done!")
        print("News Agent Done!")
