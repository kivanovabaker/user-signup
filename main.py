from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html', title="User-Signup")

@app.route("/", methods=['POST'])
#where errors will be displayed:
#error if required field empty
#         user name or password contains a space, <3 or >20 chars
#         two passwords don't match
#         email invalid (does not contain one '@' and '.', contains space, <3 or >20 chars )
#error displayed near related field
#for username and email type, preserve if no error
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
        username_error = "Please enter a valid username"
        username = ""
    if " " in password or len(password)<3 or len(password)>20:
        password_rule_error = "Please enter a valid password"
    if password != v_password:
        match_error = "Please enter matching passwords"
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