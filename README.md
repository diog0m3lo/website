# Meu Website Pessoal

Este é o repositório do meu website pessoal, desenvolvido para apresentar o meu currículo e o meu portfólio de fotografias. É construído com **Flask** e inclui um formulário de contacto.

## 🚀 Funcionalidades

- Página inicial com uma introdução.
- Seção para o meu currículo.
- Galeria para o portfólio de fotografias.
- Formulário de contacto funcional.

## 🛠️ Tecnologias Utilizadas

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Flask (Python)
- **Estrutura:** Templates e Rotas

## 📂 Estrutura do Projeto

meu_website/
│
├── app/
│   ├── static/        # Ficheiros estáticos (CSS, imagens, JS)
│   ├── templates/     # Templates HTML
│   ├── init.py    # Inicialização do Flask
│   └── routes.py      # Definição de rotas
│
├── venv/              # Ambiente virtual (ignorado no GitHub)
├── requirements.txt   # Dependências do projeto
├── run.py             # Ponto de entrada do projeto
└── .gitignore         # Lista de ficheiros ignorados

## 🖥️ Como Executar

1. Clonar o repositório:
   ```bash
   git clone https://github.com/<teu-usuario>/<nome-do-repositorio>.git
   cd <nome-do-repositorio>

2. Criar e ativar um ambiente virtual:
    python3 -m venv venv
    source venv/bin/activate

3. Instalar as dependências:
    pip install -r requirements.txt

4. Executar o servidor Flask:
    python run.py

5. Abrir o navegador em http://127.0.0.1:5000
