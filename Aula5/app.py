from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def questao1():
    nomep = "Hugo"
    return render_template('questao1.html', nome=nomep)

@app.route('/questao2')
def questao2():
    nomep = "Hugo"
    idadep = "17"
    return render_template('questa2.html', nome=nomep, idade=idadep)

def questao3():
@app.route('/questao3')
    nomep = "Hugo"
    emailp = "22400206@aluno.cotemig.com.br"
    return render_template('questao3.html', nome=nomep, email=emailp)

@app.route('/questao4')
def questao4():
    lista_alunos = [
        {"nome": "Analice", "nota": 8},
        {"nome": "Isabela", "nota": 9},
        {"nome": "Hugo", "nota": 7}
    ]
    return render_template('questao4.html', alunos=lista_alunos)

@app.route('/questao5')
def questao5():
    lista_alunos = [
        {"nome": "Analice", "nota": 8},
        {"nome": "Isabela", "nota": 9},
        {"nome": "Hugo", "nota": 7}
    ]
    return render_template('questao5.html', alunos=lista_alunos)

if __name__ == '__main__':
    app.run(debug=True)
