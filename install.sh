# Criamos este arquivo para instalar todas as dependências na hora que inícia o Script
# Escrever no terminal -->  $ . ./install.sh

python3 -m venv venv_docker;
source venv_docker/bin/activate;
pip install -r requirements.txt;
pre-commit install;

