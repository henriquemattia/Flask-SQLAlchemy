
from flask_jwt_extended import JWTManager
from flask import Flask, jsonify
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import os
from dotenv import load_dotenv
from blacklist import BLACKLIST
from flask_restful import Api

from resources.user import UserLogout, Userlogin, User, Users, UserRegister
from resources.product import Products, ProductsAcessorios, ProductsCalcado ,ProductsFeminino, ProductsMasculino, ProductsHighlights

load_dotenv()

app = Flask(__name__)
CORS(app)
api = Api(app)
bcrypt = Bcrypt(app)

app.config["JWT_SECRET_KEY"] = os.environ["SUPER_SECRET_KEY"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 86400
app.config["JWT_BLACKLIST_ENABLE"] = True

jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def verify_blacklist(self, token):
    return token["jti"] in BLACKLIST


@jwt.revoked_token_loader
def token_invalid(jwt_header, jwt_payload):
    return jsonify({"message": "log-out"})


@app.route('/')
def hello():
    return "<h1>hello meu world</h1>"

api.add_resource(User, "/user/<int:user_id>")
api.add_resource(Users, "/users")
api.add_resource(Userlogin, "/login")
api.add_resource(UserRegister, "/register")
api.add_resource(UserLogout, "/logout")

api.add_resource(Products, "/produtos")
api.add_resource(ProductsHighlights, "/destaque")
api.add_resource(ProductsMasculino, "/masculino")
api.add_resource(ProductsFeminino, "/feminino")
api.add_resource(ProductsCalcado, "/calcados")
api.add_resource(ProductsAcessorios, "/acessorios")

# if __name__ == "__main__":
#     app.run(debug=True, port=5000,)
