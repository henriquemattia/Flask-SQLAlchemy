from models.products import ProductsModel
from flask_restful import Resource


class Products(Resource):
    def get(self):
        products = ProductsModel.products_total()
        return products


class ProductsHighlights(Resource):
    def get(self):
        products = ProductsModel.products_highlights()
        return products


class ProductsMasculino(Resource):
    def get(self):
        products = ProductsModel.products_masculino()
        return products
    
    
class ProductsFeminino(Resource):
    def get(self):
        products = ProductsModel.products_feminino()
        return products

class ProductsCalcado(Resource):
    def get(self):
        products = ProductsModel.products_calcados()
        return products
    
class ProductsAcessorios(Resource):
    def get(self):
        products = ProductsModel.products_acessorios()
        return products
    
