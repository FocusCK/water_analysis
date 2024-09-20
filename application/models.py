from app import db

class WaterTest(db.Model):
    # Water test results table
    id = db.Column(db.Integer, primary_key=True)
    ph = db.Column(db.Float)
    total_coliforms = db.Column(db.Integer)
    e_coli = db.Column(db.Integer)
    iron = db.Column(db.Float)
    manganese = db.Column(db.Float)
    nitrite = db.Column(db.Float)
    nitrate = db.Column(db.Float)
    arsenic = db.Column(db.Float)
    hardness = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return f'<WaterTest {self.id}>'


class Product(db.Model):
    # Products table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    category = db.Column(db.String(100))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Product {self.name}>'


class Recommendation(db.Model):
    # Add recommendations table
    id = db.Column(db.Integer, primary_key=True)
    test_parameter = db.Column(db.String(50))  # eg. pH, Iron, ect.
    min_value = db.Column(db.Float)
    max_value = db.Column(db.Float)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    product = db.relationship('Product')

    def __repr__(self):
        return f'<Recommendation {self.test_perameter}>'