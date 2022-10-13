
from ast import Delete
from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager,  create_access_token, get_current_user, get_jwt_identity, decode_token
from flask_bcrypt import Bcrypt

from database.database import session
from models.user import Users
# from models.products import Products

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = "asdjkfnçjk0789YJB87*&&*&OSDHFBOASDH%98(566DSFSIU"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 86400
jwt = JWTManager(app)

 
# ROTA DE REGISTRO
@app.route('/register', methods=['POST'])
def register():
    try:
        name = request.json.get('name')
        email = request.json.get('email')
        password = request.json.get('password')

        if not name:
            return 'Nome é Obrigatório', 400
        if not email:
            return 'Email é obrigatório', 400
        if not password:
            return 'Senha é obrigatório', 400
        if (session.query(Users).filter(Users.email == f"{email}").all()):
            return "Email já cadastrado!", 400

        hashed = bcrypt.generate_password_hash(f"{password}").decode('utf-8')

        user = Users(name=name, email=email, password=hashed)
        session.add(user)
        session.commit()

        access_token = create_access_token(identity={"email": email})
        return jsonify({"token": access_token}), 200
    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400

# ROTA DE LOGIN


@app.route('/login', methods=['POST'])
def login():
    try:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        if not email:
            return 'Email é obrigatório', 400
        if not password:
            return 'Senha é obrigatório', 400

        user = session.query(Users).filter(Users.email == f"{email}").first()
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
            ), 400

    except AttributeError:
        return 'Forneça EMAIL e SENHA no formato JSON no corpo da requisição (request.body)', 400

    # ROTA DE LOGOUT


@app.route('/logout', methods=['POST'])
def logout():
    try:
        token = request.json.get('token', None)
        if not token:
            return 'token é obrigatório', 400
        decode = decode_token(token)
        email = decode['sub']['email']
        print(email)
        user = session.query(Users).filter(Users.email == f"{email}").first()
        session.delete(user)
        session.commit()
        return "Conta deletada com sucesso", 200

    except AttributeError:
        return 'Forneça TOKEN no formato JSON no corpo da requisição (request.body)', 400

##############################################
# ROTAS DE PRODUTOS

# TODOS OS PRODUTOS


@app.route('/produtos')
def all_products():
    res = session.execute("SELECT * FROM products WHERE is_available = 'TRUE'")
    print(res)
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12],
                'quantity': 1
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
    res = session.execute(
        "SELECT * FROM products WHERE highlights = 'TRUE' AND is_available = 'TRUE'")
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12]
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
    res = session.execute(
        "SELECT * FROM products WHERE category = 'masculino' AND is_available = 'TRUE'")
    masc = list()
    for item in res:
        masc.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12]
            }
        )
    return make_response(
        jsonify(
            dados=masc
        )
    )

    # PRODUTOS FEMININOS


@app.route('/feminino')
def rota_feminino():
    res = session.execute(
        "SELECT * FROM products WHERE category = 'feminino' AND is_available = 'TRUE'")
    fem = list()
    for item in res:
        fem.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12]
            }
        )
    return make_response(
        jsonify(
            dados=fem
        )
    )

    # PRODUTOS CALCADOS


@app.route('/calcados')
def rota_calcados():
    res = session.execute(
        "SELECT * FROM products WHERE category = 'calcados' AND is_available = 'TRUE'")
    cal = list()
    for item in res:
        cal.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12]
            }
        )
    return make_response(
        jsonify(
            dados=cal
        )
    )

    # PRODUTOS ACESSORIOS


@app.route('/acessorios')
def rota_acessorios():
    res = session.execute(
        "SELECT * FROM products WHERE category = 'acessorios' AND is_available = 'TRUE'")
    ace = list()
    for item in res:
        ace.append(
            {
                'id': item[0],
                'category': item[1],
                'name': item[2],
                'price': item[3],
                'desc_price': item[4],
                'sku': item[5],
                'route': item[6],
                'alt_img': item[7],
                'img_main': item[8],
                'img_front': item[9],
                'img_right': item[10],
                'img_left': item[11],
                'img_back': item[12]
            }
        )
    return make_response(
        jsonify(
            dados=ace
        )
    )
