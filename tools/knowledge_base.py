from confg import loadenv

import google.generativeai as genai

API_KEY = loadenv.GEMINI_API_KEY

class KnowledgeBase:
    def __init__(self):
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-flash")

    def evaluate(self, query: str)->str:
        print("Evaluating query:", query)
        response = self.model.generate_content(query)
        return response.text