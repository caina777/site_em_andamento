from flask import Flask, render_template, request

app = Flask(__name__)

# Dados dos cursos
cursos = [
    {'id': 1, 'nome': 'Curso de Python', 'descricao': 'Aprenda Python do zero.', 'preco': 'R$ 100,00', 'imagem': 'python.jpg'},
    {'id': 2, 'nome': 'Curso de Flask', 'descricao': 'Desenvolva aplicações web com Flask.', 'preco': 'R$ 150,00', 'imagem': 'flask.jpg'},
    {'id': 3, 'nome': 'Curso de Data Science', 'descricao': 'Introdução à ciência de dados.', 'preco': 'R$ 200,00', 'imagem': 'datascience.jpg'},
    {'id': 4, 'nome': 'Gestão Financeira', 'descricao': 'Aprenda a gerenciar suas finanças de forma eficiente.', 'preco': 'R$ 120,00', 'imagem': 'gestao_financeira.jpg'},
    {'id': 5, 'nome': 'Economia', 'descricao': 'Entenda os conceitos básicos e avançados de economia.', 'preco': 'R$ 130,00', 'imagem': 'economia.jpg'},
    {'id': 6, 'nome': 'Estatística', 'descricao': 'Fundamentos de estatística para análise de dados.', 'preco': 'R$ 140,00', 'imagem': 'estatistica.jpg'},
    {'id': 7, 'nome': 'Gestão de RH', 'descricao': 'Como gerenciar recursos humanos e equipes.', 'preco': 'R$ 110,00', 'imagem': 'gestao_rh.jpg'},
    {'id': 8, 'nome': 'Curso de Java', 'descricao': 'Desenvolva aplicativos com Java.', 'preco': 'R$ 160,00', 'imagem': 'java.jpg'},
    {'id': 9, 'nome': 'Curso de CSS', 'descricao': 'Aprenda a estilizar páginas web com CSS.', 'preco': 'R$ 90,00', 'imagem': 'css.jpg'}
]

@app.route('/')
def home():
    return render_template('index.html', cursos=cursos)

@app.route('/pagamento/<int:curso_id>')
def pagamento(curso_id):
    curso = next((c for c in cursos if c['id'] == curso_id), None)
    if curso is None:
        return "Curso não encontrado", 404
    return render_template('pagamento.html', curso=curso)

@app.route('/confirmacao/<int:curso_id>', methods=['POST'])
def confirmacao(curso_id):
    curso = next((c for c in cursos if c['id'] == curso_id), None)
    if curso is None:
        return "Curso não encontrado", 404
    return render_template('confirmacao.html', curso=curso)

if __name__ == '__main__':
    app.run(debug=True)
