from main.extensions import db
import json

class Client(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    company_name=db.Column(db.String(100),nullable=False)
    address=db.Column(db.String(100),nullable=False)
    website=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(100),nullable=False)
    phone=db.Column(db.BigInteger(),nullable=False)
    company_logo=db.Column(db.String(255),nullable=False)
    contact_person=db.Column(db.BigInteger(),nullable=False)
    designation=db.Column(db.String(100),nullable=False)
    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    
    def __repr__(self):
        return f"<userid:{self.id}>"
    
    def to_json(self):
        return{
            "id":self.id,
            "company_name":self.company_name,
            "address":self.address,
            "website":self.website,
            "email":self.email,
            "phone":self.phone,
            "company_logo":json.loads(self.company_logo),
            "contact_person":self.contact_person,
            "designation":self.designation,
            "created_by":self.created_by,
            "updated_by":self.updated_by,
            "created_at":self.created_at,
            "updated_at":self.created_at
        }


