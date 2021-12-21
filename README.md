# Advent of beer

## Getting started

To find out the day assignment you need to run the `day_assignment_yyyy.py`-script. This can be done by installing Python on your local machine, but it's oh so much more 2021 to use Docker. Here's how:
- Download and install Docker Desktop ([Windows](http://https://hub.docker.com/editions/community/docker-ce-desktop-windows "Windows") | [Mac](https://docs.docker.com/docker-for-mac/install/ "Mac"))
- Download and install Git ([Windows](https://gitforwindows.org/ "Windows") | [Mac](https://git-scm.com/download/mac "Mac"))
- Create a directory to store the code, e.g. `c:\code`
- Open a terminal/powershell/cmd, cd to the directory you created and clone the repository using the command `git clone https://github.com/khc-data/advent-of-beer.git`
- Start an interactive Python docker instance based on the `python:slim` image with the directory you created mapped as a volume to allow the instance to access the code: `docker run -it -v C:\code\advent-of-beer:/var/code -w /var/code python:slim bash`
- Run the script: `python day_assignment_yyyy.py`

## Results 2020

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
| 12 | Magnus | Stigberget Muddle IPA | [3.91](https://untappd.com/b/stigbergets-bryggeri-muddle/1905809) | [3.97](https://www.ratebeer.com/beer/stigbergets-muddle/479461/) |
| 13 | Johan | Samuel Adams Winter Lager | [3.43](https://untappd.com/b/boston-beer-company-samuel-adams-winter-lager/3919) | [3.21](https://www.ratebeer.com/beer/samuel-adams-winter-lager/168/) |
| 14 | Johan | Barrels And Drums Ginger Beer | [3.16](https://untappd.com/b/barrels-and-drums-ginger-beer/2679469) | N/A |
| 15 | Magnus | Omnipollo Noa Pecan Mud Cake Stout | [4.23](https://untappd.com/b/omnipollo-noa-pecan-mud-cake-stout/1046298) | [4.03](https://www.ratebeer.com/beer/omnipollo-noa-pecan-mud-cake-double-barrel/409868/) |
| 16 | Magnus | Omnipollo Fatamorgana | [4.00](https://untappd.com/b/omnipollo-fatamorgana/477842) | [3.80](https://untappd.com/b/omnipollo-fatamorgana/477842) |
| 17 | Johan | Innis & Gunn Blood Red Sky | [3.53](https://untappd.com/b/innis-and-gunn-blood-red-sky/2335869) | [3.42](https://www.ratebeer.com/beer/innis-and-gunn-blood-red-sky/561004/) |
| 18 | Magnus | Göteborg Christmas Session IPA | [2.99](https://untappd.com/b/goteborgs-nya-bryggeri-christmas-session-ipa/2364082) | [3.10](https://www.ratebeer.com/beer/goeteborgs-christmas-session-ipa/564296/) |
| 19 | Max | Stigbergets Trouble Sleep | [3.84](https://untappd.com/b/stigbergets-bryggeri-trouble-sleep/2809562) | [3.66](https://www.ratebeer.com/beer/stigbergets-trouble-sleep/658382/) |
| 20 | Johan | Abbaye D’aulne Christmas Triple Ale | [3.48](https://untappd.com/b/brasserie-de-l-abbaye-d-aulne-abbaye-d-aulne-christmas-triple-ale/4082926) | [3.75](https://www.ratebeer.com/beer/de-l-abbaye-d-aulne-biere-de-noel/878392/) |
| 21 | Magnus | Beerbliotek A Moment of Clarity | [3.63](https://untappd.com/b/beerbliotek-a-moment-of-clarity/1920392) | [3.74](https://www.ratebeer.com/beer/beerbliotek-a-moment-of-clarity/485750/) |
| 22 | Max | Stigbergets Bird in Hand Double IPA | [3.87](https://untappd.com/b/stigbergets-bryggeri-bird-in-hand/2866271) | [3.79](https://www.ratebeer.com/beer/stigbergets-bird-in-hand/670436/) |
| 23 | Max | Lagunitas Holiday Ale | [3.62](https://untappd.com/b/lagunitas-brewing-company-lagunitas-sucks-holiday-ale-2020/4036799) | [3.99](https://www.ratebeer.com/beer/lagunitas-sucks/158433/) |
| 24 | Johan | Nils Oscar God Lager | [3.28](https://untappd.com/b/nils-oscar-god-lager/7816) | [3.12](https://www.ratebeer.com/Ratings/Beer/Beer-Ratings.asp?BeerID=6135) |

## Results 2021

| Day | Responsible | Beer | Untappd score | Ratebeer score |
| --- | --- | --- | --- | --- |
| 1 | Max | All in brewing - Wheat seems to be the officer problem| [3.52](https://untappd.com/b/all-in-brewing-wheat-seems-to-be-the-officer-problem-citra-and-sabro/4385766)| [3.62](https://www.ratebeer.com/beer/all-in-brewing-stigbergets-wheat-seems-to-be-the-officer-problem-yellow-green/270492/) |
| 2 | Max | To Øl - DIPA | [3.88](https://untappd.com/b/to-ol-dipa/4028211) | [3.71](https://www.ratebeer.com/beer/to-ol-dipa/871943/) |
| 3 | Magnus | Rocket Brewing Company - Penitent | [3.32](https://untappd.com/b/rocket-brewing-company-penitent/4318476) | N/A |
| 4 | Johan | Sälens Fjällbryggeri - Fjälldimma | [3.49](https://untappd.com/b/salens-fjallbryggeri-fjalldimma/4185911) | [3.45](https://www.ratebeer.com/beer/saelens-fjaelldimma/919397/) |
| 5 | Magnus | Budweiser - Budvar B:DARK| [3.28](https://untappd.com/b/budejovicky-budvar-budweiser-budvar-b-dark-czechvar-b-dark/39819) | N/A |
| 6 | Max | Weihenstephaner - Hefeweissbier | [3.79](https://untappd.com/b/bayerische-staatsbrauerei-weihenstephan-weihenstephaner-hefeweissbier/8745) | [3.96](https://www.ratebeer.com/beer/weihenstephaner-hefeweissbier/1156/) |
| 7 | Magnus | Guiness - Draught | [3.77](https://untappd.com/b/guinness-guinness-draught/4473) | [3.56](https://www.ratebeer.com/beer/guinness-draught/1267/) |
| 8 | Johan | South Plains Brewing Company - Used Motor Oil | [3.47](https://untappd.com/b/south-plains-brewing-company-used-motor-oil/2001994) | [3.45](https://www.ratebeer.com/beer/south-plains-used-motor-oil/498477/) |
| 9 | Johan | Hönsinge Hantwerksbryggeri - Räntmästarens Röda | [3.29](https://untappd.com/b/honsinge-hantwerksbryggeri-rantmastarens-roda/696757) | [3.18](https://www.ratebeer.com/beer/hoensinge-raentmaestarens-roeda/323994/) |
| 10 | Magnus | Kaiserdom - Hefeweissbier | [3.19](https://untappd.com/b/privatbrauerei-kaiserdom-hefe-weissbier/15252) | [2.78](https://www.ratebeer.com/beer/kaiserdom-hefe-weissbier/117954/) |
| 11 | Max | Stigberget - Fraktur | [4.05](https://untappd.com/b/stigbergets-bryggeri-fraktur/4283581) | [3.80](https://www.ratebeer.com/beer/stigbergets-fraktur/926326/) |
| 12 | Johan | Sibbarps Husbryggeri - 79 | [3.38](https://untappd.com/b/sibbarps-husbryggeri-79/3985701) | [3.69](https://www.ratebeer.com/beer/sibbarps-79/865394/) |
| 13 | Max | Beerbliotek - Silly Season| [3.50](https://untappd.com/b/beerbliotek-silly-season/4555167) | [3.48](https://www.ratebeer.com/beer/beerbliotek-silly-season/966725/) |
| 14 | Max | Stockholm Brewing - Italopils Extra | [3.46](https://untappd.com/b/stockholm-brewing-co-italopils-extra/4228123) | [3.49](https://www.ratebeer.com/beer/stockholm-italopils-extra/919653/) |
| 15 | Magnus | Bira 91 - Summer Lager | [2.99](https://untappd.com/b/bira-91-bira-91-blonde/981756) | [2.14](https://www.ratebeer.com/brewers/cerana-beverages/22029/) |
| 16 | Magnus | St Peter's - Cream Stout | [3.61](https://untappd.com/b/st-peter-s-brewery-co-cream-stout/797) | [3.65](https://www.ratebeer.com/beer/st-peter-s-cream-stout-bottled/5301/) |
| 17 | Johan | Storpramen - Dark | [3.18](https://untappd.com/b/pivovary-staropramen-staropramen-dark-beer-cerny-lezak/130017) | [3.04](https://www.ratebeer.com/beer/staropramen-cerny-dark-temne/4791/) |
| 001 | Max | zzZnark - zzz001 | [3.39](https://untappd.com/b/zzz-zzznark-zzz001/4130698) | [3.13](https://www.ratebeer.com/beer/zzz001/892407/) |
| 008 | Max | zzZnark - zzz008 | [3.97](https://untappd.com/b/zzz-zzznark-zzz008/4223949) | [3.77](https://www.ratebeer.com/beer/zzz008/915315/) |
| 19 | Johan | Modelo - Negra | [3.29](https://untappd.com/b/grupo-modelo-modelo-negra/5852) | [2.79](https://www.ratebeer.com/beer/modelo-negra/745/) |
| 20 | Johan | Sibbarps - Festbier | [3.20](https://untappd.com/b/sibbarps-husbryggeri-festbier/1663726) | [3.15](https://www.ratebeer.com/beer/sibbarps-festbier/457934/) |
| 21 | Max | Duckpond Brewing - Topolino | [4.03](https://untappd.com/b/duckpond-brewing-topolino/3832316) | [3.54](https://www.ratebeer.com/beer/duckpond-topolino/853766/) |
| 22 | Magnus | | | |
| 23 | Magnus | | | |
| 24 | Johan | | | |