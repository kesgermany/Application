from application import db, app
from application.models import Products

with app.app_context():
    db.drop_all()
    db.create_all()

    new_product = Products(name="Hug Me Throw Pillow")
    db.session.add(new_product)
    db.session.commit()

    new_product2 = Products(name="Mama Africa Wall Art")
    db.session.add(new_product2)
    db.session.commit()

    new_product3 = Products(name="A Little Cosy Set")
    db.session.add(new_product3)
    db.session.commit()

    new_product4 = Products(name="Chocolate Crunch Candle")
    db.session.add(new_product4)
    db.session.commit()

    new_product5 = Products(name="Lets Hang Coat Hanger")
    db.session.add(new_product5)
    db.session.commit()

    new_product6 = Products(name="World Atlas")
    db.session.add(new_product6)
    db.session.commit()