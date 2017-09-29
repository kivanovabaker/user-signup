from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', title="User-Signup")

@app.route("/", methods=['POST'])

def validate_input():
    username = request.form['username']
    password = request.form['password']
    v_password = request.form['v_password']
    email = request.form['email']

    username_error=""
    password_rule_error=""
    match_error=""
    email_error=""

    if " " in username or len(username)<3 or len(username)>20:
        username_error = "Please enter a valid username (3-20 chars, no spaces)"
        username = ""
    if " " in password or len(password)<3 or len(password)>20:
        password_rule_error = "Please enter a valid password (3-20 chars, no spaces)"
    if password != v_password:
        match_error = "Please enter matching passwords"
    if len(email) == 0:
        email_error = ""
    else:
        if email.count("@") != 1 or email.count(".") != 1 or " " in email or len(email)<3 or len(email)>20:
            email_error = "Please enter a valid email"
            email = ""

    if not username_error and not password_rule_error and not match_error and not email_error:
        return render_template('welcome.html', title='Welcome!', username=username)
    else:
        return render_template('index.html', title="User-Signup Error", username=username, email=email, 
        username_error=username_error, password_rule_error=password_rule_error, match_error=match_error,
        email_error=email_error)

app.run()