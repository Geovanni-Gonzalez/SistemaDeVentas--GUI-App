import tkinter as tk
import os
from tkinter import ttk, messagebox
from src.repository import Repository
from src.models import Categoria, Producto, Cliente, Proveedor
from src.ui.theme import Theme

class GenericCrudFrame(ttk.Frame):
    def __init__(self, parent, model_class, filename, fields):
        super().__init__(parent)
        self.model_class = model_class
        self.repo = Repository(filename)
        self.fields = fields # List of (label, attrib_name)
        self.entries = {}
        self.model_name = model_class.__name__
        
        # 1. Top Bar: Search and Actions
        top_bar = ttk.Frame(self)
        top_bar.pack(side='top', fill='x', pady=10)
        
        ttk.Label(top_bar, text="Buscar:").pack(side='left')
        self.entry_search = ttk.Entry(top_bar)
        self.entry_search.pack(side='left', padx=5, fill='x', expand=True)
        ttk.Button(top_bar, text="Filtrar", command=self.perform_search).pack(side='left', padx=5)
        
        # 2. Form Area (Left or Top) - Let's use Sidebar
        main_content = ttk.Frame(self)
        main_content.pack(fill='both', expand=True)
        
        form_frame = ttk.LabelFrame(main_content, text="Detalle de Registro")
        form_frame.pack(side='left', fill='y', padx=10, ipadx=10, ipady=10)
        
        for i, (lbl, attr) in enumerate(fields):
            ttk.Label(form_frame, text=lbl).pack(anchor='w', pady=(10,0))
            entry = ttk.Entry(form_frame)
            if attr == 'codigo':
                entry.config(state='disabled') 
            entry.pack(fill='x', pady=2)
            self.entries[attr] = entry
            
        btn_frame = ttk.Frame(form_frame)
        btn_frame.pack(fill='x', pady=20)
        
        ttk.Button(btn_frame, text="Guardar", command=self.save_item).pack(fill='x', pady=2)
        ttk.Button(btn_frame, text="Limpiar", command=self.clear_form).pack(fill='x', pady=2)
        ttk.Button(btn_frame, text="Eliminar", style="Danger.TButton", command=self.delete_item).pack(fill='x', pady=2)
        
        # 3. Treeview Area
        tree_frame = ttk.Frame(main_content)
        tree_frame.pack(side='right', fill='both', expand=True)
        
        cols = [attr for _, attr in fields]
        self.tree = ttk.Treeview(tree_frame, columns=cols, show='headings')
        for lbl, attr in fields:
            self.tree.heading(attr, text=lbl)
            self.tree.column(attr, width=100)
            
        scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scroll.set)
        
        scroll.pack(side='right', fill='y')
        self.tree.pack(side='left', fill='both', expand=True)
        self.tree.bind("<<TreeviewSelect>>", self.on_select)
        
        self.refresh_list()

    def clear_form(self):
        for entry in self.entries.values():
            entry.config(state='normal')
            entry.delete(0, 'end')
        self.entries['codigo'].config(state='disabled')
        self.tree.selection_remove(self.tree.selection())

    def get_next_id(self, items):
        if not items: return 1
        return max([int(getattr(i, 'codigo')) for i in items]) + 1

    def refresh_list(self, filter_text=None):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        self.items = self.repo.load_all(self.model_class.from_string)
        
        for item in self.items:
            matches = True
            if filter_text:
                # Basic case-insensitive search in all fields
                matches = False
                for _, attr in self.fields:
                    val = str(getattr(item, attr)).lower()
                    if filter_text.lower() in val:
                        matches = True
                        break
            
            if matches:
                values = [getattr(item, attr) for _, attr in self.fields]
                self.tree.insert('', 'end', values=values)

    def perform_search(self):
        txt = self.entry_search.get()
        self.refresh_list(txt)

    def save_item(self):
        data = {}
        for _, attr in self.fields:
            if attr == 'codigo': continue
            data[attr] = self.entries[attr].get()

        selected = self.tree.selection()
        if selected:
            # Update
            cur_id = int(self.tree.item(selected[0], 'values')[0])
            for item in self.items:
                if int(item.codigo) == cur_id:
                     for k, v in data.items():
                         setattr(item, k, v)
                     break
            self.repo.save_all(self.items)
            messagebox.showinfo("Success", "Registro actualizado")
        else:
            # Create
            new_id = self.get_next_id(self.items)
            if self.model_class == Categoria:
                obj = Categoria(new_id, data['nombre'])
            elif self.model_class == Producto:
                 # Default Qty 0
                 obj = Producto(new_id, data['nombre'], data['categoria_id'], 0, data['precio'])
            elif self.model_class == Cliente:
                 obj = Cliente(new_id, data['nombre'], data['telefono'], data['correo'])
            elif self.model_class == Proveedor:
                 obj = Proveedor(new_id, data['nombre'], data['telefono'], data['correo'])
            
            self.repo.append(obj)
            messagebox.showinfo("Success", "Registro creado")

        self.clear_form()
        self.refresh_list()

    def delete_item(self):
        selected = self.tree.selection()
        if not selected: return
        
        cur_id = int(self.tree.item(selected[0], 'values')[0])
        
        # Validation Logic (Requirement: Constraints)
        if not self.validate_deletion(cur_id):
            return

        confirm = messagebox.askyesno("Confirmar", "¿Eliminar registro seleccionado?")
        if not confirm: return
        
        self.items = [i for i in self.items if int(i.codigo) != cur_id]
        self.repo.save_all(self.items)
        self.clear_form()
        self.refresh_list()

    def validate_deletion(self, _id):
        # Implement specific logic based on model
        if self.model_class == Categoria:
            # Check products
            repo_prod = Repository("productos.txt")
            prods = repo_prod.load_all(Producto.from_string)
            if any(p.categoria_id == _id for p in prods):
                messagebox.showerror("Error", "No se puede eliminar: Categoría tiene productos asociados.")
                return False
                
        elif self.model_class == Producto:
            # Check invoices
            # We need to scan Detail of Invoices. The text file is "detalle_factura.txt"
            # It has Format: fact_id; prod_id; qty; price
            repo_det = Repository("detalle_factura.txt")
            # We assume simple string loading to check ID presence for performance or map to DetalleFactura
            # Let's map it. We need imports. 
            # Fix path: data/detalle_factura.txt (assuming CWD is 'programa')
            if os.path.exists("data/detalle_factura.txt"):
                with open("data/detalle_factura.txt", "r") as f:
                    for line in f:
                        if f";{_id};" in line: # Quick check format
                            messagebox.showerror("Error", "No se puede eliminar: Producto ha sido facturado.")
                            return False
                        
        elif self.model_class == Cliente:
            # Check invoices (facturas.txt has client_id)
            if os.path.exists("data/facturas.txt"):
                with open("data/facturas.txt", "r") as f:
                    for line in f:
                        if f";{_id};" in line:
                             messagebox.showerror("Error", "No se puede eliminar: Cliente tiene facturas.")
                             return False

        elif self.model_class == Proveedor:
            # Check orders
            if os.path.exists("data/ordenes.txt"):
                with open("data/ordenes.txt", "r") as f:
                    for line in f:
                         if f";{_id};" in line:
                             messagebox.showerror("Error", "No se puede eliminar: Proveedor tiene órdenes de compra.")
                             return False
                         
        return True

    def on_select(self, event):
        selected = self.tree.selection()
        if not selected: return
        values = self.tree.item(selected[0], 'values')
        
        for i, (_, attr) in enumerate(self.fields):
            entry = self.entries[attr]
            entry.config(state='normal')
            entry.delete(0, 'end')
            entry.insert(0, values[i])
            if attr == 'codigo':
                entry.config(state='disabled')


class CategoriaFrame(GenericCrudFrame):
    def __init__(self, parent):
        super().__init__(parent, Categoria, "categorias.txt", [("Código", "codigo"), ("Nombre", "nombre")])

class ProductoFrame(GenericCrudFrame):
    def __init__(self, parent):
        super().__init__(parent, Producto, "productos.txt", [
            ("Código", "codigo"), 
            ("Nombre", "nombre"), 
            ("ID Categoría", "categoria_id"), 
            ("Precio Venta", "precio"),
            ("Stock", "cantidad")
        ])
        self.entries['cantidad'].config(state='disabled')

class ClienteFrame(GenericCrudFrame):
    def __init__(self, parent):
        super().__init__(parent, Cliente, "clientes.txt", [
            ("Código", "codigo"), 
            ("Nombre Completo", "nombre"),
            ("Teléfono", "telefono"),
            ("Correo", "correo")
        ])

class ProveedorFrame(GenericCrudFrame):
    def __init__(self, parent):
         super().__init__(parent, Proveedor, "proveedores.txt", [
            ("Código", "codigo"), 
            ("Nombre Completo", "nombre"),
            ("Teléfono", "telefono"),
            ("Correo", "correo")
        ])
