from server import db

def save_exercise(self):
    db.session.add(self)
    db.session.commit()