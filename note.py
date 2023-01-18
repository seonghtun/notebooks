class Note:
    def __init__(self, content) -> None:
        self.content = content

    def remove_all(self) -> None:
        self.content = ""

    def __add__(self, other) -> None:
        self.content = self.content + other.content

    def __str__(self) -> str:
        return f'note content : {self.content}'
