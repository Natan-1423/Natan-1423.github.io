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
