
from sports.source.nba.nba_team import NBA_Team


class SanAntonioSpurs(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "San Antonio Spurs"
        self.name       = "Spurs"
        self.team_id    = 1610612759