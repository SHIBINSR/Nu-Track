from flask import Blueprint,request,jsonify,json
from main.Vendor.models import Vendor
from main.extensions import db
from werkzeug.datastructures import FileStorage
from main.utils import uploadDocuments,remove_files


vendor=Blueprint("vendor",__name__,url_prefix="/vendor")

@vendor.route("/create",methods=["POST"])
def create_vendor():
    try:
        #data=request.get_json()
        form_data=request.form
        data=json.loads(form_data.get("vendor"))
        attachment=request.files.getlist("attachment")
        if not attachment or attachment==[]:
            attachment=[FileStorage('','')]
        vendor_name=data.get("vendor_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone") if data.get("phone") else None
        logo=attachment
        contact_person=data.get("contact_person") if data.get("contact_person") else None
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
        for i in attachment:
            url=uploadDocuments(file=i,id=post.id,type=2)
            post.logo=json.dumps(url)
            db.session.commit()

        return jsonify({
            "message":"added successfully",
            "status":True,
            "data":"",
            "error":""
        }),200
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@vendor.route("/")
def show_all_vendor():
    try:
        page=request.args["page"]
        per_page=request.args["per_page"]
        data=Vendor.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            temp=Vendor.to_json(i)
            # id=i.id
            # vendor_name=i.vendor_name
            # address=i.address
            # website=i.website
            # email=i.email
            # phone=i.phone
            # logo=i.logo
            # contact_person=i.contact_person
            # designation=i.designation

            # temp={
            #     "id":id,
            #     "vendor_name":vendor_name,
            #     "address":address,
            #     "website":website,
            #     "email":email,
            #     "phone":phone,
            #     "logo":logo,
            #     "contact_person":contact_person,
            #     "designation":designation
            # }
            all_data.append(temp)
        return jsonify({
            "msg":"",
            "data":all_data,
            "Status":True,
            "error":""
        }),201
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@vendor.route("/edit/<int:id>",methods=["PUT"])
def edit_data(id):
    try:
        remove_file=remove_files(id=id,type=2)
        # data=request.get_json()
        form_data=request.form
        data=json.loads(form_data.get("vendor"))
        attachment=request.files.getlist("attachment")
        if not attachment or attachment == []:
            attachment = [FileStorage('', '')]

        vendor_name=data.get("vendor_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        if phone==None or phone=="":
            phone=None
        contact_person=data.get("contact_person")
        if contact_person==None or contact_person=="":
            contact_person=None
        designation=data.get("designation")

        vendor_id=Vendor.query.get(id)
        if vendor_id is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        for i in attachment:
            url=uploadDocuments(id=vendor_id.id,type=2,file=i)
            vendor_id.logo=json.dumps(url)

        vendor_id.vendor_name=vendor_name
        vendor_id.address=address
        vendor_id.website=website
        vendor_id.email=email
        vendor_id.phone=phone 
        vendor_id.contact_person=contact_person
        vendor_id.designation=designation

        db.session.commit()

        return jsonify({
            "message":"changes saved",
            "status":True,
            "data":"",
            "error":""
        }),201
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@vendor.route("/delete/<int:id>",methods=["DELETE"])
def delete_data(id):
    try:
        data=Vendor.query.get(id)
        if data is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            "message":"deleted successfully",
            "status":True,
            "data":"",
            "error":""
        }),201
    except Exception  as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@vendor.route("/<int:id>")
def get_by_id(id):
    try:
        data=Vendor.query.get(id)
        if data is None:
            return jsonify({
                "message":"id not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        demo =Vendor.to_json(data)
        return jsonify({
            "msg":"",
            "status":True,
            "data":demo,
            "error":""
        }),200
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500