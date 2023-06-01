from main.extensions import db

class Services(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    subscriber_type=db.Column(db.String(200),nullable=False)
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
    
    def to_json(self):
        return{
            "id":self.id,
            "subscriber_type":self.subscriber_type,
            "client_name":self.client_name,
            "subscribed_service":self.subscribed_service,
            "plan":self.plan,
            "plan_amount":self.plan_amount,
            "vendor":self.vendor,
            "subcribed_on":self.subscribed_on,
            "next_renewal_date":self.next_renewal_date,
            "remind_on":self.remind_on,
            "service_status":self.service_status,
            "plan_details":self.plan_details,
            "comments":self.comments
        }
        
