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

BALANCE_AMOUNT = 1000