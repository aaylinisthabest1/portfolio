from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    email = request.form['email']
    comment = request.form['text']
    
    with open('feedback.txt', 'a') as f:
        f.write(f'Email: {email}\nComment: {comment}\n\n')
    
    return 'Thank you for your feedback!'

if __name__ == '__main__':
    app.run(debug=True)

