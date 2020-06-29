from app import db

class Algorithm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    algorithmName = db.Column(db.String(64), index=True, unique=True)
    exceString = db.Column(db.String(500))
    legit = db.Column(db.Boolean)

    def __repr__(self):
        return '<User {}>'.format(self.algorithmName)