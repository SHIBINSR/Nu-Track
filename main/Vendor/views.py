from flask import Blueprint,request,jsonify
from main.Vendor.models import Vendor
from main.extensions import db

vendor=Blueprint("vendor",__name__,url_prefix="/vendor")

@vendor.route("/create",methods=["POST"])
def create_vendor():
    try:
        data=request.get_json()
        vendor_name=data.get("vendor_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        logo=data.get("logo")
        contact_person=data.get("contact_person")
        designation=data.get("designation")
        
        post=Vendor(vendor_name=vendor_name,
                    address=address,
                    website=website,
                    email=email,
                    phone=phone,
                    logo=logo,
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

@vendor.route("/")
def show_all_vendor():
    try:
        page=request.args["page"]
        per_page=request.args["per_page"]
        data=Vendor.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            id=i.id
            vendor_name=i.vendor_name
            address=i.address
            website=i.website
            email=i.email
            phone=i.phone
            logo=i.logo
            contact_person=i.contact_person
            designation=i.designation

            temp={
                "id":id,
                "vendor_name":vendor_name,
                "address":address,
                "website":website,
                "email":email,
                "phone":phone,
                "logo":logo,
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

@vendor.route("/edit/<int:id>",methods=["put"])
def edit_data(id):
    try:
        data=request.get_json()
        vendor_name=data.get("vendor_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        logo=data.get("logo")
        contact_person=data.get("contact_person")
        designation=data.get("designation")

        client_id=Vendor.query.get(id)
        if client_id is None:
            return jsonify({
                "message":"data not found",
                "status":False
            })

        client_id.vendor_name=vendor_name
        client_id.address=address
        client_id.website=website
        client_id.email=email
        client_id.phone=phone 
        client_id.logo=logo
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

@vendor.route("/delete/<int:id>",methods=["DELETE"])
def delete_data(id):
    try:
        data=Vendor.query.get(id)
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

@vendor.route("/<int:id>")
def get_by_id(id):
    try:
        data=Vendor.query.get(id)
        if data is None:
            return jsonify({
                "message":"id not found",
                "status":False
            })
        demo =Vendor.to_json(data)
        return jsonify({
            "staus":True,"data":demo
        })
    except Exception as e:
        return jsonify({
            "message":str(e)
        }) 