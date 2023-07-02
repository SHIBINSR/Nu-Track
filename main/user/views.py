from flask import jsonify,Blueprint,request
from main.user.models import User
from werkzeug.security import check_password_hash,generate_password_hash
from main.extensions import db

user=Blueprint("user",__name__,url_prefix="/user")

@user.route("/create-user",methods=["POST"])
def create_user():
    try:
        data=request.get_json()
        name=data.get("name")
        phone_number=data.get("phone_number")
        email=data.get("email")
        if User.query.filter_by(email=email).first():
            return jsonify({
                "message":"email already exists",
                "data":"",
                "status":False,
                "error":""
            }),201
        if User.query.filter_by(phone_number=phone_number).first():
            return jsonify({
                "message":"phone number already exists",
                "data":"",
                "status":False,
                "error":""
            }),201

        password=data.get("password")
        post=User(name=name,phone_number=phone_number,email=email,password=generate_password_hash(password))
        db.session.add(post)
        db.session.commit()
        return jsonify({
            "data":"",
            "status":True,
            "msg":"data added successfully",
            "error":""
        }),200
    except Exception as e:
        return jsonify({
            "data":"",
            "msg":"",
            "status":False,
            "error":str(e)
        }),500

@user.route("/login", methods=['POST'])
def loginAuthData():
    try:
        json_data = request.get_json()

        loginData = {
            "email": json_data.get("email"),
            "password": json_data.get("password")
        }
        authData = User.query.filter_by(email=loginData.get("email")).first()
        print(authData.password)
        if authData is None:
            #technical_log().warning({"status": False, "data": "", "msg": "Invalid user credential!!!"})
            return jsonify({"status": False, 
                            "data": "", 
                            "msg": "Invalid user credential!!!", 
                            "error":""}),200
        if not check_password_hash(authData.password, loginData.get("password")):
            #technical_log().warning({"status": False, "data": "", "msg": "Invalid password!!!"})
            return jsonify({"status": False, 
                            "data": "", 
                            "msg": "Invalid password!!!",
                            "error": ""}), 200
        return jsonify({"status": True,
                        "data":"",
                        "msg": "successfully logged-in",
                        "error": ""}), 201
    except Exception as e:
        #error_log().error({"status": False, "data": "", "msg": "", "error": str(e)})
        return jsonify({"status": False,
                        "data": "",
                        "msg": "",
                        "error": str(e)}), 500
    
@user.route("/update-user/<int:user_id>",methods=["PUT"])
def update_user(user_id):
    try:
        data=request.get_json()
        name=data.get("name")
        phone_number=data.get("phone_number")
        email=data.get("email")
        password=data.get("password")
        id_checking=User.query.get(user_id)
        if id_checking is None:
            return jsonify({
                "msg":"id not found",
                "data":"",
                "status":False,
                "error":""
            }),404
        id_checking.name=name
        id_checking.phone_number=phone_number
        id_checking.email=email
        id_checking.password=generate_password_hash(password) 
        db.session.commit()
        return jsonify({
            "data":"",
            "status":True,
            "msg":"data updated successfully",
            "error":""
        }),200
    except Exception as e:
        return jsonify({
            "data":"",
            "msg":"",
            "status":False,
            "error":str(e)
        }),500
    
@user.route("/get-all-user",methods=["GET"])
def get_user():
    try:
        data=User.query.all()
        total=[]
        for i in data:
            temp=User.to_json(i)
            total.append(temp)
        return jsonify({
            "data":total,
            "status":True,
            "error":"",
            "msg":""
        }),200
    except Exception as e:
        return jsonify({
            "data":"",
            "status":False,
            "error":str(e),
            "msg":""
        }),500
    
@user.route("/get-user/<int:user_id>",methods=["GET"])
def get_userid(user_id):
    try:
        id_checking=User.query.get(user_id)
        if id_checking is None:
            return jsonify({
                "msg":"id not found",
                "data":"",
                "error":"",
                "status":False
            }),404
        data=User.to_json(id_checking)
        return jsonify({
            "data":data,
            "error":"",
            "status":True,
            "msg":""
        }),201
    except Exception as e:
        return jsonify({
            "data":"",
            "error":str(e),
            "status":True,
            "msg":""
        }),500
    
@user.route("/delete-user/<int:user_id>",methods=["DELETE"])
def delete_user(user_id):
    try:
        id_checking=User.query.get(user_id)
        if id_checking is None:
            return jsonify({
                "msg":"id not found",
                "data":"",
                "error":"",
                "status":False
            }),404
        db.session.delete(id_checking)
        db.session.commit()
        return jsonify({
            "message":"deleted successfully",
            "status":True,
            "data":"",
            "error":""
        }),200
    except Exception  as e:
        return jsonify({
            "message":"",
            "status":False,
            "data":"",
            "error":str(e)
        }),500

