# Git repository Finder

## What does the Code do?
The code contained within this small repository is responsible for going through all the folder specified by the user and gathering a list of git repositories. After which it will go through all these repositories and add a new remote specified by the user at the beginning. It will then upload the repositories to the new remote. 

## Motivation
The reason I created this script was that the projects i developed at University were held on a GitLab instance hosted by the university. When I left i no longer had acess to the remote repositories. So I created my own instance and ran this script to put all my old repositories on it.


## How to Run
Simply run the "main.py" file and input the domain of your remote repository ie: "https://github.com/ScottGibb". After this input the folder path you wish to scan from. For example "D://"