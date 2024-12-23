from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import relationship

# Import models (assuming your models are in a module called `models.py`)
from models import Product, Supplier, Warehouse, Order


# Product Serializer
class ProductSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        load_instance = True  # To load data into SQLAlchemy instances

    # Define relationships (to serialize related objects)
    supplier = fields.Nested('SupplierSchema', many=False)
    warehouse = fields.Nested('WarehouseSchema', many=False)


# Supplier Serializer
class SupplierSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Supplier
        load_instance = True
    
    # Relationship
    products = fields.Nested(ProductSchema, many=True)


# Warehouse Serializer
class WarehouseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Warehouse
        load_instance = True

    # Relationship
    products = fields.Nested(ProductSchema, many=True)


# Order Serializer
class OrderSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Order
        load_instance = True

    # Relationship
    product = fields.Nested(ProductSchema, many=False)


# Example usage
if __name__ == "__main__":
    # Let's assume you have a session object with a query
    # from sqlalchemy.orm import sessionmaker
    # Session = sessionmaker(bind=engine)
    # session = Session()
    
    # Example: Querying a Product and serializing it
    product = session.query(Product).first()  # Just an example, you can modify this
    product_schema = ProductSchema()
    
    # Serialize
    result = product_schema.dump(product)
    print(result)
    
    # Example: Querying and serializing a Supplier
    supplier = session.query(Supplier).first()  # Just an example, you can modify this
    supplier_schema = SupplierSchema()
    
    # Serialize
    result = supplier_schema.dump(supplier)
    print(result)
