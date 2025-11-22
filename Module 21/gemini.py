from google import genai
import os

# Directly pass your API key here (not recommended for production)
api_key = "AIzaSyBBc1LVouv9tCqei9nvKTGieHc69va-ZhY"

# Correct way to initialize the client
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Write an article about cat within 100 words"
)

print(response.text)
