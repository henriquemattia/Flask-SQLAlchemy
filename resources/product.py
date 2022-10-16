from models.products import ProductsModel
from flask_restful import Resource

class Products(Resource):
    def get(self):
        products = ProductsModel.find_products()
        return products
    
class Highlights(Resource):
    def get():
        products = ProductsModel.highlights_true()
        return products
    
    
class ProductsCategory(Resource):
    def get():
        products = ProductsModel.products_category()
        return products
    

