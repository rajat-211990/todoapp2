import json
from flask import Blueprint, jsonify, render_template, request
from flask_login import  login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET','POST'])
@login_required
def home():
    if request.method == 'POST':
      note = request.form.get('note')  
      new_note = Note(data = note, user_id = current_user.id)
      db.session.add(new_note)
      db.session.commit()
    return render_template("home.html", user = current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    print(noteId)
    print(note)
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})