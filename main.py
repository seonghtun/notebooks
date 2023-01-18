from note import Note
from notebook import NoteBook

notebook = NoteBook("my pagenote")
new_note = Note("아 내목적의식은 뭘까")

notebook.add_note(new_note)
print(notebook.notes[1])
