from flask import Flask, jsonify, request,make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager,  create_access_token
from flask_bcrypt import Bcrypt

from database import  session
from user import Users
from products import Products, Imagens

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "asdjkfnçjk0789YJB87*&&*&OSDHFBOASDH%98(566DSFSIU"  
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        
        if not name:
            return 'Nome é Obrigatório',400
        if not email:
            return 'Email é obrigatório', 400
        if not password:
            return 'Senha é obrigatório', 400
        if(session.query(Users).filter(Users.email==f"{email}").all()):
            return "Email já cadastrado!", 400
        
        hashed = bcrypt.generate_password_hash(f"{password}").decode('utf-8')

        user = Users(name=name, email=email, password=hashed)
        session.add(user)
        session.commit()

        access_token = create_access_token(identity={"email": email})
        return jsonify({"access_token": access_token}), 200
    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        if not email:
            return 'Email é obrigatório', 400
        if not password:
            return 'Missing password', 400
        
        user = session.query(Users).filter(Users.email==f"{email}").first()
        if not user:
            return "nao passou", 404
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity={"email": email})
            return {"access_token": access_token}, 200
        else:
            return 'senha inválida', 404
        
    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400

@app.route('/teste')
def test():
    # ter = session.query(Products).join(Imagens).filter(Products.img_id==Imagens.id).all()
    ter = session.query(Products.img_id).join(Imagens, Products.img_id==Imagens.id).filter(Products.categoria=='masculino'), session.commit()
    print(ter)
    return 'boa', 200
    
