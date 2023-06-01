from flask import Blueprint,request,jsonify
from main.Services.models import Services
from main.extensions import db

services=Blueprint("services",__name__,url_prefix="/services")

@services.route("/create",methods=["POST"])
def add_services_form():
    try:
        data=request.get_json()
        subscriber_type=data.get("subscriber_type")
        client_name=data.get("client_name")
        subscribed_service=data.get("subscribed_service")
        plan=data.get("plan")
        plan_amount=data.get("plan_amount")
        vendor=data.get("vendor")
        subscribed_on=data.get("subscribed_on")
        next_renewal_date=data.get("next_renewal_date")
        remind_on=data.get("remind_on")
        service_status=data.get("service_status")
        plan_details=data.get('plan_details')
        comments=data.get("comments")

        post=Services(subscriber_type=subscriber_type,
                      client_name=client_name,
                      subscribed_service=subscribed_service,
                      plan=plan,
                      plan_amount=plan_amount,
                      vendor=vendor,
                      subscribed_on=subscribed_on,
                      next_renewal_date=next_renewal_date,
                      remind_on=remind_on,
                      service_status=service_status,
                      plan_details=plan_details,
                      comments=comments)
        
        db.session.add(post)
        db.session.commit()
        return jsonify({
            "message":"created successfully",
            "Status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })

@services.route("/")
def display_all_services():
    try:
        page=request.args["page"]
        per_page=request.args["per_page"]
        data=Services.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            id=i.id
            subscriber_type=i.subscriber_type
            client_name=i.client_name
            subscribed_service=i.subscribed_service
            plan=i.plan
            plan_amount=i.plan_amount
            vendor=i.vendor
            subscribed_on=i.subscribed_on
            next_renewal_date=i.next_renewal_date
            remind_on=i.remind_on
            service_status=i.service_status
            plan_details=i.plan_details
            comments=i.comments

            temp={
                "id":id,
                "subscriber_type":subscriber_type,
                "client_name":client_name,
                "subscribed_service":subscribed_service,
                "plan":plan,
                "plan_amount":plan_amount,
                "vendor":vendor,
                "subscribed_on":subscribed_on,
                "next_renewal_date":next_renewal_date,
                "remind_on":remind_on,
                "service_status":service_status,
                "plan_details":plan_details,
                "comments":comments
            }
            all_data.append(temp)
        return jsonify({
            "datas":all_data,
            "Status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })

@services.route("/edit/<int:id>",methods=["put"])
def edit_data(id):
    try:
        data=request.get_json()
        subscriber_type=data.get("subscriber_type")
        client_name=data.get("client_name")
        subscribed_service=data.get("subscribed_service")
        plan=data.get("plan")
        plan_amount=data.get("plan_amount")
        vendor=data.get("vendor")
        subscribed_on=data.get("subscribed_on")
        next_renewal_date=data.get("next_renewal_date")
        remind_on=data.get("remind_on")
        service_status=data.get("service_status")
        plan_details=data.get('plan_details')
        comments=data.get("comments")

        service_id=Services.query.get(id)
        if service_id is None:
            return jsonify({
                "message":"data not found",
                "status":False
            })

        service_id.subcriber_type=subscriber_type
        service_id.client_name=client_name
        service_id.subscribed_service=subscribed_service
        service_id.plan=plan
        service_id.plan_amount=plan_amount
        service_id.vendor=vendor
        service_id.subscribed_on=subscribed_on
        service_id.next_renewal_date=next_renewal_date
        service_id.remind_on=remind_on
        service_id.service_status=service_status
        service_id.plan_details=plan_details
        service_id.comments=comments

        db.session.commit()

        return jsonify({
            "message":"edited done",
            "status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })

@services.route("/delete/<int:id>",methods=["DELETE"])
def delete_data(id):
    try:
        data=Services.query.get(id)
        if data is None:
            return jsonify({
                "message":"data not found",
                "status":False
            })
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            "message":"deleted successfully",
            "status":True
        })
    except Exception  as e:
        return jsonify({
            "message":str(e)
        })

@services.route("/<int:id>")
def get_by_id(id):
    try:
        data=Services.query.get(id)
        if data is None:
            return jsonify({
                "message":"id not found",
                "status":False
            })
        demo = Services.to_json(data)
        return jsonify({
            "staus":True,"data":demo
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })






