from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_submit', methods=['POST'])  # Ensure you specify POST here
def register_submit():
    email = request.form['email']
    username = request.form['username']
    birthday = request.form['birthday']
    password = request.form['password']

    # Process the data (save, validate, etc.)
    return "Registration Successful!"  # Redirect or render a success page

if __name__ == '__main__':
    app.run(debug=True)
