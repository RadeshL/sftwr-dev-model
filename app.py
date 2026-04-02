from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/signup',methods = ['GET'])
def signup_page():
    return render_template('signup.html')

@app.route('/signup', methods = ['POST'])
def signup():
    username = request.form['username']
    password = request.form['pswd']

    with open('users.txt', 'a') as f:
        f.write(f"{username},{password}\n")

    return redirect('/signup')

if __name__ == '__main__':
    app.run(debug = True)
