from sportsdata.source.nba.nba_team import NBA_Team


class WashingtonWizards(NBA_Team):
    """
    NBA's Washington Wizards Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Washington Wizards"
        self.name       = "Wizards"
        self.team_id    = 1610612764
