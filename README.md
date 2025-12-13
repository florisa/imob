# Instructions
clonar projeto: https://github.com/florisa/imob.git/

# Criar virtual environment
python3 -m venv env

# Ativar virtual env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

# Wagtail
pip install wagtail

# Dependencias
pip install -r requirements.txt

# Rodar servidor local
python manage.py runserver
