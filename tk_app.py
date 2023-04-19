import tkinter as tk
import file
from notes import Notes


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent['bg'] = 'grey'
        self.parent.minsize(350, 350)
        self.parent.title('yet another note-taking app')

        self.my_entry = tk.Entry(self.parent)
        self.my_entry.focus_set()
        self.my_entry.pack(padx=10, pady=10)

        self.create_btn = tk.Button(self.parent, text='Create note', command=self.create_new_note)
        self.create_btn['bg'] = 'green'
        self.create_btn.pack(padx=10, pady=10)

        self.reveal_btn = tk.Button(self.parent, text='All notes visible', command=self.all_notes_visible)
        self.reveal_btn['bg'] = 'purple'
        self.reveal_btn.pack(padx=15, pady=15)

        self.delete_button = tk.Button(self.parent, text='Delete all notes', command=self.delete_all)
        self.delete_button['bg'] = 'red'
        self.delete_button.pack(padx=15, pady=15)

    def create_new_note(self):
        entry_content = self.my_entry.get()
        new_note = Notes()
        new_note.write_to_note(entry_content)
        file.refresh_file_notes()
        self.refresh_note_btns(False)

    def wipe_btns(self):
        existing_button_widgets = self.parent.winfo_children()[5:]
        for widget in existing_button_widgets:
            widget.destroy()

    def update_note(self, idx):
        target_note = Notes.notes_list[idx]
        target_note.write_to_note(self.my_entry.get())
        file.refresh_file_notes()
        self.refresh_note_btns(False)

    def hide_note_btn(self, button_index):
        note_index = button_index
        Notes.notes_list[note_index].visible = False
        self.refresh_note_btns(False)

    def refresh_note_btns(self, is_on_launch):
        if is_on_launch:
            Notes.create_notes_from_file()
        else:
            self.wipe_btns()
        for index, note in enumerate(Notes.notes_list):
            if note.visible:
                note_button = tk.Button(self.parent, name=str(index))
                note_button['command'] = (lambda txt=note.note_content, idx=index: self.make_note_window(txt, idx))
                note_button['text'] = note.note_content
                note_button['bg'] = 'yellow'
                note_button.pack(padx=5, pady=5, ipadx=25, ipady=25)

                update_button = tk.Button(self.parent, command=lambda idx=index: self.update_note(idx))
                update_button['text'] = 'Update'
                update_button['bg'] = 'blue'
                update_button.pack(padx=3, pady=3)

                hide_button = tk.Button(self.parent, command=lambda idx=index: self.hide_note_btn(idx))
                hide_button['text'] = 'Hide'
                hide_button['bg'] = 'purple'
                hide_button.pack(padx=3, pady=3)

    def all_notes_visible(self):
        for note in Notes.notes_list:
            note.visible = True
        self.refresh_note_btns(False)

    def delete_all(self):
        file.delete_lines()
        Notes.delete_all_notes()
        self.refresh_note_btns(False)

    def make_note_window(self, txt, idx):
        new_window = tk.Toplevel(self.parent)
        new_window.focus_set()
        new_window.geometry('600x600')

        my_textbox = tk.Text(new_window)
        my_textbox.insert(1.0, txt)
        my_textbox.focus_set()
        my_textbox.pack(padx=30, pady=30)

        del_btn = tk.Button(new_window, text='Delete')
        del_btn['command'] = (lambda index=idx: self.delete_individual(index))
        del_btn['bg'] = 'red'
        del_btn.pack()

    def delete_individual(self, index):
        Notes.delete_note_obj(index)
        file.refresh_file_notes()
        self.refresh_note_btns(False)
