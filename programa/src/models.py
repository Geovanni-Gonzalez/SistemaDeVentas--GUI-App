class BaseModel:
    def to_string(self):
        raise NotImplementedError

class Usuario:
    def __init__(self, username, password, full_name):
        self.username = username
        self.password = password
        self.full_name = full_name

    def to_string(self):
        return f"{self.username};{self.password};{self.full_name};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 3:
            return Usuario(parts[0], parts[1], parts[2])
        return None

class Categoria:
    def __init__(self, codigo, nombre):
        self.codigo = int(codigo)
        self.nombre = nombre

    def to_string(self):
        return f"{self.codigo};{self.nombre};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 2:
            return Categoria(parts[0], parts[1])
        return None

class Producto:
    def __init__(self, codigo, nombre, categoria_id, cantidad, precio):
        self.codigo = int(codigo)
        self.nombre = nombre
        self.categoria_id = int(categoria_id)
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def to_string(self):
        return f"{self.codigo};{self.nombre};{self.categoria_id};{self.cantidad};{self.precio};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 5:
            return Producto(parts[0], parts[1], parts[2], parts[3], parts[4])
        return None

class Cliente:
    def __init__(self, codigo, nombre, telefono, correo):
        self.codigo = int(codigo)
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def to_string(self):
        return f"{self.codigo};{self.nombre};{self.telefono};{self.correo};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return Cliente(parts[0], parts[1], parts[2], parts[3])
        return None

class Proveedor:
    def __init__(self, codigo, nombre, telefono, correo):
        self.codigo = int(codigo)
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

    def to_string(self):
        return f"{self.codigo};{self.nombre};{self.telefono};{self.correo};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return Proveedor(parts[0], parts[1], parts[2], parts[3])
        return None

class DetalleOrden:
    def __init__(self, orden_id, producto_id, cantidad, precio_unitario):
        self.orden_id = int(orden_id)
        self.producto_id = int(producto_id)
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    def to_string(self):
        return f"{self.orden_id};{self.producto_id};{self.cantidad};{self.precio_unitario};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return DetalleOrden(parts[0], parts[1], parts[2], parts[3])
        return None

class OrdenCompra:
    def __init__(self, codigo, proveedor_id, fecha, total):
        self.codigo = int(codigo)
        self.proveedor_id = int(proveedor_id)
        self.fecha = fecha
        self.total = float(total)

    def to_string(self):
        return f"{self.codigo};{self.proveedor_id};{self.fecha};{self.total};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return OrdenCompra(parts[0], parts[1], parts[2], parts[3])
        return None

class DetalleFactura:
    def __init__(self, factura_id, producto_id, cantidad, precio_unitario):
        self.factura_id = int(factura_id)
        self.producto_id = int(producto_id)
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)

    def to_string(self):
        return f"{self.factura_id};{self.producto_id};{self.cantidad};{self.precio_unitario};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return DetalleFactura(parts[0], parts[1], parts[2], parts[3])
        return None

class Factura:
    def __init__(self, codigo, cliente_id, fecha, total):
        self.codigo = int(codigo)
        self.cliente_id = int(cliente_id)
        self.fecha = fecha
        self.total = float(total)

    def to_string(self):
        return f"{self.codigo};{self.cliente_id};{self.fecha};{self.total};"

    @staticmethod
    def from_string(line):
        parts = line.split(';')
        if len(parts) >= 4:
            return Factura(parts[0], parts[1], parts[2], parts[3])
        return None
