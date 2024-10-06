CREATE SCHEMA Inventario;

CREATE TABLE Inventario.Producto(
    id_producto INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    tipo VARCHAR(40),
    valorUnitario REAL NOT NULL,
    valorVenta REAL NOT NULL,
    cantidadTotal INT

);

CREATE TABLE Inventario.Pedido(
    id_pedido INT PRIMARY KEY,
    cantidad INT NOT NULL,
    fecha DATE DEFAULT CURRENT_DATE   
);


CREATE TABLE Inventario.PedidoProducto(
    pedido_id INT,
    producto_id INT,
    PRIMARY KEY(pedido_id,producto_id),

    CONSTRAINT fk_pedido_id FOREIGN KEY (pedido_id) REFERENCES Inventario.Pedido(id_pedido),
    CONSTRAINT fk_producto_id FOREIGN KEY (producto_id) REFERENCES Inventario.Producto(id_producto) 
);

CREATE TABLE Inventario.Merma(
    id_merma INT PRIMARY KEY,
    cantidad INT NOT NULL,
    descripcion VARCHAR(255),
    fecha DATE DEFAULT CURRENT_DATE
);

CREATE TABLE Inventario.ProductoMerma(
    producto_id INT,
    merma_id INT,
    PRIMARY KEY(producto_id,merma_id),

    CONSTRAINT fk_producto_id FOREIGN KEY (producto_id) REFERENCES Inventario.Producto(id_producto),
    CONSTRAINT fk_merma_id FOREIGN KEY (merma_id) REFERENCES Inventario.Merma(id_merma)
);