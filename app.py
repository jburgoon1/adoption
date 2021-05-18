from flask import Flask, request, render_template, redirect
from models import Pet, connect_db, db
from forms import addPetForm, editPetForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'adoptionapp'

connect_db(app)
db.create_all()
@app.route('/')
def show_home():
    pet = Pet.query.all()
    return render_template('home.html', pet = pet)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    form = addPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        available = form.available.data
        newpet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes, available= available)
        db.session.add(newpet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('new_pet_form.html', form = form )

@app.route('/<int:pet_id>/details')
def show_details(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    return render_template('pet_details.html', pet = pet)

@app.route('/<int:pet_id>/edit', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    pet = Pet.query.get_or_404(pet_id)
    form = editPetForm(obj = pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_form.html', form = form )

