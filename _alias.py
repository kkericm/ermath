from typing import TypeAlias, Literal

MiscMode: TypeAlias = Literal["aparar", "reduzir", "mmc", "mdc"]
Operate: TypeAlias = Literal["+", "-", "*", "/", "**", "*/"]
Number: TypeAlias = (int | float)