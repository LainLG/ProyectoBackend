from config.db import Base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class producto(Base):
    __tablename__ = 'producto'
    __table_args__ = {'schema': 'inventario'}

    id_producto = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    tipo = Column(String)
    valorunitario = Column(Float)
    valorventa = Column(Float)    
    cantidadtotal = Column(Integer)  

    # Relaciones
    pedidos = relationship("pedidoproducto", back_populates="producto")
    mermas = relationship("productomerma", back_populates="producto")


class pedido(Base):
    __tablename__ = 'pedido'
    __table_args__ = {'schema': 'inventario'}

    id_pedido = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer)
    fecha = Column(DateTime)

    # Relación
    productos = relationship("pedidoproducto", back_populates="pedido")


class merma(Base):
    __tablename__ = 'merma'
    __table_args__ = {'schema': 'inventario'}

    id_merma = Column(Integer, primary_key=True, autoincrement=True)
    cantidad = Column(Integer)
    descripcion = Column(String)
    fecha = Column(DateTime)

    # Relación
    productos = relationship("productomerma", back_populates="merma")


class pedidoproducto(Base):
    __tablename__ = 'pedidoproducto'
    __table_args__ = {'schema': 'inventario'}

    pedido_id = Column(Integer, ForeignKey('inventario.pedido.id_pedido'), primary_key=True)
    producto_id = Column(Integer, ForeignKey('inventario.producto.id_producto'), primary_key=True)

    # Relaciones
    pedido = relationship("pedido", back_populates="productos")
    producto = relationship("producto", back_populates="pedidos")


class productomerma(Base):
    __tablename__ = 'productomerma'
    __table_args__ = {'schema': 'inventario'}

    producto_id = Column(Integer, ForeignKey('inventario.producto.id_producto'), primary_key=True)
    merma_id = Column(Integer, ForeignKey('inventario.merma.id_merma'), primary_key=True)

    # Relaciones
    producto = relationship("producto", back_populates="mermas")
    merma = relationship("merma", back_populates="productos")