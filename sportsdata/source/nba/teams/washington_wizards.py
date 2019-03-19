from sportsdata.source.nba.team import NBA_Team


class WashingtonWizards(NBA_Team):
    """
    NBA Golden State Warriors Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "Washington Wizards"
        self.name       = "Wizards"
        self.team_id    = None
