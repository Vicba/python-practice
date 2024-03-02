class Musician:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"The musician {self.name}"

    def play(self) -> str:
        return f"{self.name} is playing music"
    

class Dancer:
    def __init__(self, name: str) -> None:
        self.name = name

    def __str__(self) -> str:
        return f"The dancer {self.name}"

    def dance(self) -> str:
        return f"{self.name} is dancing"