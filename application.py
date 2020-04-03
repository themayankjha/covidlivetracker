from flask import Flask, render_template, redirect, url_for
import apiresolver
app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    summary=apiresolver.getsummary()
    total=summary['total']
    confirmedCasesIndian=summary['confirmedCasesIndian']
    confirmedCasesForeign=summary['confirmedCasesForeign']
    discharged=summary['discharged']
    statelist=apiresolver.statelist()
    deaths=summary['deaths']
    confirmcases=apiresolver.confirmcases()
    deathcases=apiresolver.deathcases()
    dischargedcases=apiresolver.dischargedcases()
    return render_template('dashboard.html', total=total,discharged=discharged,deaths=deaths,confirmedCasesIndian=confirmedCasesIndian,confirmedCasesForeign=confirmedCasesForeign,statelist=statelist,confirmcases=confirmcases,deathcases=deathcases,dischargedcases=dischargedcases)

if __name__ == '__main__':
    app.run()
