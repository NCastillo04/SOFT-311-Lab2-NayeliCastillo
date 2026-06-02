# Instrucciones

Para ejecutar usar vscode y abrir el archivo login_test.py, una vez abierto ejecutar en la terminal o seleccionar el boton de Run en la parte superior derecha.

El proyecto esta organizado por paginas (home_page, signup_page y login_page) y un test (login_test)

El programa automatiza el proceso de registro (signup) desde la pantalla de login, luego registra un usuario, valida que haya sido exitoso el registro validando
la pagina actual (/account_created), luego valida que carga bien el home y por ultimo valida el login automatico del proceso de registro por medio de si es
visible o no el boton logout

# Comandos

```py
py -m venv .venv
.venv\Scripts\activate
.\.venv\Scripts\python -m pip install --upgrade pip
.\.venv\Scripts\pip install -e .
.\.venv\Scripts\python -m playwright install chromium
```

# Ejecucion

```py
.venv\Scripts\python -m pytest --html=report.html --self-contained-html
```
