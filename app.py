from flask import Flask, jsonify, request
from flask_cors import CORS
import bcrypt
from flask_jwt_extended import JWTManager,  create_access_token


from config.database import  session
from models.user import Users

app = Flask(__name__)
CORS(app)
app.config["JWT_SECRET_KEY"] = "asdjkfnçjk0789YJB87*&&*&OSDHFBOASDH%98(566DSFSIU"  
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')
        
        if not name:
            return 'Nome é Obrigatório'
        if not email:
            return 'Email é obrigatório'
        if not password:
            return 'Senha é obrigatório'
        
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        user = Users(name=name, email=email, password=hashed)
        session.add(user)
        session.commit()

        access_token = create_access_token(identity={"email": email})
        return jsonify({"access_token": access_token})
    except AttributeError:
        return 'Provide an Email and Password in JSON format in the request body'


@app.route('/login', methods=['POST'])
def login():
        Email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not Email:
            return 'Email é obrigatório'
        if not password:
            return 'Missing password'
        
        user = session.query(Users).filter(Users.email=={Email})
        print(user)
        if not user:
            return "nao passou"

        if bcrypt.checkpw(password.encode('utf-8'), user.password):
            access_token = create_access_token(identity={"email": Email})
            return {"access_token": access_token}, 200
        else:
            return 'Login invalido', 400

