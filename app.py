from flask import Flask, render_template, request
from llm import invoke
from football import teamComp
app= Flask(__name__)

print(type(app))


@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        print(request.form)
        teamA=request.form.get('teamA')
        teamB=request.form.get('teamB')
        result=teamComp(teamA,teamB)
        
        teamname1 = result[0]['team_name']
        description1 =result[0]['description']
        print(result)
        print(type(result))
        score1=result[0]['score']

        teamname2 = result[1]['team_name']
        description2 =result[1]['description']
        score2 =result[1]['score']
        return render_template('index.html',teamname1=teamname1,description1=description1,score1=score1,teamname2=teamname2,description2=description2,score2=score2)
    return render_template('index.html')

@app.route("/<teamname>/")
def teampage(teamname):
    club=teamname
    context={'teamname':club}
    return render_template(template_name_or_list="teampage.html",**context)

@app.route("/python_filehandling")
def python_filehandling():
    f=open("index.html",'r')
    data=f.read()
    f.close()
    return data

if __name__=="__main__":
    app.run(host='localhost',port='8000')



    # get request, post req, decorator





# HW
# get and post request, use llm , compare two games
# mood=" i want to racing game "