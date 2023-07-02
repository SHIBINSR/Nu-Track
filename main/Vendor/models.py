from main.extensions import db
import json

class Vendor(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    vendor_name=db.Column(db.String(100))
    address=db.Column(db.String(100))
    website=db.Column(db.String(100))
    email=db.Column(db.String(100))
    phone=db.Column(db.BigInteger())
    logo=db.Column(db.String(255))
    contact_person=db.Column(db.BigInteger())
    designation=db.Column(db.String(100))
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())
    
    def __repr__(self):
        return f"<Vendor:{self.id}>"
    
    def to_json(self): 
        return{
            "id":self.id,
            "vendor_name":self.vendor_name,
            "address":self.address,
            "website":self.website,
            "email":self.email,
            "phone":self.phone,
            "logo":json.loads(self.logo),
            "contact_person":self.contact_person,
            "designation":self.designation,
            "created_by":self.created_by,
            "updated_by":self.updated_by,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
        
    def dorpdown(self):
        return{
            "id":self.id,
            "vendor":self.vendor_name
        }
        
    
