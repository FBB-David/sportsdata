import requests
import logging

class NBA:

    base_url = "http://stats.nba.com/stats/{0}"
    headers = {
        'user-agent': (
            'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36'),# noqa: E501
            'Dnt': ('1'),
            'Accept-Encoding': ('gzip, deflate, sdch'),
            'Accept-Language': ('en'),
            'origin': ('http://stats.nba.com')
    }
    leagues =
    def allstarBallotPredictor(self):
        url = self.base_url.format("allstarballotpredictor")
        logging.debug(url)
        req = requests.get(url,headers=self.headers)
        print(req.text)

    def boxscoreadvancedv2(self):
        url = self.base_url.format("boxscoreadvancedv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscorefourfactorsv2(self):
        url = self.base_url.format("boxscorefourfactorsv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscoremiscv2(self):
        url = self.base_url.format("boxscoremiscv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscoreplayertrackv2(self):
        url = self.base_url.format("boxscoreplayertrackv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscorescoringv2(self):
        url = self.base_url.format("boxscorescoringv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscoresummaryv2(self):
        url = self.base_url.format("boxscoresummaryv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscoretraditionalv2(self):
        url = self.base_url.format("boxscoretraditionalv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def boxscoreusagev2(self):
        url = self.base_url.format("boxscoreusagev2")
        req = requests.get(url, headers=self.headers)

    def commonTeamYears(self):
        url = self.base_url.format("commonTeamYears")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def commonallplayers(self):
        url = self.base_url.format("commonallplayers")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def commonplayerinfo(self):
        url = self.base_url.format("commonplayerinfo")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def commonplayoffseries(self):
        url = self.base_url.format("commonplayoffseries")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def commonteamroster(self):
        url = self.base_url.format("commonteamroster")
        req = requests.get(url,headers=self.headers)
        print(req.text)

    def draftcombinedrillresults(self):
        url = self.base_url.format("draftcombinedrillresults")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinenonstationaryshooting(self):
        url = self.base_url.format("draftcombinenonstationaryshooting")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombineplayeranthro(self):
        url = self.base_url.format("draftcombineplayeranthro")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinespotshooting(self):
        url = self.base_url.format("draftcombinespotshooting")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def draftcombinestats(self):
        url = self.base_url.format("draftcombinestats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def drafthistory(self):
        url = self.base_url.format("drafthistory")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def franchisehistory(self):
        url = self.base_url.format("franchisehistory")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def homepageleaders(self):
        url = self.base_url.format("homepageleaders")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def homepagev2(self):
        url = self.base_url.format("homepagev2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaderstiles(self):
        url = self.base_url.format("leaderstiles")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashlineups(self):
        url = self.base_url.format("leaguedashlineups")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerbiostats(self):
        url = self.base_url.format("leaguedashplayerbiostats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerclutch(self):
        url = self.base_url.format("leaguedashplayerclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerptshot(self):
        url = self.base_url.format("leaguedashplayerptshot")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayershotlocations(self):
        url = self.base_url.format("leaguedashplayershotlocations")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashplayerstats(self):
        url = self.base_url.format("leaguedashplayerstats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashptdefend(self):
        url = self.base_url.format("leaguedashptdefend")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamclutch(self):
        url = self.base_url.format("leaguedashteamclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamptshot(self):
        url = self.base_url.format("leaguedashteamclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamshotlocations(self):
        url = self.base_url.format("leaguedashteamclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leaguedashteamstats(self):
        url = self.base_url.format("leaguedashteamstats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def leagueleaders(self):
        url = self.base_url.format("leaguedashteamstats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playByPlay(self):
        url = self.base_url.format("playbyplay")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playbyplayv2(self):
        url = self.base_url.format("playbyplayv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playercareerstats(self):
        url = self.base_url.format("playbyplayv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playercompare(self):
        url = self.base_url.format("playbyplayv2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyclutch(self):
        url = self.base_url.format("playerdashboardbyclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbygamesplits(self):
        url = self.base_url.format("playerdashboardbygamesplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbygeneralsplits(self):
        url = self.base_url.format("playerdashboardbygeneralsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbylastngames(self):
        url = self.base_url.format("playerdashboardbylastngames")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyopponent(self):
        url = self.base_url.format("playerdashboardbyopponent")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyshootingsplits(self):
        url = self.base_url.format("playerdashboardbyshootingsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyteamperformance(self):
        url = self.base_url.format("playerdashboardbyteamperformance")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashboardbyyearoveryear(self):
        url = self.base_url.format("playerdashboardbyyearoveryear")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptpass(self):
        url = self.base_url.format("playerdashptpass")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptreb(self):
        url = self.base_url.format("playerdashptreb")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptshotdefend(self):
        url = self.base_url.format("playerdashptshotdefend")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerdashptshots(self):
        url = self.base_url.format("playerdashptshots")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playergamelog(self):
        url = self.base_url.format("playergamelog")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerprofile(self):
        url = self.base_url.format("playerprofile")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playerprofilev2(self):
        url = self.base_url.format("playerprofilev2")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playersvsplayers(self):
        url = self.base_url.format("playersvsplayers")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playervsplayer(self):
        url = self.base_url.format("playervsplayer")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def playoffpicture(self):
        url = self.base_url.format("playoffpicture")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def scoreboard(self,game_date, leauge_id, day_offset):
        url = self.base_url.format("scoreboard")
        params = {'GameDate':game_date,'LeagueID':leauge_id,'DayOffset':day_offset}
        req = requests.get(url,headers=self.headers,params=params)
        print(req.text)

    def scoreboardv2(self,game_date, leauge_id, day_offset):
        url = self.base_url.format("scoreboardv2")
        params = {'GameDate':game_date,'LeagueID':leauge_id,'DayOffset':day_offset}
        req = requests.get(url,headers=self.headers,params=params)
        print(req.text)

    def shotchartdetail(self):
        url = self.base_url.format("shotchartdetail")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def shotchartlineupdetail(self):
        url = self.base_url.format("shotchartlineupdetail")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyclutch(self):
        url = self.base_url.format("teamdashboardbyclutch")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbygamesplits(self):
        url = self.base_url.format("teamdashboardbygamesplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbygeneralsplits(self):
        url = self.base_url.format("teamdashboardbygeneralsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbylastngames(self):
        url = self.base_url.format("teamdashboardbylastngames")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyopponent(self):
        url = self.base_url.format("teamdashboardbyopponent")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyshootingsplits(self):
        url = self.base_url.format("teamdashboardbyshootingsplits")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyteamperformance(self):
        url = self.base_url.format("teamdashboardbyteamperformance")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashboardbyyearoveryear(self):
        url = self.base_url.format("teamdashboardbyyearoveryear")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashlineups(self):
        url = self.base_url.format("teamdashlineups")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptpass(self):
        url = self.base_url.format("teamdashptpass")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptreb(self):
        url = self.base_url.format("teamdashptreb")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamdashptshots(self):
        url = self.base_url.format("teamdashptshots")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamgamelog(self):
        url = self.base_url.format("teamgamelog")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teaminfocommon(self):
        url = self.base_url.format("teaminfocommon")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamplayerdashboard(self):
        url = self.base_url.format("teamplayerdashboard")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamplayeronoffdetails(self):
        url = self.base_url.format("teamplayeronoffdetails")
        req = requests.get(url, headers=self.headers)
        print(req.text)


    def teamplayeronoffsummary(self):
        url = self.base_url.format("teamplayeronoffsummary")
        req = requests.get(url, headers=self.headers)
        print(req.text)


    def teamvsplayer(self):
        url = self.base_url.format("teamvsplayer")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def teamyearbyyearstats(self):
        url = self.base_url.format("teamyearbyyearstats")
        req = requests.get(url, headers=self.headers)
        print(req.text)

    def videoStatus(self):
        url = self.base_url.format("videoStatus")
        req = requests.get(url, headers=self.headers)
        print(req.text)