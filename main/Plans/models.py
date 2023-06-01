from main.extensions import db

class Plans(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    domain_name=db.Column(db.String(100),nullable=False)
    website=db.Column(db.String(100),nullable=False)
    hosting=db.Column(db.String(100),nullable=False)
    software=db.Column(db.String(100),nullable=False)
    
    def __repr__(self):
        return f"<userid:{self.id}>"
    
    def to_json(self):
        return {
            "id":self.id,
            "domain":self.domain_name,
            "website":self.website,
            "hosting":self.hosting,
            "software":self.software
        }
