from sports.source.nba.nba_team import NBA_Team


class BrooklynNets(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Brooklyn Nets"
        self.name       = "Nets"
        self.team_id    = 1610612751