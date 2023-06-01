# Alias (#002)

from typing import TypeAlias, Literal

MiscMode: TypeAlias = Literal["aparar", "reduzir", "mmc", "mdc", "arred"]
Operate: TypeAlias = Literal["+", "-", "*", "/", "**", "*/"]
Number: TypeAlias = (int | float)