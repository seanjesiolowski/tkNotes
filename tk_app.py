import tkinter as tk
from notes import Notes
from file import FileHandler


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        #  self.pencil = tk.BitmapImage(file='pencil.png')

        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent['bg'] = 'grey'
        self.parent.minsize(350, 350)
        self.parent.title('yet another note-taking app')

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
        new_note = Notes()
        new_note.write_to_note(entry_content)
        handle = FileHandler()
        handle.append_line(entry_content)
        self.render_notes(False)

    # render_notes is currently meant to make button widgets based on note objects in Notes.notes_list
    # only creates note objects on application launch
    def render_notes(self, is_from_file):
        #  on application launch
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
                note_button = tk.Button(self.parent, name=str(index))
                note_button['command'] = (lambda txt=note.note_content, idx=index: self.render_note_window(txt, idx))
                note_button['text'] = note.note_content
                note_button['bg'] = 'yellow'
                note_button.pack(padx=5, pady=5, ipadx=25, ipady=25)
                update_button = tk.Button(self.parent, command=lambda idx=index: self.update_note(idx))
                update_button['text'] = 'Edit'
                update_button['bg'] = 'blue'
                update_button.pack(padx=3, pady=3)
                hide_button = tk.Button(self.parent, command=lambda idx=index: self.hide_note(idx))
                hide_button['text'] = 'Hide'
                hide_button['bg'] = 'purple'
                hide_button.pack(padx=3, pady=3)

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
            handle.append_line(note.note_content)
        self.render_notes(False)

    def render_note_window(self, txt, idx):
        new_window = tk.Toplevel(self.parent)
        new_window.focus_set()
        new_window.geometry('600x600')

        my_textbox = tk.Text(new_window)
        my_textbox.insert(1.0, txt)
        my_textbox.focus_set()
        my_textbox.pack(padx=30, pady=30)

        del_btn = tk.Button(new_window, text='Delete')
        del_btn['command'] = (lambda index=idx: self.delete_individual_note(index))
        del_btn['bg'] = 'red'
        del_btn.pack()

    def delete_individual_note(self, index):
        Notes.delete_note_obj(index)
        self.render_notes(False)
        handle = FileHandler()
        handle.delete_lines()
        # probably need a method for this:
        for note in Notes.notes_list:
            handle.append_line(note.note_content)

        # or maybe a "refresh-notes-to-file" method
