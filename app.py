#import flask, and render template function
from flask import Flask, render_template,jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)
#defining a job list for dynamic entry
JOBS = [
  {
    'Id': 1,
    'Title': 'Data Analyst',
    'Location': 'Winnipeg, MB',
    'Salary': '$50,000'
  },
  {
    'Id': 2,
    'Title': 'Data Scienist',
    'Location': 'Winnipeg, MB',
    'Salary': '$75,000'
  },
  {
    'Id': 3,
    'Title': 'Frontend Engineer ',
    'Location': 'Remote',
    'Salary': '$50,000'
  },
  {
    'Id': 4,
    'Title': 'Backend Engineer ',
    'Location': 'Winnipeg, MB',
    'Salary': '$85,000'
  }
]
#define function to return jobs from database
def load_jobs_from_db():
  #with statement closes the connection when the with statement is exited
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
  #convert the result to a list of dictionaries
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
    return jobs

# define view function called hello_world using app.route decorator  
# converts a reg function into a view function
@app.route("/")
def hello_world():
  jobs = load_jobs_from_db()
  return render_template("home.html", jobs=JOBS, company_name="Jovian")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)