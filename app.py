from flask import Flask , render_template


# an instance of the flaskclass
app=Flask(__name__)
app.secret_key='replacelater'


@app.route("/", methods=['GET','POST'])
def login():

    return render_template("login.html")


if __name__=="__main__":
    app.run(debug=True)