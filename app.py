import os
import openai
from flask import Flask, request, render_template
from dotenv import load_dotenv
load_dotenv()  # This line will load the .env file


app = Flask(__name__)

# Set the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')
print("API Key:", os.getenv('OPENAI_API_KEY'))


def get_openai_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",  # The chat model identifier
        temperature=0.7, 
        messages=[
            {"role": "system", "content": "You are a knowledgeable assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message['content'].strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        script = request.form['script']
        article = get_openai_response(script)
        return render_template('result.html', article=article)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
