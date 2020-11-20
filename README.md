# Advent of beer

## Getting started

To find out the day assignment you need to run the `day_assignment.py`-script. This can be done by installing Python on your local machine, but it's oh so much more 2020 to use docker. Here's how:
- Download and install Docker Desktop ([Windows](http://https://hub.docker.com/editions/community/docker-ce-desktop-windows "Windows") | [Mac](https://docs.docker.com/docker-for-mac/install/ "Mac"))
- Download and install Git ([Windows](https://gitforwindows.org/ "Windows") | [Mac](https://git-scm.com/download/mac "Mac"))
- Create a directory to store the code, e.g. `c:\code`
- Open a terminal/powershell/cmd, cd to the directory you created and clone the repository using the command `git clone https://github.com/khc-data/advent-of-beer.git`
- Start an interactive Python docker instance based on the `python:slim` image with the directory you created mapped as a volume to allow the instance to access the code: `docker run -it -v C:\code\advent-of-beer:/var/code -w /var/code python:slim bash`
- Run the script: `python day_assignment.py`