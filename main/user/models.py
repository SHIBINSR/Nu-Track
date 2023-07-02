from main.extensions import db

class User(db.Model):
    id=db.Column(db.BigInteger,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    phone_number=db.Column(db.BigInteger(),nullable=False,unique=True)
    email=db.Column(db.String(100),nullable=False,unique=True)
    password=db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    def __repr__(self):
        return f"<User:{self.id}>"
    
    def to_json(self):
        return{
            "id":self.id,
            "name":self.name,
            "phone":self.phone_number,
            "email":self.email,
            "password":self.password,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
