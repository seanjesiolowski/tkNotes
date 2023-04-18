class FileHandler:
    def __init__(self):
        self.filename = 'tasks.txt'

    def save_note(self, note_text):
        with open(self.filename, 'a') as f:
            f.write(note_text + '\n')

    def read_all_notes(self):
        with open(self.filename, 'r') as f:
            file_lines = f.readlines()
        return file_lines
