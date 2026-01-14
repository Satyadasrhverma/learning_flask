from flask import Flask, request, redirect, url_for, flash, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))

    def __init__(self, name, city, addr, pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin

@app.route('/')
def show_all():
    return render_template('show_all.html', students=Student.query.all())

@app.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
            flash("Please enter all fields")
            return redirect(url_for('new'))

        student = Student(
            request.form['name'],
            request.form['city'],
            request.form['addr'],
            request.form['pin']
        )

        db.session.add(student)
        db.session.commit()
        flash("Record added successfully")
        return redirect(url_for('show_all'))

    return render_template('new.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)



