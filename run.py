import tkinter as tk
from tk_app import MainApplication


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    app.pack(side="top", fill="both", expand=True)
    app.render_notes(True)
    root.mainloop()
