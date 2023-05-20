from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def results():
    message = request.form['message']
    return render_template('results.html', message=message)
import requests

def results():
    message = request.form['message']

    # Make API call to ChatGPT API
    api_key = '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'
    headers = {
        'Authorization': 'Bearer ' + api_key,
        'Content-Type': 'application/json'
    }
    data = {
        'message': message,
        'context': 'Optional context for the API call'
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', json=data, headers=headers)

    if response.status_code == 200:
        chat_result = response.json()
        # Extract the generated response from the API response and pass it to the template
        generated_message = chat_result['choices'][0]['message']['content']
        return render_template('results.html', message=message, generated_message=generated_message)
    else:
        # Handle API error or failed request
        return

