from flask import Blueprint,request,jsonify,json
from werkzeug.datastructures import FileStorage
from main.Client.models import Client
from main.extensions import db
from main.utils import uploadDocuments,remove_files

client=Blueprint("client",__name__,url_prefix="/client")

@client.route("/create",methods=["POST"])
def create_clients():
    try:
        #data=request.get_json()
        form_data=request.form
        data=json.loads(form_data.get("client"))
        attachment=request.files.getlist("attachment")
        if not attachment or attachment == []:
            attachment = [FileStorage('', '')]

        company_name=data.get("company_name")
        company_logo=attachment
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone") if data.get("phone") else None
        contact_person=data.get("contact_person") if data.get("contact_person") else None
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
        for i in attachment:
            url=uploadDocuments(file=i,id=post.id,type=1)
            post.company_logo=json.dumps(url)
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
            "error":str(e),
            "data":""
        }),500

@client.route("/")
def show_all_client():
    try:
        page=request.args["page"]
        per_page=request.args["per_page"]
        data=Client.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            temp=Client.to_json(i)
            # id=i.id
            # company_name=i.company_name
            # address=i.address
            # website=i.website
            # email=i.email
            # phone=i.phone
            # company_logo=i.company_logo
            # contact_person=i.contact_person
            # designation=i.designation

            # temp={
            #     "id":id,
            #     "company_name":company_name,
            #     "address":address,
            #     "website":website,
            #     "email":email,
            #     "phone":phone,
            #     "company_logo":company_logo,
            #     "contact_person":contact_person,
            #     "designation":designation
            # }
            all_data.append(temp)
        return jsonify({
            "data":all_data,
            "Status":True,
            "error":"",
            "msg":''
        }),200
    except Exception as e:
        return jsonify({
            "message":"",
            "data":"",
            "status":False,
            "error":str(e)
        }),500

@client.route("/edit/<int:id>",methods=["PUT"])
def edit_data(id):
    try:
        remove_file=remove_files(type=1,id=id)
        #data=request.get_json()
        form_data=request.form
        data=json.loads(form_data.get("client"))
        attachment=request.files.getlist("attachment")
        if not attachment or attachment == []:
            attachment = [FileStorage('', '')]

        company_name=data.get("company_name")
        address=data.get("address")
        website=data.get("website")
        email=data.get("email")
        phone=data.get("phone")
        if phone== None or phone=="":
            phone=None
        contact_person=data.get("contact_person")
        if contact_person==None or contact_person=="":
            contact_person=None
        designation=data.get("designation")

        client_id=Client.query.get(id)
        if client_id is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        for i in attachment:
            url=uploadDocuments(id=client_id.id,type=1,file=i)
            client_id.company_logo=json.dumps(url)
            

        client_id.company_name=company_name
        client_id.address=address
        client_id.website=website
        client_id.email=email
        client_id.phone=phone 
        client_id.contact_person=contact_person
        client_id.designation=designation

        db.session.commit()
        return jsonify({
            "message":"edited done",
            "status":True,
            "error":"",
            "data":""
        }),201
    except Exception as e:
        return jsonify({
            "error":str(e),
            "msg":"",
            "data":"",
            "status":False
        }),500

@client.route("/delete/<int:id>",methods=["DELETE"])
def delete_data(id):
    try:
        data=Client.query.get(id)
        if data is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "error":"",
                "data":""
            }),404
        db.session.delete(data)
        db.session.commit()
        return jsonify({
            "message":"deleted successfully",
            "status":True,
            "error":"",
            "data":""
        }),200
    except Exception  as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@client.route("/<int:id>")
def get_by_id(id):
    try:
        data=Client.query.get(id)
        if data is None:
            return jsonify({
                "message":"id not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        demo =Client.to_json(data)
        return jsonify({
            "msg":"",
            "staus":True,
            "data":demo,
            "error":""
        }),201
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500
    
@client.route("/drop-down",methods=["GET"])
def drop_down():
    try:
        all_data=[]
        data=Client.query.all()
        for i in data:
            temp=Client.dropdown(i)
            all_data.append(temp)
        return jsonify({
            "data":all_data,
            "error":"",
            "status":True,
            "msg":""
        }),201
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500