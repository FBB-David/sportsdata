from sports.source.nba.nba_team import NBA_Team


class UtahJazz(NBA_Team):
    """
    NBA's Washington Wizards Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Utah Jazz"
        self.name       = "Jazz"
        self.team_id    = 1610612762