class user(db.Model):
    id=db.Column(db.Int,Primary_Key=True)
    email=db.Column(db.String(1000),unique=True)
    phone=db.Column(db.Int(50),unique=True)
    credits=db.Column(db.Int(50))
