# Music Diagnosis App
This project is a FastAPI-based application for music diagnosis.
Setup and Installation
## Prerequisites

Python 3.11 or higher
pip (Python package installer)
pyenv (recommended for Python version management)

## Setting up the development environment

Clone the repository:
```
git clone https://github.com/yourusername/dev-music-diagnosis-app.git
cd dev-music-diagnosis-app
```

## Set up Python version with pyenv:
```
pyenv install 3.11.4
pyenv local 3.11.4
```

## Create and activate a virtual environment:
```
python -m venv venv
source venv/bin/activate  # On macOS/Linux
# OR
venv\Scripts\activate.bat  # On Windows
```

## Install dependencies from requirements.txt:
```
pip install -r requirements.txt
```


## Running the application locally
To run the application in development mode:
```
uvicorn app.main:app --reload
```
The API will be available at http://127.0.0.1:8000.

## Use Alembic for database migrations:
```
alembic revision --autogenerate -m "Description of the change"
alembic upgrade head
```

## Add new dependencies to requirements.txt:
```
pip install new-package
pip freeze > requirements.txt
```

## Code Quality and Formatting
We use several tools to maintain code quality and consistency:
### Black (Code formatter):
```
black .
```

### isort (Import sorter):
```
isort .
```

### flake8 (Linter):
```
flake8 .
```

### mypy (Static type checker):
```
mypy .
```


