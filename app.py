
from flask import Flask, jsonify, request,make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager,  create_access_token
from flask_bcrypt import Bcrypt

from database.database import  session
from models.user import Users

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "asdjkfnçjk0789YJB87*&&*&OSDHFBOASDH%98(566DSFSIU"  
jwt = JWTManager(app)


#ROTA DE REGISTRO
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
        return jsonify({"token": access_token}), 200
    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400

# ROTA DE LOG9IN
@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        if not email:
            return 'Email é obrigatório', 400
        if not password:
            return 'Senha é obrigatório', 400
        
        user = session.query(Users).filter(Users.email==f"{email}").first()
        if not user:
            return make_response(
                jsonify(
                    error="true",
                    message="Email inválido!"
            )
            ), 400
        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity={"email": email})
            return {"token": access_token}, 200
        else:
            return make_response(
                jsonify(
                    error="true",
                    message="Senha inválida"
            )
            ), 400 #parei aq2ui
        
    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400

##############################################
# ROTAS DE PRODUTOS



# TODOS OS PRODUTOS
@app.route('/produtos')
def all_prosucts():
    res =  session.execute("SELECT * FROM products p FULL OUTER JOIN images i ON p.img_id = i.id WHERE is_available = 'TRUE'")
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'price': item[3],
                'desc_preco': item[4],
                'SKU': item[5],
                'rota': item[6],
                'img_main': item[11],
                'img_front': item[12],
                'img_right': item[13],
                'img_left': item[14],
                'img_back': item[15]
                # ADICIONAR ALT para acessibilidade de imagens!
            }
        )
    return make_response(
        jsonify(
            dados=dest
        )
    )



# PRODUTOS EM DESTAQUE
    
@app.route('/destaque')
def destaques():
    res = session.execute("SELECT * FROM products p FULL OUTER JOIN images i ON p.img_id = i.id WHERE destaque = 'TRUE' and is_available = 'TRUE'")
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'price': item[3],
                'desc_preco': item[4],
                'SKU': item[5],
                'rota': item[6],
                'img_main': item[11],
                'img_front': item[12],
                'img_right': item[13],
                'img_left': item[14],
                'img_back': item[15]
            }
        )
    return make_response(
        jsonify(
            dados=dest
        )
    )
    
    #  PRODUTOS MASCULINO
@app.route('/masculino')
def rota_masculino():
    res = session.execute("SELECT * FROM products p FULL OUTER JOIN images i ON p.img_id = i.id WHERE categoria = 'masculino' and is_available = 'TRUE'")
    masc = list()
    for item in res:
        masc.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'price': item[3],
                'desc_preco': item[4],
                'SKU': item[5],
                'rota': item[6],
                'img_main': item[11],
                'img_front': item[12],
                'img_right': item[13],
                'img_left': item[14],
                'img_back': item[15]
            }
        )
    return make_response(
        jsonify(
            dados=masc
        )
    )