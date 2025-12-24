# Instructions

clonar projeto: https://github.com/florisa/imob.git/

# Setup inicial

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
brew install python
```

# Criar virtual environment

```
python3 -m venv env
```

# Ativar virtual env

```
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

# Wagtail

```
pip install wagtail
```

# Dependencias

```
pip install -r requirements.txt
```

# Instalar pacotes node

```
npm install
```

# Corrigir permissões do Sass (apenas uma vez após instalar pacotes node)

```
chmod +x node_modules/.bin/sass
```

# Rodar servidor local

```
env/bin/honcho start
```

# Pages:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/inicio
- http://127.0.0.1:8000/imóveis

```

```
