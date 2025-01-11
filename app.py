# from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///asep.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

# Define the database models
class Component(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

# @app.route("/")
# def home_page():
#     # components = Component.query.all()  # Fetch all components from the database
#     return render_template("index.html")

@app.route("/engine")
def engine_page():
    return render_template("engine.html")

@app.route("/brake")
def brake_page():
    return render_template("brake.html")

@app.route("/trans")
def transmission_page():
    return render_template("trans.html")

# @app.route("/query")
# def query_page():
#     return render_template("query.html")



if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)


#   <------------------------------------------>

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'backendrunner2@gmail.com'
app.config['MAIL_PASSWORD'] = 'Asepgroup@03'

db = SQLAlchemy(app)
mail = Mail(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flash('Signup successful!')
        return redirect(url_for('index'))
    return render_template('signup.html')

@app.route('/query', methods=['GET', 'POST'])
def issue():
    if request.method == 'POST':
        issue = request.form['issue']
        msg = Message('New Issue Submitted', sender='your_email@gmail.com', recipients=['business_email@example.com'])
        msg.body = f"Issue: {issue}"
        mail.send(msg)
        flash('Issue submitted successfully!')
        return redirect(url_for('index'))
    return render_template('query.html')

# if __name__ == '__main__':
#     app.run(debug=True)


