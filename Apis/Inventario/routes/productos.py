from fastapi import APIRouter ,Depends
from config.db import get_db
from models.models import producto
from schemas.inventario import CrearProducto , ActualizarProducto
from sqlalchemy.orm import Session

productos = APIRouter()


@productos.get("/inventario")
async def get_productos(db: Session = Depends(get_db)):
    return db.query(producto).all()

@productos.post("/crear")
async def insert_producto(product: CrearProducto , db: Session = Depends(get_db)):
    db_producto = producto(
        nombre = product.nombre,
        tipo = product.tipo,
        valorunitario = product.valorunitario,
        valorventa = product.valorventa,
        cantidadtotal = product.cantidadtotal
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)  # Refresh para obtener el id generado automáticamente

    return {"message": "Producto creado", "producto_id": db_producto.id_producto}

from fastapi import HTTPException

@productos.put("/actualizar/{producto_id}")
async def actualizar_producto(producto_id: int, product: ActualizarProducto, db: Session = Depends(get_db)):
    # Buscar el producto en la base de datos
    db_producto = db.query(producto).filter(producto.id_producto == producto_id).first()
    
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    # Actualizar los campos del producto
    if product.nombre is not None:
        db_producto.nombre = product.nombre
    if product.tipo is not None:
        db_producto.tipo = product.tipo
    if product.valorunitario is not None:
        db_producto.valorunitario = product.valorunitario
    if product.valorventa is not None:
        db_producto.valorventa = product.valorventa
    if product.cantidadtotal is not None:
        db_producto.cantidadtotal = product.cantidadtotal
    
    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(db_producto)  # Opcional: refrescar el objeto para obtener los valores actualizados

    return {"message": "Producto actualizado", "producto_id": db_producto.id_producto}


