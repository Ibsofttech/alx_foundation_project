from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Hardcoded credentials for demonstration purposes
users = {"ibrahim": "password123"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Simple authentication check
        if username in users and users[username] == password:
            return redirect(url_for('index'))
        else:
            return "Invalid username or password", 401
    
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
