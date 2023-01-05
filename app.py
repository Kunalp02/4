from flask import Flask, request, redirect, session

app = Flask(__name__)

# Set a secret key for encrypting session data
app.secret_key = 'my_secret_key'

users = {
    'kunal': '1234',
    'user2': 'password2'
}

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get the username and password from the form
        username = request.form['username']
        password = request.form['password']

        # Check if the username and password are correct
        if username in users and users[username] == password:
            # Store the logged-in status in the session
            session['logged_in'] = True

            # Redirect to the home page
            return 'Login successful'
        else:
            # The login was unsuccessful
            return 'Invalid username or password'
    else:
        # Show the login form (GET Method)
        return '''
            <form method="post">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <input type="submit" value="Log In">
            </form>
        '''

@app.route('/logout')
def logout():
    # Clear the session data
    session.clear()

    # Redirect to the home page
    return redirect('/')

if __name__ == '__main__':
    app.run()






