from flask import jsonify,Blueprint,request
from main.extensions import db
from main.Plans.models import Plans

plans=Blueprint("plans",__name__,url_prefix="/plans")

@plans.route("/create",methods=["POST"])
def add_plans():
    try:
        data=request.get_json()
        domain_name=data.get("domain_name")
        website=data.get("website")
        hosting=data.get("hosting")
        software=data.get("software")

        post=Plans(domain_name=domain_name,
                website=website,
                hosting=hosting,
                software=software)
        
        db.session.add(post)
        db.session.commit()

        return jsonify({
            "message":"data added successfully",
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

@plans.route("/")
def show_all_plans():
    try:
        page=request.args["page"]
        per_page=request.args['per_page']
        data=Plans.query.paginate(page=int(page),per_page=int(per_page),error_out=False)
        all_data=[]
        for i in data:
            id=i.id
            domain_name=i.domain_name
            website=i.website
            hosting=i.hosting
            software=i.software
            temp={
                "id":id,
                "domain_name":domain_name,
                "website":website,
                "hosting":hosting,
                "software":software
            }
            all_data.append(temp)
        return jsonify({
            "msg":"",
            "status":True,
            "data":all_data,
            "error":""
        }),200
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@plans.route("/edit/<int:id>",methods=["PUT"])
def edit_plan(id):
    try:
        data=request.get_json()
        domain_name=data.get("domain_name")
        website=data.get("website")
        hosting=data.get("hosting")
        software=data.get("software")

        edit=Plans.query.get(id)
        if edit is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "data":"",
                "error":""
            }),404
    
        edit.domain_name=domain_name
        edit.website=website
        edit.hosting=hosting
        edit.software=software
        
        db.session.commit()

        return jsonify({
            "message":"changes saved",
            "status":True,
            "data":"",
            "eror":""
        }),201
    except Exception as e:
        return jsonify({
            "msg":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

@plans.route("/delete/<int:id>",methods=["DELETE"])
def delete_plans(id):
    try:
        delete=Plans.query.get(id)
        if delete is None:
            return jsonify({
                "message":"data not found",
                "status":False
            })
        db.session.delete(delete)
        db.session.commit()
        return jsonify({
            "message":"data deleted successfully",
            "status":True
        })
    except Exception as e:
        return jsonify({
            "message":str(e),
            "status":False
        })

@plans.route("/<int:id>")
def show_by_id(id):
    try:
        data=Plans.query.get(id)
        if data is None:
            return jsonify({
                "message":"data not found",
                "status":False,
                "data":"",
                "error":""
            }),404
        demo=Plans.to_json(data)
        return jsonify({
            "msg":"",
            "data":demo,
            "status":True,
            "error":""
        }),201
    except Exception as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500
