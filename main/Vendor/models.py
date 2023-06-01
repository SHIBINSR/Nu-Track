from main.extensions import db

class Vendor(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    vendor_name=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    website=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.BigInteger(),nullable=False)
    logo=db.Column(db.String(255),nullable=False)
    contact_person=db.Column(db.BigInteger(),nullable=False)
    designation=db.Column(db.String(100),nullable=False)
    
    def __repr__(self):
        return f"<userid:{self.id}>"
    
    def to_json(self):
        return{
            "id":self.id,
            "vendor_name":self.vendor_name,
            "address":self.address,
            "website":self.website,
            "email":self.email,
            "phone":self.phone,
            "logo":self.logo,
            "contact_person":self.contact_person,
            "designation":self.designation
        }
        
        
    
