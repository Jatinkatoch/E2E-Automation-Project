from database import db


class Product(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    name=db.Column(
        db.String(100)
    )

    category=db.Column(
        db.String(50)
    )

    price=db.Column(
        db.Float
    )

    image=db.Column(
        db.String(300)
    )

    description=db.Column(
        db.Text
    )

    rating=db.Column(
        db.Float
    )



class User(db.Model):

    id=db.Column(
        db.Integer,
        primary_key=True
    )

    name=db.Column(
        db.String(100)
    )

    email=db.Column(
        db.String(100),
        unique=True
    )

    password=db.Column(
        db.String(100)
    )