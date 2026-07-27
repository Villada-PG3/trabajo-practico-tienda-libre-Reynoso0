## Tienda Libre

Proyecto realizado en **Django** para la materia **Programación III**.

El objetivo es aprender a desarrollar una aplicación web utilizando el patrón **MTV (Model - Template - View)** y trabajar con una base de datos.

---

# Tecnologías utilizadas

- Python 3.12
- Django
- SQLite
- HTML

---

# Cómo ejecutar el proyecto

## 1. Clonar el repositorio

```bash
git clone git@github.com:usuario/tienda-libre.git
cd tienda-libre
```

## 2. Crear el entorno virtual

```bash
python -m venv .venv
```

## 3. Activarlo

Linux:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

## 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## 5. Aplicar las migraciones

```bash
python manage.py migrate
```

## 6. Crear un administrador

```bash
python manage.py createsuperuser
```

## 7. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

Panel de administración:

```
http://127.0.0.1:8000/admin/
```

---

# Estructura del proyecto

```
config/
```

Contiene la configuración principal del proyecto.

- settings.py
- urls.py
- asgi.py
- wsgi.py

```
tiendalibre/
```

Aplicación principal.

- models.py
- views.py
- urls.py
- admin.py
- templates/

```
manage.py
```

Archivo principal para ejecutar comandos de Django.

```
requirements.txt
```

Lista de dependencias del proyecto.

---

# Lo visto hasta ahora

## Clase 1

- Instalación de Django.
- Creación del proyecto.
- Creación de la aplicación.
- Primer modelo.
- Registro del modelo en el panel de administración.
- Migraciones.
- Uso del administrador.

## Clase 2

- Patrón MTV.
- Configuración de URLs.
- Creación de vistas.
- Primer template HTML.
- Renderizado de páginas.

---

# Comandos útiles

Crear migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

Crear administrador:

```bash
python manage.py createsuperuser
```

Ejecutar el servidor:

```bash
python manage.py runserver
```

Abrir la consola de Django:

```bash
python manage.py shell
```

---

# Notas

- Siempre activar el entorno virtual antes de trabajar.
- Después de modificar un modelo ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```

- Si se instala una nueva librería actualizar:

```bash
pip freeze > requirements.txt
```

---

Proyecto realizado como práctica para aprender Django.
