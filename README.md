# notesProject

## Current application 
- takes input string from user, then creates (in memory) and saves (to file) a list of notes
- allows each note to render as a button that hides itself when pressed (note (text) remains in file)
- at application launch, reads file "notes", assigning each note's text content to a unique and subsequently rendered note object
- allows user to edit/update the rendered note by inputting text in main entry and pressing note's "E" (for edit) button
- uses python (programming language), tkinter (user interface) and object-oriented programming (code structure)

### Todo
- *big picture: complete C.R.U.D. functionality and adequate styling/UI*
- refactor update-individual-note functionality
- refactor FileHandler class around class attribute for file
- refactor MainApplication class - i.e., render_notes and delete_notes methods
- switch ui geometry management from pack to grid 