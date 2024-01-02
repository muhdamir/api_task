class IdNotFound(Exception):
    def __init__(self, id_: int, *args: object) -> None:
        self.message = f"Data with id: {id_} is not found"
        super().__init__(*args)

    def __str__(self) -> str:
        return self.message
