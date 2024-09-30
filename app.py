from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    birthday = request.form['birthday']
    password = request.form['password']
    # Add logic to save this data
    return redirect(url_for('success'))  # Redirect to a success page or homepage
@app.route('/login_submit', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    # Add logic to validate the user credentials here
    return redirect(url_for('homepage'))  # Redirect to the homepage or another page
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/login_submit', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']
    # Add your authentication logic here
    return redirect(url_for('home'))

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/register_submit', methods=['POST'])
def register_submit():
    # Handle registration logic here
    pass
python app.py
chmod +x start_flask.sh
./start_flask.sh
