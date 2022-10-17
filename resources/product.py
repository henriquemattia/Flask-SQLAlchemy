from models.products import ProductsModel
from flask_restful import Resource


class Products(Resource):
    def get(self):
        products = ProductsModel.find_products()
        return products


class Highlights(Resource):
    def get(self):
        products = ProductsModel.highlights_true()
        return products


class ProductsMasculino(Resource):
    def get(self):
        products = ProductsModel.products_masculino(self)
        return products
