class RoutineFailure(RuntimeError):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Routine:
    def __init__(self, id: str) -> None:
        self.id = id
    def run(self) -> bool:
        return True
    