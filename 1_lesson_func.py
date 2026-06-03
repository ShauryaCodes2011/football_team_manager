# func

def calcTeamgoals(team):
    return len(team)*50


def goalCount(*args) -> list[int]:    # args
    """
    This function calculates the goal count by the given teams 
    Params:
    team1: str name of the football team
    team2 : str name of the football team

    Returns:
    List of goal done by the teams

    Example:
    >>> goalCount('fcb','psg')
    [100,50]

    >>> goalCount('rm','psg')
    [150,50]
    """
    result=[]
    for team in args:
        result.append(calcTeamgoals(team))
    return result






def invitationCard(**team_stat) -> list[int]:    # kwargs
    print(team_stat)


print(goalCount('fcb','rm','psg2'))

print(invitationCard(name='fcb',bio='best team'))

names=['tom','jerry']
fts=['fcb','rm','psg']
for name in names:
    for ft in fts:
        print("hello {player_name}, you are invited to play for {team_name}, would you accept".format(player_name=name,team_name=ft))




# jinja (template)  -> python code to render it as an html    ( backend dev)

# what was that template? (frontend)

# inserts the values in the tempalte, which tempalte to use when? ( backend dev)

