import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', nome='Análise de Atrito')

@app.route('/predicao', methods=['POST'])
def predicao():
  Age = request.form['Age']
  YearsAtCompany = request.form['YearsAtCompany']
  Department = request.form['Department']
  JobSatisfaction = request.form['JobSatisfaction']
  MaritalStatus = request.form['MaritalStatus']
  WorkLifeBalance = request.form['WorkLifeBalance']
 

  array=[[str(Age), str(YearsAtCompany), str(Department), str(JobSatisfaction), str(MaritalStatus), str(WorkLifeBalance)]]

  predicao = model.predict(array)

  return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)
