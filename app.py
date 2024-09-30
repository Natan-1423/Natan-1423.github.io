from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    email = request.form.get('email')
    username = request.form.get('username')
    birthday = request.form.get('birthday')
    password = request.form.get('password')

    # Here you would normally save the user information to a database
    # For demonstration, we'll just print it to the console
    print(f'Registering user: {username}, Email: {email}, Birthday: {birthday}')

    # Redirect to a login page or homepage after registration
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Login Page"

if __name__ == '__main__':
    app.run(debug=True)
