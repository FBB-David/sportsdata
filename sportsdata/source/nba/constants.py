from enum import Enum


class PerMode(Enum):
    TOTALS      =   "Totals"
    PER_GAME    =   "PerGame"
    PER_36      =   "Per36"


class SeasonType(Enum):
    ALL_STAR        =   "All-Star"
    REGULAR_SEASON  =   "Regular Season"
    PRE_SEASON      =   "Pre Season"
    PLAYOFFS        =   "Playoffs"
