# Mi Aplicación Flask

Esta es una aplicación Flask básica que se conecta a una base de datos de ElephantSQL y despliega datos en una página web.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. Crea y activa un entorno virtual:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Configura la URL de tu base de datos ElephantSQL en una variable de entorno:
    ```bash
    export DATABASE_URL=tu_database_url
    ```

5. Ejecuta la aplicación:
    ```bash
    python app.py
    ```

## Despliegue

Este proyecto está configurado para ser desplegado en Heroku. Asegúrate de tener el [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) instalado y sigue estos pasos:

1. Inicia sesión en Heroku:
    ```bash
    heroku login
    ```

2. Crea una nueva aplicación en Heroku:
    ```bash
    heroku create
    ```

3. Configura la URL de tu base de datos ElephantSQL en Heroku:
    ```bash
    heroku config:set DATABASE_URL=tu_database_url
    ```

4. Despliega la aplicación en Heroku:
    ```bash
    git push heroku main
    ```

5. Abre la aplicación en tu navegador:
    ```bash
    heroku open
    ```

## Uso

La aplicación mostrará los datos de tu base de datos ElephantSQL en la página principal.
