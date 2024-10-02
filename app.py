@app.route('/register_submit', methods=['POST'])
def register_submit():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']
    birthday = request.form['birthday']
    
    # Process the data (save to database, validate, etc.)
    
    return 'Registration successful'
flask run
