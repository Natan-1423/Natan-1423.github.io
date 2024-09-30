from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    birthday = request.form['birthday']
    password = request.form['password']
    
    # Here you would add your logic to save the data
    # e.g., save to a database or file

    return redirect(url_for('success'))  # Redirect to a success page

@app.route('/success')
def success():
    return "Registration Successful!"

if __name__ == '__main__':
    app.run(debug=True)
