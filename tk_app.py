import tkinter as tk
from notes import Notes
from file import FileHandler


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        #  self.pencil = tk.BitmapImage(file='pencil.png')

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent['bg'] = 'grey'

        self.my_entry = tk.Entry(self.parent)
        self.my_entry.focus_set()
        self.my_entry.pack(padx=10, pady=10)

        self.create_btn = tk.Button(self.parent, text='Create note', command=self.click_create_note)
        self.create_btn['bg'] = 'green'
        self.create_btn.pack(padx=10, pady=10)

        self.reveal_btn = tk.Button(self.parent, text='All notes visible', command=self.all_notes_visible)
        self.reveal_btn['bg'] = 'purple'
        self.reveal_btn.pack(padx=15, pady=15)

        self.delete_button = tk.Button(self.parent, text='Delete all notes', command=self.delete_notes)
        self.delete_button['bg'] = 'red'
        self.delete_button.pack(padx=15, pady=15)

    def click_create_note(self):
        entry_content = self.my_entry.get()
        note_in_hand = Notes()
        note_in_hand.write_to_note(entry_content)
        f_hand = FileHandler()
        f_hand.write_lines(entry_content)
        self.render_notes(False)

    def render_notes(self, is_from_file):
        if is_from_file:
            handle = FileHandler()
            for line_text in handle.read_lines():
                new_note_obj = Notes()
                new_note_obj.note_content = line_text.strip()
        else:
            existing_button_widgets = self.parent.winfo_children()[5:]
            for widget in existing_button_widgets:
                widget.destroy()
        for index, note in enumerate(Notes.notes_list):
            if note.visible:
                note_button = tk.Button(self.parent, name=str(index), command=lambda idx=index: self.hide_note(idx))
                note_button['text'] = note.note_content
                note_button['bg'] = 'yellow'
                note_button.pack(padx=5, pady=5, ipadx=25, ipady=25)
                update_button = tk.Button(self.parent, command=lambda idx=index: self.update_note(idx))
                update_button['text'] = 'E'  # for "Edit"
                update_button['bg'] = 'blue'
                update_button.pack(padx=3, pady=3)

    def hide_note(self, button_index):
        note_index = button_index
        Notes.notes_list[note_index].visible = False
        self.render_notes(False)

    def all_notes_visible(self):
        for note in Notes.notes_list:
            note.visible = True
        self.render_notes(False)

    def delete_notes(self):
        handle = FileHandler()
        handle.delete_lines()
        Notes.notes_list = []
        self.render_notes(False)

    def update_note(self, idx):
        target_note = Notes.notes_list[idx]
        target_note.write_to_note(self.my_entry.get())
        handle = FileHandler()
        handle.delete_lines()
        for note in Notes.notes_list:
            handle.write_lines(note.note_content)
        self.render_notes(False)
