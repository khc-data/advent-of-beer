# Advent of beer

## Getting started

To find out the day assignment you need to run the `day_assignment.py`-script. This can be done by installing Python on your local machine, but it's oh so much more 2020 to use docker. Here's how:
- Download and install Docker Desktop ([Windows](http://https://hub.docker.com/editions/community/docker-ce-desktop-windows "Windows") | [Mac](https://docs.docker.com/docker-for-mac/install/ "Mac"))
- Download and install Git ([Windows](https://gitforwindows.org/ "Windows") | [Mac](https://git-scm.com/download/mac "Mac"))
- Create a directory to store the code, e.g. `c:\code`
- Open a terminal/powershell/cmd, cd to the directory you created and clone the repository using the command `git clone https://github.com/khc-data/advent-of-beer.git`
- Start an interactive Python docker instance based on the `python:slim` image with the directory you created mapped as a volume to allow the instance to access the code: `docker run -it -v C:\code\advent-of-beer:/var/code -w /var/code python:slim bash`
- Run the script: `python day_assignment.py`

## Results

| Day | Responsible | Beer | Untappd score | Ratebeer score |
| --- | --- | --- | --- | --- |
| 1 | Max | Weihenstephaner Hefe Weissbier | [3.80](https://untappd.com/b/bayerische-staatsbrauerei-weihenstephan-weihenstephaner-hefeweissbier/8745) | [3.96](https://www.ratebeer.com/beer/weihenstephaner-hefeweissbier/1156/) |
| 2 | Max | Bernard Bohemian Winter Ale | [π](https://untappd.com/b/bernard-family-brewery-bohemian-winter-ale/1294417) | [3.26](https://www.ratebeer.com/beer/bernard-bohemian-ale-16/279996/) |
| 3 | Johan | Norrlands Guld Export | [2.76](https://untappd.com/b/spendrups-bryggeri-norrlands-guld-export/8267) | [2.12](https://www.ratebeer.com/Ratings/Beer/Beer-Ratings.asp?BeerID=9671) |
| 4 | Magnus | Stranger than Fiction | [3.72](https://untappd.com/b/collective-arts-brewing-stranger-than-fiction/1009922) | [3.68](https://www.ratebeer.com/Ratings/Beer/Beer-Ratings.asp?BeerID=325758) |
| 5 | Max | Oppigård Winter Ale | [3.45](https://untappd.com/b/oppigards-bryggeri-winter-ale/12168) | [3.42](https://www.ratebeer.com/beer/oppigards-winter-ale/39203/) |
| 6 | Max | Bernard Celebration Lager | [3.32](https://untappd.com/b/bernard-family-brewery-celebration-lager-svatecni-lezak/14628) | [3.22](https://www.ratebeer.com/beer/bernard-svatecni-lezak-12-celebration-lager-12/26766/) |
| 7 | Magnus | Purity Pure Gold | [3.31](https://untappd.com/b/purity-brewing-co-england-pure-gold/6445) | [3.23](https://www.ratebeer.com/beer/purity-pure-gold/54329/) |
| 8 | Max | Hibernation Ale | [3.65](https://untappd.com/b/great-divide-brewing-company-hibernation-ale/414) | [3.74](https://www.ratebeer.com/beer/great-divide-hibernation-ale/1653/) |
| 9 | Johan | Störtebeker Bernstein-Weizen | [3.42](https://untappd.com/b/stortebeker-braumanufaktur-bernstein-weizen/29780) | [3.20](https://www.ratebeer.com/beer/stoertebeker-bernstein-weizen/39881/) |
| 10 | Magnus | Rocket The King In Yellow | [3.32](https://untappd.com/b/rocket-brewing-company-the-king-in-yellow/3161442) | [2.93](https://www.ratebeer.com/beer/rocket-the-king-in-yellow/754185/) |
| 11 | Johan | Falcon Julbrygd | [2.93](https://untappd.com/b/carlsberg-sverige-falcon-julbrygd/97541) | [2.66](https://www.ratebeer.com/beer/falcon-juloel-julbrygd/19971/) |
| 12 | Magnus | | | |
| 13 | Johan | | | |
| 14 | Johan | | | |
| 15 | Magnus | | | |
| 16 | Magnus | | | |
| 17 | Johan | | | |
| 18 | Magnus | | | |
| 19 | Max | | | |
| 20 | Johan | | | |
| 21 | Magnus | | | |
| 22 | Max | | | |
| 23 | Max | | | |
| 24 | Johan | | | |
