# from openai import OpenAI
 
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="Enter your openai api",
# )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)










import google.generativeai as genai

# Configure Gemini AI with your API key
genai.configure(api_key="AIzaSyCvGIIAJAW43kdC2x0EUAU_6q9tFmNSxdw")

# Initialize the Gemini AI model
model = genai.GenerativeModel("gemini-pro")

def aiProcess(command):
    response = model.generate_content(command)
    return response.text.strip() if response.text else "Sorry, I couldn't understand that."

# Example usage
if __name__ == "__main__":
    print(aiProcess("What is coding?"))


