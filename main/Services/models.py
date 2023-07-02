from main.extensions import db
import datetime

class Services(db.Model):
    id=db.Column(db.BigInteger(),primary_key=True)
    subscriber_type=db.Column(db.String(200))
    client_name=db.Column(db.String(100))
    subscribed_service=db.Column(db.Integer())
    plan=db.Column(db.String(150))
    plan_amount=db.Column(db.Float(precision=32,decimal_return_scale=None))
    vendor=db.Column(db.String(100))
    subscribed_on=db.Column(db.DateTime(),server_default=db.func.now())
    next_renewal_date=db.Column(db.Date())
    remind_on=db.Column(db.Date())
    service_status=db.Column(db.Integer())
    plan_details=db.Column(db.String(250))
    comments=db.Column(db.String(200))
    created_by = db.Column(db.Integer)
    updated_by = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), server_default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime(timezone=True), server_default=db.func.now(), onupdate=db.func.now())


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
            "subscribed_on":""if self.subscribed_on is None else datetime.datetime.strftime(self.subscribed_on,"%Y-%m-%d") ,
            "next_renewal_date":"" if self.next_renewal_date is None else datetime.datetime.strftime(self.next_renewal_date,"%Y-%m-%d"),
            "remind_on":"" if self.remind_on is None else datetime.datetime.strftime(self.remind_on,"%Y-%m-%d"),
            "service_status":self.service_status,
            "plan_details":self.plan_details,
            "comments":self.comments,
            "created_by":self.created_by,
            "updated_by":self.updated_by,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }
        
    def update_service(self,detail):
        self.subcriber_type= detail.get("subscriber_type")
        self.client_name= detail.get("client_name")
        self.subscribed_service=detail.get("subscribed_service")
        if self.subscribed_service==None or self.subscribed_service=="":
            self.subscribed_service=None
        self.plan=detail.get("plan")
        self.plan_amount=detail.get("plan_amount")
        if self.plan_amount==None or self.plan_amount=="":
            self.plan_amount=None
        self.vendor=detail.get("vendor")
        self.subscribed_on=detail.get("subscribed_on")
        self.next_renewal_date=None if detail.get("next_renewal_date")=="" else detail.get("next_renewal_date")
        self.remind_on=None if detail.get("remind_on") =="" else detail.get("remind_on")
        self.service_status=detail.get("service_status")
        if self.service_status==None or self.service_status=="":
            self.service_status=None
        self.plan_details=detail.get("plan_details")
        self.comments=detail.get("comments")

        db.session.commit()
        return "updated successfully"
    
    def dropdown(self):
        return{
            "id":self.id,
            "client_name":self.client_name
        }
        
