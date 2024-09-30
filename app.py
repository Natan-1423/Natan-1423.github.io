from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    birthday = request.form['birthday']
    password = request.form['password']
    # Add logic to save this data, validate, etc.
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
