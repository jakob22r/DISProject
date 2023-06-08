from flask_bcrypt import Bcrypt

from project import app
if __name__ == '__main__':
    # from project import bcrypt
    # print(bcrypt.generate_password_hash("hej1234").decode('utf-8'))
    # print(bcrypt.generate_password_hash("kodeordet").decode('utf-8'))
    # print(bcrypt.generate_password_hash("sortKaffe").decode('utf-8'))
    # print(bcrypt.generate_password_hash("rødHvidRose").decode('utf-8'))
    # print(bcrypt.generate_password_hash("simpleMaskine").decode('utf-8'))
    # print(bcrypt.generate_password_hash("123estland").decode('utf-8'))
    # print(bcrypt.generate_password_hash("bedsteTA").decode('utf-8'))
    # print(bcrypt.generate_password_hash("musTændstik34").decode('utf-8'))
    # print(bcrypt.generate_password_hash("franskCanadier").decode('utf-8'))
    # print(bcrypt.generate_password_hash("mrEurovision").decode('utf-8'))
    # print(bcrypt.generate_password_hash("uis").decode('utf-8'))
    
    

    app.run(debug=True, host='127.0.0.1', port=5001)


