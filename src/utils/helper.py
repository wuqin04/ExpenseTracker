from enum import StrEnum

class Direction(StrEnum):
    LEFT        = "W"
    RIGHT       = "E"
    UP          = "N"
    DOWN        = "S"
    FILLED      = "NSEW"
    UP_LEFT     = "NW"
    UP_RIGHT    = "NE"
    DOWN_LEFT   = "SW"
    DOWN_RIGHT  = "SE"

def Debug(str):
    len_escape = 12 + len(str)
    for i in range(len_escape):
        print("-", end="")

    print(f"\n[Debugger]: {str}")

    for i in range(len_escape):
        print("-", end="")

    print()