from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os
from Extractor import Extractor

load_dotenv()
api = os.getenv('gemini_api')
task = "Go to CNN, find world news, click on the first news, and return the news content."

with open('news_agent/browser.txt', "w", encoding="utf-8") as f:
    f.write("")
async def main():
    agent = Agent(
        task=task,
        llm=ChatGoogleGenerativeAI(api_key=api,model="gemini-2.0-flash"),
    )
    result = await agent.run()
    print(result)
    result = str(result)
    with open('news_agent/browser.txt', "a", encoding="utf-8") as f:
        f.write(result)

if __name__ == '__main__':
    asyncio.run(main())
    extractor = Extractor()
    print('-'*50)
    print("Extracting news content...")
    news = extractor.extract("use text format, not markdown.Output the news content as a readable format.")
    print(news)
    with open('./txt/browser.txt', "w", encoding="utf-8") as f:
        f.write(news)
    print("Done")


