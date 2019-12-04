from flask import Flask , render_template
from wtforms_fields import *



# an instance of the flaskclass
app=Flask(__name__)
app.secret_key='replacelater'


@app.route("/", methods=['GET','POST'])
def reg():

    reg_form = RegistrationForm()
# #update database if validation sucessfull
#     if reg_form.validate_on_submit():
#         username = reg_form.username.data
#         password = reg_form.password.data
#         return redirect(url_for('login'))        

    return render_template("reg.html",form=reg_form)

@app.route("/login", methods=['GET','POST'])
def login():
    loginform = LoginForm()

    return render_template("login.html", form=loginform)


if __name__=="__main__":
    app.run(debug=True)