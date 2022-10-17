# from flask_restful import Resource, reqparse
# from flask_jwt_extended import create_access_token, jwt_required, get_jwt
# from blacklist import BLACKLIST
# from models.user import UsersModel


# arguments = reqparse.RequestParser()
# arguments.add_argument("name", type=str, required=True,
#                        help="Nome é obrigatório")
# arguments.add_argument("email", type=str, required=True,
#                        help="email é obrigatório")
# arguments.add_argument("password", type=str, required=True,
#                        help="password é obrigatório")


# class Users(Resource):

#     def get(self):
#         users = UsersModel.find_users()
#         return users


# class User(Resource):

#     def get(self, user_id):
#         user = UsersModel.find_user(user_id)

#         if user:
#             return user.json()
#         return {"message": "User not found"}, 404

#     def put(self, user_id):

#         data = arguments.parse_args()

#         user_found = UsersModel.find_user(user_id)

#         if user_found:
#             try:
#                 user_found.update_user(**data)
#                 user_found.save_user()
#             except:
#                 return {"message": "User not updated"}

#             return user_found.json(), 200

#     def delete(self, user_id):

#         user = UsersModel.find_user(user_id)

#         if user:
#             try:
#                 user.delete_user()
#             except:
#                 return {"message": "User not deleted"}, 500
#             return {"message": "User sussefl delete"}, 200
#         return {"message": "User not found"}, 404


# class UserRegister(Resource):

#     def post(self):

#         data = arguments.parse_args()
#         user = UsersModel(**data)

#         try:
#             user.hash_password(data["password"])
#             user.save_user()
#             access_token = create_access_token(identity=user.user_id)
#         except:
#             return {"message": "Internal server error"}, 500
#         # return (user.json(), access_token), 200
#         return {"token": access_token}, 200


# class Userlogin(Resource):

#     @classmethod
#     def post(cls):
#         arguments = reqparse.RequestParser()
#         arguments.add_argument(
#             "email", type=str, required=True, help="email é obrigatório")
#         arguments.add_argument("password", type=str,
#                                required=True, help="password é obrigatório")

#         data = arguments.parse_args()
#         user = UsersModel.find_user_email(data["email"])
#         if user:
#             access_token = create_access_token(identity=user.user_id)
#             return {"token": access_token}, 200


# class UserLogout(Resource):

#     @jwt_required()
#     def post(self):
#         jwt_id = get_jwt()["jti"]
#         BLACKLIST.add(jwt_id)
#         return {"message": "Log-out successfully"}, 200
