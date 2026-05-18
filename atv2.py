from flask import Flask
app = Flask(__name__)

@app.route('/curriculo')
def inicio():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <h1> Currículo </h1>

        <h2> Informações pessoais: </h2>
        <ul>
            <li> Nome: Hugo Carvalho Nascimento </li>
            <li> Email: 22400206@aluno.cotemig.com.br </li>
            <li> Telefone: +55 (31) 998968389 </li>
        </ul>

        <h2> Experiência Profissional: </h2>
        <ul>
            <li> Empresa: Cotemig </li>
            <li> Cargo: Aluno </li>
            <li> Período: 3° ano do EM </li>
        </ul>
    </body>
    </html>
'''
