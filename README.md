# Sistema de Ventas e Inventario (Tkinter FrameWork)

Sistema robusto de administración empresarial desarrollado en Python con interfaz gráfica moderna. Permite la gestión completa de inventarios, transacciones de compra/venta y generación de reportes profesionales.

## 🚀 Características Principales

### 🖥️ Interfaz Moderna (UI/UX)

- Diseño limpio y profesional ("Flat Design") con paleta de colores corporativa.
- **Dashboard Interactivo**: Visualización en tiempo real de stock crítico y accesos rápidos.
- Navegación intuitiva mediante barra de menú superior.

### 📦 Gestión de Inventario

- **CRUD Completo**: Administración de Categorías, Productos, Clientes y Proveedores.
- **Búsqueda en Tiempo Real**: Filtros instantáneos en todos los listados.
- **Integridad de Datos**: Validaciones inteligentes que impiden eliminar registros en uso.

### 💰 Transacciones y Facturación

- **Punto de Venta (POS)**: Generación ágil de facturas con validación automática de stock.
- **Órdenes de Compra**: Reabastecimiento de inventario integrado.
- **Anulación**: Sistema de reversión de transacciones (Facturas/Órdenes) con ajuste automático de stock.

### 📄 Reportes Profesionales

- Generación automática de **PDFs** con librería `fpdf`.
- Facturas detalladas con diseño corporativo.
- Listados exportables de transacciones.

## 🛠️ Tecnologías

- **Lenguaje**: Python 3.13+
- **GUI**: Tkinter + ttk (Themed Tkinter)
- **Reportes**: biblioteca `fpdf`
- **Persistencia**: Sistema de Archivos Planos (`.txt`)

## ⚙️ Instalación y Ejecución

1. **Requisitos Previos**:
   Asegúrese de tener Python instalado. Instale la dependencia de reportes:

   ```bash
   pip install fpdf
   ```

2. **Ejecutar la Aplicación**:
   Navegue a la carpeta del programa e inicie el script principal:

   ```bash
   cd programa
   python main.py
   ```

3. **Credenciales por Defecto**:
   - **Usuario**: `admin`
   - **Contraseña**: `admin`

## 📂 Estructura del Proyecto

```
.
├── documentacion/          # Manual de Usuario y Técnica
├── programa/
│   ├── data/               # Base de datos (archivos .txt)
│   ├── reportes/           # Salida de PDFs generados
│   ├── src/                # Código Fuente (Modelos, Vistas, Controladores)
│   └── main.py             # Punto de entrada
├── info.txt                # Metadatos del Curso
└── project-info.json       # Detalle del Proyecto
```

---
**Curso**: Taller de Programación | **Estudiante**: Geovanni Gonzalez Aguilar | **Año**: 2026
