from notes import Notes

filename = 'tasks.txt'


def read_lines():
    with open(filename, 'r') as f:
        file_lines = f.readlines()
    return file_lines


def delete_lines():
    with open(filename, 'w') as f:
        f.write('')


def write_notes_as_lines():
    with open(filename, 'a') as f:
        for note in Notes.notes_list:
            f.write(note.note_content + '\n')


def refresh_file_notes():
    delete_lines()
    write_notes_as_lines()
