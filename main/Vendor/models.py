from main.extensions import db

class Vendor(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    Vendor_name=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    website=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.BigInteger(),nullable=False)
    logo=db.Column(db.String(100),nullable=False)
    contact_person=db.Column(db.BigInteger(),nullable=False)
    designation=db.Column(db.String(100),nullable=False)
    
    def __repr__(self):
        return f"<userid:{self.id}>"