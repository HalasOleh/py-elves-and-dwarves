from .dwarf import Dwarf


class DwarfBlacksmith(Dwarf):
    def __init__(
        self, nickname: str,
        favorite_dish: str,
        skill_level: int
    ) -> None:
        super().__init__(nickname, favorite_dish)
        self._skill_level = skill_level

    def player_info(self) -> str:
        return (f"Dwarf blacksmith {self.nickname}"
                f" with skill of the {self._skill_level} level")

    def get_rating(self) -> int:
        return self._skill_level

