import tkinter as tk
from tkinter import ttk, messagebox
from .crud_frames import CategoriaFrame, ProductoFrame, ClienteFrame, ProveedorFrame
from .orders_window import OrdersWindow
from .billing_window import BillingWindow
from src.ui.theme import Theme
from src.repository import Repository
from src.models import Producto

class MainMenu:
    def __init__(self, root, user):
        self.root = root
        self.user = user
        Theme.apply_styles(root)
        
        # Configure MenuBar (Requirement 3.c)
        menubar = tk.Menu(root)
        root.config(menu=menubar)
        
        # Administración
        menu_admin = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Administración", menu=menu_admin)
        menu_admin.add_command(label="Categorías", command=lambda: self.show_module("Categorías", CategoriaFrame))
        menu_admin.add_command(label="Productos", command=lambda: self.show_module("Productos", ProductoFrame))
        menu_admin.add_command(label="Clientes", command=lambda: self.show_module("Clientes", ClienteFrame))
        menu_admin.add_command(label="Proveedores", command=lambda: self.show_module("Proveedores", ProveedorFrame))
        
        # Punto de Venta
        menu_pos = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Punto de Venta", menu=menu_pos)
        menu_pos.add_command(label="Facturación", command=self.open_billing)
        menu_pos.add_command(label="Orden de Compra", command=self.open_orders)
        menu_pos.add_separator()
        menu_pos.add_command(label="Búsqueda de Facturas", command=self.open_search_invoices)
        menu_pos.add_command(label="Búsqueda de Órdenes", command=self.open_search_orders)
        
        # Reports
        menu_rep = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Reportes", menu=menu_rep)
        menu_rep.add_command(label="Listado de Invoices", command=lambda: self.gen_report('INVOICES'))
        menu_rep.add_command(label="Listado de Órdenes", command=lambda: self.gen_report('ORDERS'))
        
        # Salir
        menubar.add_command(label="Salir", command=root.quit)
        
        # --- Dashboard Area ---
        self.container = ttk.Frame(root)
        self.container.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.show_dashboard()

    def show_dashboard(self):
        for widget in self.container.winfo_children():
            widget.destroy()
            
        ttk.Label(self.container, text=f"Bienvenido, {self.user.full_name}", style="H1.TLabel").pack(anchor='w', pady=20)
        
        stats_frame = ttk.Frame(self.container)
        stats_frame.pack(fill='x', pady=20)
        
        # Load Stats
        repo_prod = Repository("productos.txt")
        prods = repo_prod.load_all(Producto.from_string)
        total_prods = sum([p.cantidad for p in prods])
        low_stock = len([p for p in prods if p.cantidad < 5])
        
        self.create_stat_card(stats_frame, "Total Productos", f"{len(prods)}", "#3498db", 0)
        self.create_stat_card(stats_frame, "Unidades en Stock", f"{total_prods}", "#2ecc71", 1)
        self.create_stat_card(stats_frame, "Stock Bajo", f"{low_stock}", "#e74c3c", 2)
        
        # Actions
        act_frame = ttk.Frame(self.container)
        act_frame.pack(fill='x', pady=20)
        ttk.Label(act_frame, text="Accesos Rápidos", style="H2.TLabel").pack(anchor='w', pady=(0, 10))
        
        ttk.Button(act_frame, text="Nueva Venta", command=self.open_billing).pack(side='left', padx=10)
        ttk.Button(act_frame, text="Reabastecer (Orden)", command=self.open_orders).pack(side='left', padx=10)

    def create_stat_card(self, parent, title, value, color, col_idx):
        card = tk.Frame(parent, bg=color, padx=20, pady=20)
        card.grid(row=0, column=col_idx, padx=10, sticky='ew')
        parent.columnconfigure(col_idx, weight=1)
        
        tk.Label(card, text=value, font=("Segoe UI", 32, "bold"), fg="white", bg=color).pack()
        tk.Label(card, text=title, font=("Segoe UI", 12), fg="white", bg=color).pack()

    def show_module(self, title, frame_class):
        for widget in self.container.winfo_children():
            widget.destroy()
            
        header = tk.Frame(self.container, bg=Theme.BG_MAIN)
        header.pack(fill='x', pady=(0, 20))
        
        ttk.Label(header, text=title, style="H1.TLabel").pack(side='left')
        ttk.Button(header, text="Volver al Inicio", command=self.show_dashboard).pack(side='right')
        
        content = frame_class(self.container)
        content.pack(fill='both', expand=True)

    def open_orders(self):
        OrdersWindow(self.root)

    def open_billing(self):
        BillingWindow(self.root)
        
    def open_search_invoices(self):
        from src.ui.search_window import SearchTransactionsWindow
        SearchTransactionsWindow(self.root, mode="INVOICE")
        
    def open_search_orders(self):
        from src.ui.search_window import SearchTransactionsWindow
        SearchTransactionsWindow(self.root, mode="ORDER")

    def gen_report(self, rtype):
        try:
            from src.reports import PDFGenerator
            from src.repository import Repository
            from src.models import Factura, OrdenCompra
            
            # Generate Report (Standardized call remains same as reports.py inherits FPDF)
            # But wait, PDFGenerator INHERITS FPDF now. We must instantiate it.
            # The method signature for generate_list_report is `self.generate_list_report(...)`
            # Wait, PyFPDF usage: `pdf = PDFGen()`. 
            # My modified code in `src/report.py`: `class PDFGenerator(FPDF):`
            # and methods use `self.add_page()`.
            # So usage `gen = PDFGenerator()` is correct.
            
            gen = PDFGenerator()
            if rtype == 'INVOICES':
                repo = Repository("facturas.txt")
                items = repo.load_all(Factura.from_string)
                data = [[i.codigo, i.fecha, i.cliente_id, f"{i.total:.2f}"] for i in items]
                path = gen.generate_list_report("Reporte de Facturas", ["ID", "Fecha", "Cliente", "Total"], data, "Reporte_Facturas")
            else:
                repo = Repository("ordenes.txt")
                items = repo.load_all(OrdenCompra.from_string)
                data = [[i.codigo, i.fecha, i.proveedor_id, f"{i.total:.2f}"] for i in items]
                path = gen.generate_list_report("Reporte de Órdenes", ["ID", "Fecha", "Prov", "Total"], data, "Reporte_Ordenes")
            
            messagebox.showinfo("Éxito", f"Reporte generado en: {path}")
        except Exception as e:
            messagebox.showerror("Error", f"Fallo generando reporte: {e}")
