import os 
from flask import current_app,request
from werkzeug.utils import secure_filename

def uploadDocuments(type=None, file=None, id=None):
    if file is None:
        return None

    if file.filename is None:
        return None
    if len(file.filename) == 0:
        return None

    file_type = {
        1: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/client/company_logo{id}/",
        2: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/vendor/vendor_logo{id}/",
    }
    filename = secure_filename(file.filename)
    root_path = current_app.root_path
    # print(current_app.)

    path = None
    if type == 1:
        path = os.path.join(root_path, file_type[1])
    if type == 2:
        path = os.path.join(root_path, file_type[2])
    try:
        os.makedirs(path)
    except FileExistsError:
        print("path already exist!!!")

    file.save(os.path.join(path, filename))

    return f"{request.root_url}{file_type[type]}{filename}"

def remove_files(type,id):
    file_type = {
        1: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/client/company_logo{id}/",
        2: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/vendor/vendor_logo{id}/",
        # 3: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Benefits_Of_Standards/standard{standard_id}/",
        # 4: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Abbreviation/standard{standard_id}/",
        # 5: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/QAndHelp/standard{standard_id}/",
        # 6: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/DiagramsLogo/standard{standard_id}/",
        # 7: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Implementation_CheckList/standard{standard_id}/",
        # 8: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/InternalAudit/standard{standard_id}/",
        # 9: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Miantenance/standard{standard_id}/",
        # 10: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/MasterListDocument/standard{standard_id}/",
        # 11: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/standard/{standard_id}/",
        # 12: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/CompanyLogo/",
        # 13: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/User/",
        # 14: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Security_Incident/standard{standard_id}/",
        # 15: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Training_Calender/standard{standard_id}/",
        # 16: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Vendor_Management/standard{standard_id}/",
        # 17: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/MOM/standard{standard_id}/",
        # 18: f"{current_app.config['UPLOAD_FOLDER']}/uploadImgAndDocument/Audit_schedule/standard{standard_id}/",
   
    }

    root_path = current_app.root_path

    path = None
    if type == 1:
        path = os.path.join(root_path, file_type[1])
    if type == 2:
        path = os.path.join(root_path, file_type[2])
    # if type == 3:
    #     path = os.path.join(root_path, file_type[3])
    # if type == 4:
    #     path = os.path.join(root_path, file_type[4])
    # if type == 5:
    #     path = os.path.join(root_path, file_type[5])
    # if type == 6:
    #     path = os.path.join(root_path, file_type[6])
    # if type == 7:
    #     path = os.path.join(root_path, file_type[7])
    # if type == 8:
    #     path = os.path.join(root_path, file_type[8])
    # if type == 9:
    #     path = os.path.join(root_path, file_type[9])
    # if type == 10:
    #     path = os.path.join(root_path, file_type[10])
    # if type == 11:
    #     path = os.path.join(root_path, file_type[11])
    # if type == 12:
    #     path = os.path.join(root_path, file_type[12])   
    # if type == 13:
    #     path = os.path.join(root_path, file_type[13])
    # if type == 14:
    #     path = os.path.join(root_path, file_type[14])
    # if type == 15:
    #     path = os.path.join(root_path, file_type[15])
    # if type == 16:
    #     path = os.path.join(root_path, file_type[16])
    # if type == 17:
    #     path = os.path.join(root_path, file_type[17])
    # if type == 18:
    #     path = os.path.join(root_path, file_type[18])

    if path:
        path = os.path.join(root_path, path.format(id))
        for old_file in os.listdir(path):
            print("old file",old_file)
            try:
                os.remove(os.path.join(path, old_file))
            except FileNotFoundError:
                print('not exist',old_file)
            except Exception as e:
                print("Error occurred:", str(e))
    return "Done"