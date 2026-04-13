from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret123'   # needed for session

# Dummy user (no database for now)
USER = {
    "username": "admin",
    "password": "1234"
}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER["username"] and password == USER["password"]:
            session['user'] = username
            return redirect('/dashboard')
        else:
            return "Invalid credentials"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html')
    return redirect('/login')

@app.route('/profile')
def profile():
    if 'user' in session:
        return render_template('profile.html')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)