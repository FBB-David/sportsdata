from sports.nba.nba_team import NBA_Team


class NewOrleansPelicans(NBA_Team):
    """
    NBA's New Orleans Pelicans Static Information

    """

    def __init__(self):
        """
        """
        super().__init__()
        self.full_name  = "New Orleans Pelicans"
        self.name       = "Pelicans"
        self.team_id    = 1610612740