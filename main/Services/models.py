from main.extensions import db

class Services(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    subscriber_type=db.Column(db.Integer(),nullable=False,server_default="0")#0-individual,1-bussiness
    client_name=db.Column(db.String(100),nullable=False)
    subscribed_service=db.Column(db.Integer(),nullable=False)
    plan=db.Column(db.String(150),nullable=False)
    plan_amount=db.Column(db.Float(precision=32,decimal_return_scale=None),nullable=False)
    vendor=db.Column(db.String(100),nullable=False)
    subscribed_on=db.Column(db.DateTime(),server_default=db.func.now())
    next_renewal_date=db.Column(db.Date(),nullable=False)
    remind_on=db.Column(db.Date(),nullable=False)
    service_status=db.Column(db.Integer(),nullable=False)
    plan_details=db.Column(db.String(250),nullable=False)
    comments=db.Column(db.String(200))

    def __repr__(self):
        return f"<userid:{self.id}>"