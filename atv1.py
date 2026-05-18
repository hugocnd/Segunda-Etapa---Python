from flask import Flask

app = Flask(__name__)

@app.route('/decorator')
def explicar():
    return """
    <h1> O que é um decorator? </h1>
    Em Python, um decorator (decorador) é uma função que recebe outra função como argumento, adiciona alguma funcionalidade a ela e retorna a função modificada. Tudo isso sem alterar o código original da função decorada.
    Eles são representados pelo símbolo de arroba (@) seguido pelo nome da função decoradora, colocado logo acima da definição da função alvo.

    <h1> Para que servem? </h1>
    Os decorators servem para aplicar a reutilização de código, separando a "lógica de negócio" da sua aplicação de tarefas secundárias ou transversais (também chamadas de cross-cutting concerns).
    Casos de uso comuns incluem:
    <p> - Verificar se o usuário está logado antes de permitir o acesso a uma página. </p>
    <p> - Medir o tempo de execução de uma função ou registrar quando ela foi chamada. </p>
    <p> - Capturar falhas e exceções automaticamente. </p>

    <h1> Como ele é utilizado no Flask? </h1>
    <p> No framework web Flask, o decorator @app.route serve para mapear URLs do seu site/API para funções específicas em Python. Quando alguém acessa um determinado endereço no navegador, o Flask sabe qual função deve ser executada. </p>
"""


if __name__ == '__main__':
    app.run(debug=True)
