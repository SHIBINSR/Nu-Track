from main.extensions import db

class Plans(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    domain_name=db.Column(db.String(100),nullable=False)
    website=db.Column(db.String(100),nullable=False)
    hosting=db.Column(db.String(100),nullable=False)
    software=db.Column(db.String(100),nullable=False)
    created_by = db.Column(db.Integer, nullable=True)
    updated_by = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())

    
    def __repr__(self):
        return f"<userid:{self.id}>"
    
    def to_json(self):
        return {
            "id":self.id,
            "domain":self.domain_name,
            "website":self.website,
            "hosting":self.hosting,
            "software":self.software,
            "created_by":self.created_by,
            "updated_by":self.updated_by,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
