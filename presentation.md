---
marp: true
theme: uncover
paginate: true
---

# Калькулятор на Django
## Лабораторная работа №11

---

## Цель работы

Разработка веб-приложения на Django
с использованием Docker-контейнеризации

---

## Инструменты

- **uv** — менеджер зависимостей
- **Django** — веб-фреймворк
- **Docker** — контейнеризация
- **Marp** — презентации из Markdown

---

## Структура проекта

```
my_django_project/
├── calculator/        # Приложение
│   ├── models.py      # Модель CalculationHistory
│   ├── views.py       # Логика калькулятора
│   ├── urls.py        # Маршруты
│   └── templates/     # HTML-шаблоны
├── config/            # Настройки Django
├── Dockerfile         # Инструкции сборки
└── docker-compose.yml # Оркестрация
```

---

## Модель данных

```python
class CalculationHistory(models.Model):
    num1 = models.FloatField()
    num2 = models.FloatField()
    operation = models.CharField(max_length=1)
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
```

---

## Логика (views.py)

- **GET** — отображение формы и истории
- **POST** — вычисление, сохранение в БД
- Поддержка операций: +, -, *, /

---

## Dockerfile

```dockerfile
FROM python:3.14-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev
COPY . .
ENV PATH="/app/.venv/bin:$PATH"
EXPOSE 8000
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
```

---

## Результат

![width:700px](скриншот_калькулятора.png)

- Калькулятор работает локально и в Docker
- История сохраняется в SQLite

---

## Спасибо за внимание!!
