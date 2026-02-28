# SisNum - AGENTS.md

## Project Overview

SisNum is a Django web application for controlling sequential numbering of administrative documents (Memorandos, Circulares, Ofícios, etc.). It replaces manual control with a simple web interface.

- **Backend:** Python, Django 6.0.2
- **Database:** SQLite
- **Frontend:** HTML with Bootstrap (via CDN)

## Development Commands

### Running the Application

```bash
python manage.py runserver
```

Access at http://localhost:8000/

### Database Migrations

```bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### Testing

Run all tests:
```bash
python manage.py test
```

Run tests for a specific app:
```bash
python manage.py test documentos
```

Run a single test class:
```bash
python manage.py test documentos.tests.TipoDocumentoModelTest
```

Run a single test method:
```bash
python manage.py test documentos.tests.TipoDocumentoModelTest.test_proximo_numero
```

### Django Management Commands

```bash
# Create superuser
python manage.py createsuperuser

# Check for issues
python manage.py check

# Show URLs
python manage.py show_urls
```

### Linting (Optional - not configured)

If you add linting, consider using:
- **ruff**: `ruff check .` (fast, modern)
- **flake8**: `flake8 .`
- **pylint-django**: for Django-specific analysis

Install with: `pip install ruff` or `pip install flake8`

## Code Style Guidelines

### General

- Follow Django and Python conventions
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 120 characters
- Use meaningful, descriptive names

### Imports

Organize imports in this order (per PEP 8):
1. Standard library
2. Third-party
3. Django
4. Local application

Within each group, alphabetize:

```python
# Good
import os
from pathlib import Path

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from .models import TipoDocumento
from .forms import TipoDocumentoForm
```

### Models (models.py)

- Use `PascalCase` for model class names
- Use `snake_case` for field names
- Define `__str__` method on every model
- Add verbose_name for user-facing fields when needed

```python
# Good
class TipoDocumento(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    ultimo_numero = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

    def proximo_numero(self):
        return self.ultimo_numero + 1
```

### Views (views.py)

- Use function-based views (FBV) for simple operations
- Use `@login_required` decorator for protected views
- Use `get_object_or_404` for single-object retrieval
- Use Django's messaging framework for user feedback
- Return `redirect` after POST requests (Post/Redirect/Get pattern)

```python
@login_required(login_url='login')
def index(request):
    if request.method == 'POST':
        form = TipoDocumentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tipo de documento cadastrado com sucesso!')
            return redirect('index')
    # ...
```

### Forms (forms.py)

- Use `ModelForm` for model-backed forms
- Define `Meta` class with `model`, `fields`, and `widgets`
- Use Bootstrap classes in widgets for styling

```python
class TipoDocumentoForm(forms.ModelForm):
    class Meta:
        model = TipoDocumento
        fields = ['nome']
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: Memorando, Ofício, Circular...',
            })
        }
```

### URLs (urls.py)

- Use descriptive URL names
- Use trailing slashes
- Group related URLs

```python
# Good
urlpatterns = [
    path('', views.index, name='index'),
    path('incrementar/<int:tipo_id>/', views.incrementar, name='incrementar'),
    path('zerar/', views.zerar_todos, name='zerar_todos'),
]
```

### Templates

- Store in `templates/documentos/`
- Use Django template inheritance
- Load static files with `{% load static %}`
- Use Bootstrap classes for styling

### Error Handling

- Use Django's built-in exceptions (`Http404`, `PermissionDenied`)
- Use `messages` framework for user feedback
- Log errors appropriately
- Never expose sensitive information in error messages

### Security

- Never commit secrets (use environment variables in production)
- Use `@login_required` for protected views
- Validate all user input via forms
- Use CSRF protection (enabled by default in Django)

### Testing

- Write tests for models, views, and forms
- Use Django's test client for view testing
- Use `TestCase` for database-backed tests

```python
from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class TipoDocumentoModelTest(TestCase):
    def test_proximo_numero(self):
        tipo = TipoDocumento.objects.create(nome='Memorando', ultimo_numero=5)
        self.assertEqual(tipo.proximo_numero(), 6)
```

### Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Models | PascalCase | `TipoDocumento` |
| Fields | snake_case | `ultimo_numero` |
| Methods | snake_case | `proximo_numero()` |
| URLs | lowercase with hyphens | `zerar-todos` |
| URL names | snake_case | `zerar_todos` |
| Templates | lowercase | `index.html` |
| Variables | snake_case | `tipo_id` |
| Constants | UPPER_SNAKE_CASE | `MAX_LENGTH` |

### File Organization

```
sisnum/
├── manage.py
├── sisnum/              # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── documentos/          # Main app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── admin.py
│   ├── apps.py
│   ├── tests.py
│   └── migrations/
├── templates/
│   └── documentos/
├── static/
└── media/
```

## Working with This Project

1. Activate virtual environment: `source venv/bin/activate`
2. Run migrations if needed: `python manage.py migrate`
3. Create superuser: `python manage.py createsuperuser`
4. Run server: `python manage.py runserver`
5. Run tests: `python manage.py test`
