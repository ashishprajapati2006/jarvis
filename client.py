import google.generativeai as genai

# Configure Gemini AI with your API key
genai.configure(api_key="gemini api")

# Initialize the Gemini AI model
model = genai.GenerativeModel("gemini-pro")

def aiProcess(command):
    response = model.generate_content(command)
    return response.text.strip() if response.text else "Sorry, I couldn't understand that."

# Example usage
if __name__ == "__main__":
    print(aiProcess("What is coding?"))


