from application import app, db
from application.models import Products

@app.route('/add')
def add():
    new_product = Products(name="Throw Pillow")
    db.session.add(new_product)
    db.session.commit()
    return "Added new product to database"




