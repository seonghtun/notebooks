class NoteBook:
    def __init__(self, title) -> None:
        self.title: str = title
        self.page_number: int = 1
        self.notes: dict = {}

    def add_note(self, note, page=0):
        if self.page_number < 300:
            if page == 0:
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page: note}
                self.page_number += 1
        else:
            print("page가 다 채워졌습니다")

    def remove_note(self, page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("존재하지 않는 페이지 입니다.")

    def get_number_of_pages(self):
        return len(self.notes.keys())
