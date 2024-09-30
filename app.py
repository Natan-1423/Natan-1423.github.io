from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    birthday = request.form['birthday']
    password = request.form['password']
    
    # Here, process the data (e.g., save to a database)
    # Validate data as necessary.

    return "Registration successful!"

if __name__ == '__main__':
    app.run(debug=True)
