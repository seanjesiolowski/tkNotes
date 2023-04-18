class FileHandler:
    def __init__(self):
        self.filename = 'tasks.txt'

    def save_note(self, note_text):
        with open(self.filename, 'a') as f:
            f.write(note_text + '\n')
