<div align="center">
  <h3 align="center">Personal Finace Tracker</h3>

  <div>
    <img src="https://img.shields.io/badge/-Python-black?logo=python&logoColor=white&color=3776AB" alt="python">
    <img src="https://img.shields.io/badge/-Django-black?logo=django&logoColor=white&color=092E20" alt="django">
    <img src="https://img.shields.io/badge/-HTMX-black?logoColor=white&logo=htmx&color=3366CC" alt="htmx" />
    <img src="https://img.shields.io/badge/-Tailwind_CSS-black?logoColor=white&logo=tailwindcss&color=06B6D4" alt="tailwindcss" />
    <img src="https://img.shields.io/badge/-Cloudinary-black?logoColor=white&logo=cloudinary&color=3448C5" alt="cloudinary" />
    <img src="https://img.shields.io/badge/-Postgresql-black?logoColor=white&logo=postgresql&color=4169E1" alt="postgresql" />
  </div>
</div>

## <a name="quick-start">🚀 Quick Start</a>

Follow these steps to set up the project locally on your machine.

**Prerequisites**

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/en)
- [Postgresql](https://www.postgresql.org/download/windows/) (Optional)

**Installation**

Install the project dependencies using `pip`:

```bash
pip install -r requirements.txt
python manage.py tailwind install
```

**Installation**

Create `.env` file in `root` folder:

```bash
SECRET_KEY="<your_secret_key>"
DATABASE_URL="postgres://<username>:<password>@<hostname>:<port>/<dbname>"
# OPTIONAL
CLOUDINARY_CLOUD_NAME="<your_LOUDINARY_CLOUD_NAME>"
CLOUDINARY_API_KEY="<your_CLOUDINARY_API_KEY>"
CLOUDINARY_API_SECRET="your_CLOUDINARY_API_SECRET"
```

**Running the Project**

Update `root/Personal_Finace_Tracker/settings.py` file:

```python
DEBUG = True
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
INTERNAL_IPS = [
    "127.0.0.1",
]
```

```bash
python manage.py tailwind start
```

```bash
python manage.py migrate 
python manage.py runserver
```

Open [http://localhost:8000](http://localhost:8000) in your browser to view the project.


