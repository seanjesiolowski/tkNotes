class Notes:
    notes_list = list()

    def __init__(self):
        self.note_content = ''
        self.blank = True
        self.visible = True
        Notes.notes_list.append(self)

    def write_to_note(self, the_content):
        self.note_content = the_content
        self.blank = False

    @classmethod
    def delete_note_obj(cls, index):
        Notes.notes_list.pop(index)

    @classmethod
    def edit_note_obj(cls, index, new_content):
        note_obj = Notes.notes_list[index]
        note_obj.note_content = new_content
