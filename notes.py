import file


class Notes:
    notes_list = list()

    def __init__(self):
        self.note_content = ''
        self.visible = True
        Notes.notes_list.append(self)

    def write_to_note(self, the_content):
        self.note_content = the_content

    @classmethod
    def update_note_obj(cls, index, new_content):
        note_obj = Notes.notes_list[index]
        note_obj.note_content = new_content

    @classmethod
    def delete_note_obj(cls, index):
        Notes.notes_list.pop(index)

    @classmethod
    def delete_all_notes(cls):
        Notes.notes_list = []

    @classmethod
    def create_notes_from_file(cls):
        for line_text in file.read_lines():
            new_note_obj = Notes()
            new_note_obj.note_content = line_text.strip()
