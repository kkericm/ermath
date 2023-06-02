# Alias (#002)

from typing import TypeAlias, Literal

MiscMode: TypeAlias = Literal["aparar", "reduzir", "mmc", "mdc", "arred"]
TrigonometryModes: TypeAlias = Literal["rad", "cos", "sin", "tan", "cot", "sec", "csc", ]
Operate: TypeAlias = Literal["+", "-", "*", "/", "**", "*/"]
Number: TypeAlias = (int | float)
Arrest: TypeAlias = Literal["top right", "top left", "bottom right", "bottom left"]