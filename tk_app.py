import tkinter as tk
from notes import Notes


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # build app from here
        self.my_entry = tk.Entry(self.parent, width=5)
        self.my_entry.focus_set()
        self.my_entry.pack()

        self.my_button = tk.Button(self.parent, text='Create note', command=self.click_create_note)
        self.my_button.pack()

    def click_create_note(self):
        entry_content = self.my_entry.get()
        note_in_hand = Notes()
        note_in_hand.write_to_note(entry_content)
        self.render_notes()

    def render_notes(self):
        existing_label_widgets = self.parent.winfo_children()[3:]
        for widget in existing_label_widgets:
            widget.destroy()
        for note in Notes.notes_list:
            note_label = tk.Label(self.parent, text=note.note_content)
            note_label.pack()
