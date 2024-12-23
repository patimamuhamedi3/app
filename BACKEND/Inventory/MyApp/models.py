from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()



# Product Model
# class Product(request):
#     __tablename__ = 'products'
    
#     ProductID = Column(Integer, primary_key=True)
#     ProductName = Column(String(255), nullable=False)
#     Category = Column(String(255))
#     Price = Column(Float)
#     QuantityInStock = Column(Integer)
    
#     # Foreign Key to Supplier
#     SupplierID = Column(Integer, ForeignKey('suppliers.SupplierID'))
    
#     # Foreign Key to Warehouse
#     WarehouseID = Column(Integer, ForeignKey('warehouses.WarehouseID'))
    
#     # Relationships
#     supplier = relationship("Supplier", back_populates="products")
#     warehouse = relationship("Warehouse", back_populates="products")

# # Supplier Model
# class Supplier(Base):
#     __tablename__ = 'suppliers'
    
#     SupplierID = Column(Integer, primary_key=True)
#     SupplierName = Column(String(255), nullable=False)
#     ContactName = Column(String(255))
#     ContactPhone = Column(String(50))
#     Address = Column(String(255))
    
#     # Relationship with Product
#     products = relationship("Product", back_populates="supplier")

# # Warehouse Model
# class Warehouse(Base):
#     __tablename__ = 'warehouses'
    
#     WarehouseID = Column(Integer, primary_key=True)
#     WarehouseLocation = Column(String(255), nullable=False)
#     Capacity = Column(Integer)
#     ManagerName = Column(String(255))
    
#     # Relationship with Product
#     products = relationship("Product", back_populates="warehouse")

# # Order Model
# class Order(Base):
#     __tablename__ = 'orders'
    
#     OrderID = Column(Integer, primary_key=True)
#     OrderDate = Column(Date, nullable=False)
#     ShippingDate = Column(Date)
#     OrderStatus = Column(String(50))
#     TotalAmount = Column(Float)
    
#     # Foreign Key to Product
#     ProductID = Column(Integer, ForeignKey('products.ProductID'))
    
#     # Relationship with Product
#     product = relationship("Product")

# # Database Setup (Engine and Session)
# engine = create_engine('sqlite:///inventory.db', echo=True)

# Base.metadata.create_all(engine)
