class FileHandler:
    def __init__(self):
        self.filename = 'tasks.txt'

    def append_line(self, note_text):
        with open(self.filename, 'a') as f:
            f.write(note_text + '\n')

    def read_lines(self):
        with open(self.filename, 'r') as f:
            file_lines = f.readlines()
        return file_lines

    def delete_lines(self):
        with open(self.filename, 'w') as f:
            f.write('')
