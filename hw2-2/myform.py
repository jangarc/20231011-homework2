import flask
from flask import Flask, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash

def check_password(password):
    with open('mysecret', 'r') as f:
      passwordhash = f.read().strip()
    return check_password_hash(passwordhash, password)

def set_password(password):
    return generate_password_hash(method='pbkdf2:sha512:150000', password=password)

app = flask.Flask(__name__)
@app.route("/myform")
def form():
    return render_template('myform.html')

@app.route("/submit", methods=['POST'])
def submit():
    account = request.values['account']
    password = request.values['password']
    passwordhash = set_password(password)
    
    try:
    	assert check_password(password)
    except AssertionError:
        print("<H1> Error Account or Password! </H1>"+passwordhash)
        return render_template('myform.html')
        
    return render_template('resp.html', **locals())
    
    """
    if check_password(passwordhash, password) is True:
        return render_template('resp.html', **locals())
    else:
        print("<H1> Error Account or Password! </H1>"+passwordhash+"<div>"+password+"</div>")
        return render_template('myform.html')
	"""

if __name__ == '__main__':
    app.run()
