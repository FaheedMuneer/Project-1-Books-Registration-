from flask import Flask, render_template, request
import psycopg2
try: 
    conn = psycopg2.connect(database="postgres", user="postgres",  
    password="Faheed8294", host="localhost")
    print("connected")
except:
    print ("I am unable to connect to the database")
mycursor =conn.cursor()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():
    # return render_template("registration.html")
    # success=None
    error=None
    # if request.method == "POST":
    uname = request.form.get('uname')
    # mail = request.form.get('mail')
    # passw = request.form.get('passw')
    # spwd=request.form.get('spwd')
    # if len(uname)<8:
    #     error="Username should not cross 8 characters"
    # elif len(passw!=spwd):
    #     error="Password does not matched.. Please try again"
    # elif len(passw)<7:
    #     error="Password must be have 7 characters"
    # else:
    #     success="Your account created successfully "" " + uname


        # return redirect(url_for("login"))
    return render_template("registration.html", msg=uname)
@app.route("/admin")
def admin():
    print("hi")
    mycursor.execute("SELECT * FROM Users")
    data = mycursor.fetchall()
    return render_template('admin.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
