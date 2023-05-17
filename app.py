"""adopt application."""

from flask import Flask, render_template, request, redirect, session
from models import db, connect_db, Pet
from flask_sqlalchemy import SQLAlchemy
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adpot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

db.create_all()

@app.route('/')
def home():
    pets = Pet.query.all()
    return render_template("homelist.html", pets=pets)

@app.route("/add", methods=["GET", "POST"])
def add_snack():
    """Snack add form; handle adding."""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        return redirect("/add")

    else:
        return render_template(
            "petadd.html", form=form)