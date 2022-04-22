# 507finalaajaafar
Instructions: Upon running the file the user will be prompted the following:
Input any key to continue, "help" for input guidelines, “info" for more information about the program, or "exit" to quit”.
Python Packages:
The required (not built-in) python packages for this code to work include requests, OS, and the MLB-Stats API wrapper for Python(https://pypi.org/project/MLB-StatsAPI/).
Data Sources
Data Source: https://statsapi.mlb.com/ (subscription cost is $35, wrapper used to circumvent it). 
Wrapper for the source, MLB-StatsAPI: https://pypi.org/project/MLB-StatsAPI/ 
Wiki/Documentation: https://github.com/toddrob99/MLB-StatsAPI/wiki
Data accessed through the “get” function of the wrapper. Documentation found here: https://github.com/toddrob99/MLB-StatsAPI/wiki/Function:-get . Allowed for advanced querying of the MLB StatsAPI.

Summary of data
•	~1000 records of data per season, one record for each player. Data involving player stats and team stats, and individual game stats also available (approximately one record per game). 
•	~4000-5000 records retrieved in total (one per each player per season used in program)

Data Structure
A network is used to link players to each other based on teams they previously played on using a “Player Graph” similar to the “Movie Graph” utilized in the Kevin Bacon project. The code for the graph and nodes is provided in the GitHub repo and below. 
