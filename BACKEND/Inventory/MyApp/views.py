from django.shortcuts import render

# Create your views here.
from flask import Flask, jsonify, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Product, Supplier, Warehouse, Order, Base
from serializers import ProductSchema, SupplierSchema, WarehouseSchema, OrderSchema

# Initialize Flask app
app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///inventory.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Ensure the database tables are created
Base.metadata.create_all(engine)

# Routes

# Product Routes
@app.route('/products', methods=['GET'])
def get_products():
    products = session.query(Product).all()
    product_schema = ProductSchema(many=True)
    return jsonify(product_schema.dump(products))

@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = session.query(Product).filter_by(ProductID=id).first()
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product_schema = ProductSchema()
    return jsonify(product_schema.dump(product))

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product_schema = ProductSchema()
    product = product_schema.load(data, session=session)
    session.add(product)
    session.commit()
    return jsonify(product_schema.dump(product)), 201

@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = session.query(Product).filter_by(ProductID=id).first()
    if not product:
        return jsonify({"error": "Product not found"}), 404
    data = request.json
    product_schema = ProductSchema()
    product = product_schema.load(data, instance=product, session=session)
    session.commit()
    return jsonify(product_schema.dump(product))

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = session.query(Product).filter_by(ProductID=id).first()
    if not product:
        return jsonify({"error": "Product not found"}), 404
    session.delete(product)
    session.commit()
    return jsonify({"message": "Product deleted"}), 200

# Similar routes can be added for Suppliers, Warehouses, and Orders

# Supplier Routes
@app.route('/suppliers', methods=['GET'])
def get_suppliers():
    suppliers = session.query(Supplier).all()
    supplier_schema = SupplierSchema(many=True)
    return jsonify(supplier_schema.dump(suppliers))

@app.route('/suppliers/<int:id>', methods=['GET'])
def get_supplier(id):
    supplier = session.query(Supplier).filter_by(SupplierID=id).first()
    if not supplier:
        return jsonify({"error": "Supplier not found"}), 404
    supplier_schema = SupplierSchema()
    return jsonify(supplier_schema.dump(supplier))

# Warehouse and Order routes can follow similar patterns.

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
