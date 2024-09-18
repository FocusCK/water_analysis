class WaterTest(db.Model):
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