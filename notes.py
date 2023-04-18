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
