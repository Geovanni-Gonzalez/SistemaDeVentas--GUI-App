import tkinter as tk
from tkinter import ttk

class Theme:
    # Colors
    BG_DARK = "#2c3e50"     # Midnight Blue
    BG_MAIN = "#ecf0f1"     # Clouds
    ACCENT = "#3498db"      # Peter River
    ACCENT_HOVER = "#2980b9"
    TEXT_LIGHT = "#ffffff"
    TEXT_DARK = "#2c3e50"
    SUCCESS = "#27ae60"     # Nephritis
    DANGER = "#e74c3c"      # Alizarin
    WARNING = "#f39c12"     # Orange

    FONT_H1 = ("Segoe UI", 24, "bold")
    FONT_H2 = ("Segoe UI", 16, "bold")
    FONT_BODY = ("Segoe UI", 11)
    FONT_BOLD = ("Segoe UI", 11, "bold")

    @staticmethod
    def apply_styles(root):
        style = ttk.Style(root)
        style.theme_use('clam') # Base theme to allow color customization

        # General Frame
        style.configure("TFrame", background=Theme.BG_MAIN)
        
        # Labels
        style.configure("TLabel", background=Theme.BG_MAIN, foreground=Theme.TEXT_DARK, font=Theme.FONT_BODY)
        style.configure("H1.TLabel", font=Theme.FONT_H1, foreground=Theme.ACCENT)
        style.configure("H2.TLabel", font=Theme.FONT_H2, foreground=Theme.BG_DARK)
        
        # Buttons (TButton)
        style.configure("TButton", 
                        font=Theme.FONT_BOLD, 
                        background=Theme.ACCENT, 
                        foreground=Theme.TEXT_LIGHT, 
                        borderwidth=0, 
                        focuscolor=Theme.ACCENT_HOVER,
                        padding=10)
        style.map("TButton", 
                  background=[('active', Theme.ACCENT_HOVER)],
                  foreground=[('active', Theme.TEXT_LIGHT)])
                  
        # Danger Button
        style.configure("Danger.TButton", background=Theme.DANGER)
        style.map("Danger.TButton", background=[('active', "#c0392b")])
        
        # Treeview
        style.configure("Treeview", 
                        background="white",
                        foreground=Theme.TEXT_DARK,
                        rowheight=30,
                        fieldbackground="white",
                        font=Theme.FONT_BODY)
        style.configure("Treeview.Heading", 
                        font=Theme.FONT_BOLD, 
                        background=Theme.BG_DARK, 
                        foreground=Theme.TEXT_LIGHT)
        style.map("Treeview", background=[('selected', Theme.ACCENT)])
        
        # Notebook
        style.configure("TNotebook", background=Theme.BG_MAIN, borderwidth=0)
        style.configure("TNotebook.Tab", 
                        font=Theme.FONT_BOLD, 
                        padding=[15, 5], 
                        background=Theme.BG_DARK, 
                        foreground="lightgray")
        style.map("TNotebook.Tab", 
                  background=[('selected', Theme.ACCENT)], 
                  foreground=[('selected', 'white')])

        # Entry
        style.configure("TEntry", fieldbackground="white", padding=5)

        root.configure(bg=Theme.BG_MAIN)
