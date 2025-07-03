import os
import json
from google import generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")

def generate_recommendation(city: str, risks: list):
    prompt = f"""
    Şehir: {city}
    Risk Türleri: {', '.join(risks)}

    Yukarıdaki şehirde bu afet türlerine karşı alınması gereken önlemleri ve bir olay durumunda yapılacakları 5-10 maddelik sade ve anlaşılır bir şekilde açıkla.
    """

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Hata oluştu: {str(e)}"
