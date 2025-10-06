from flask import Flask, render_template, request
from summary import summarizer 


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET','POST'])
def analyze():
    if request.method == 'POST':
        text = request.form['text']
        summary, text , original_length, summary_length = summarizer(text)
    
    return render_template('summary.html', original_text=text, summary=summary, original_length=original_length, summary_length=summary_length)

if __name__ == '__main__':
    app.run(debug=True)

