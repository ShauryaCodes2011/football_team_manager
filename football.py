from llm import invoke


def teamComp(team_a,team_b):

    output_structure = """{
        "team_name": string containing the name of the team,
        "description: short one line justifying the result,
        "score": int range(0,100) you have to provide score based on the team performance,
        
    }"""
    prompt = f"given {team_a} & {team_b} provide me the outpute in this structure {output_structure}"

    result = eval(invoke(prompt).split("```json")[1].split("```")[0]) # algo
    
    return result