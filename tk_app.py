import tkinter as tk
import file
from notes import Notes


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent['bg'] = 'grey'

        self.my_label = tk.Label(self.parent, text='note/todo list', bg='grey')
        self.my_label.grid(row=0, columnspan=3)

        self.my_entry = tk.Entry(self.parent)
        self.my_entry.focus_set()
        self.my_entry.grid(row=1, column=0, columnspan=2)

        self.create_btn = tk.Button(self.parent, text='Create new', command=self.create_new_note)
        self.create_btn['bg'] = 'green'
        self.create_btn.grid(row=2, column=0)

        self.reveal_btn = tk.Button(self.parent, text='Unhide all', command=self.all_notes_visible)
        self.reveal_btn['bg'] = 'purple'
        self.reveal_btn.grid(row=2, column=1)

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
                new_frame = tk.Frame(self.parent)
                new_frame['bg'] = 'grey'
                new_frame.grid(rowspan=2, columnspan=3, pady=3)

                note_button = tk.Button(new_frame, name=str(index))
                note_button['command'] = (lambda txt=note.note_content, idx=index: self.make_note_window(txt, idx))
                note_button['text'] = note.note_content
                note_button['width'] = 16
                note_button['height'] = 7
                note_button['bg'] = 'yellow'
                note_button.grid(row=0, columnspan=2)

                hide_button = tk.Button(new_frame, command=lambda idx=index: self.hide_note_btn(idx))
                hide_button['text'] = 'Hide'
                hide_button['bg'] = 'purple'
                hide_button.grid(row=1, column=0, sticky='e')

                update_button = tk.Button(new_frame, command=lambda idx=index: self.update_note(idx))
                update_button['text'] = 'Update'
                update_button['bg'] = 'blue'
                update_button.grid(row=1, column=1, sticky='w')

    def all_notes_visible(self):
        for note in Notes.notes_list:
            note.visible = True
        self.refresh_note_btns(False)

    def make_note_window(self, txt, idx):
        new_window = tk.Toplevel(self.parent)

        my_frame = tk.Frame(new_window, bg='grey')
        my_frame.grid(columnspan=1, rowspan=2)

        my_textbox = tk.Text(my_frame)
        my_textbox.focus_set()
        my_textbox['width'] = 50
        my_textbox.insert('1.0', txt)
        my_textbox.grid(row=0)

        del_btn = tk.Button(my_frame, text='Delete')
        del_btn['command'] = (lambda index=idx: self.delete_individual(index))
        del_btn['bg'] = 'red'
        del_btn.grid(row=1)

    def delete_individual(self, index):
        Notes.delete_note_obj(index)
        file.refresh_file_notes()
        self.refresh_note_btns(False)
