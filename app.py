#this is python configuration file

from flask import Flask ,render_template

app=Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/s2s/api/signup')
def user_signup():
    return "this is a user signup page"

@app.route('/s2s/api/About')
def user_about():
     return "this is the content of user"

@app.route('/s2s/api/contact')
def user_contact():
     return "Users contact"


if __name__=="__main__":
        app.run(debug=True)

