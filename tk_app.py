import tkinter as tk
from notes import Notes
from file import FileHandler


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # build app from here
        self.my_entry = tk.Entry(self.parent)
        self.my_entry.focus_set()
        self.my_entry.pack()

        self.my_button = tk.Button(self.parent, text='Create note', command=self.click_create_note)
        self.my_button.pack()

    def click_create_note(self):
        entry_content = self.my_entry.get()
        note_in_hand = Notes()
        note_in_hand.write_to_note(entry_content)
        f_hand = FileHandler()
        f_hand.save_note(entry_content)
        self.render_notes(False)  # False -> is from memory, NOT from file

    def render_notes(self, is_from_file):
        if is_from_file:
            handle = FileHandler()
            for line_text in handle.read_all_notes():
                new_note_obj = Notes()
                new_note_obj.note_content = line_text.strip()
        else:
            existing_button_widgets = self.parent.winfo_children()[3:]
            for widget in existing_button_widgets:
                widget.destroy()
        for index, note in enumerate(Notes.notes_list):
            if note.visible:
                note_button = tk.Button(self.parent, name=str(index), command=lambda idx=index: self.hide_note(idx))
                note_button['text'] = note.note_content
                note_button['bg'] = 'yellow'
                note_button.pack()

    def hide_note(self, button_index):
        note_index = button_index
        Notes.notes_list[note_index].visible = False
        self.render_notes(False)
