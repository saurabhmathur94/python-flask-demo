from app import db


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    age = db.Column(db.Integer)
    address = db.Column(db.String(128), index=True)

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    @property
    def tojson(self):
        return {
            'name': self.name,
            'age': self.age,
            'address': self.address
        }

