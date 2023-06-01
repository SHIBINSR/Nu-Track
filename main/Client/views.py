from flask import Blueprint,request,jsonify
from main.Client.models import Client
from main.extensions import db

client=Blueprint("client",__name__,url_prefix="/client")

@client.route("/create",methods=["POST"])
def create_clients():
    try:
        data=request.get_json()
        company_name=data.get("company_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        company_logo=data.get("company_logo")
        contact_person=data.get("contact_person")
        designation=data.get("designation")
        
        post=Client(company_name=company_name,
                    address=address,
                    website=website,
                    email=email,
                    phone=phone,
                    company_logo=company_logo,
                    contact_person=contact_person,
                    designation=designation)
        
        db.session.add(post)
        db.session.commit()

        return jsonify({
            "message":"added successfully",
            "status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })

@client.route("/")
def show_all_client():
    try:
        page=request.args["page"]
        per_page=request.args["per_page"]
        data=Client.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            id=i.id
            company_name=i.company_name
            address=i.address
            website=i.website
            email=i.email
            phone=i.phone
            company_logo=i.company_logo
            contact_person=i.contact_person
            designation=i.designation

            temp={
                "id":id,
                "company_name":company_name,
                "address":address,
                "website":website,
                "email":email,
                "phone":phone,
                "company_logo":company_logo,
                "contact_person":contact_person,
                "designation":designation
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

@client.route("/edit/<int:id>",methods=["put"])
def edit_data(id):
    try:
        data=request.get_json()
        company_name=data.get("company_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        company_logo=data.get("company_logo")
        contact_person=data.get("contact_person")
        designation=data.get("designation")

        client_id=Client.query.get(id)
        if client_id is None:
            return jsonify({
                "message":"data not found",
                "status":False
            })

        client_id.company_name=company_name
        client_id.address=address
        client_id.website=website
        client_id.email=email
        client_id.phone=phone 
        client_id.company_logo=company_logo
        client_id.contact_person=contact_person
        client_id.designation=designation

        db.session.commit()

        return jsonify({
            "message":"edited done",
            "status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        })

@client.route("/delete/<int:id>",methods=["DELETE"])
def delete_data(id):
    try:
        data=Client.query.get(id)
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

@client.route("/<int:id>")
def get_by_id(id):
    try:
        data=Client.query.get(id)
        if data is None:
            return jsonify({
                "message":"id not found",
                "status":False
            })
        demo =Client.to_json(data)
        return jsonify({
            "staus":True,"data":demo
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        }) 