# Enclan Africa Technical Assessment - Brian Makumi

Written answers are in [`answers.md`](./answers.md). Code is split one folder per question.

## Structure

```
enclan-assessment/
├── answers.md
├── README.md
├── q1_programming_fundamentals/
│   └── dedupe_sort.py
├── q2_django_api/
│   ├── blog_api/
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── permissions.py
│   │   ├── views.py
│   │   └── urls.py
│   └── project_settings_snippet.py
└── q4_relational_databases/
    └── schema_and_query.sql
```

(For question 3, the answer is in `answers.md`.)

## Running it

**Q1**
```bash
cd q1_programming_fundamentals
python dedupe_sort.py
```
Output: `[3, 5, 7, 8, 9, 12]`

**Q2**
`blog_api/` is a Django app, not a full project (kept it small on purpose). To try it out:
```bash
python -m venv venv
source venv/bin/activate
pip install django djangorestframework

django-admin startproject project .
# copy q2_django_api/blog_api/ into the new project folder
# apply the settings changes in project_settings_snippet.py

python manage.py makemigrations blog_api
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Then POST to `/api/auth-token/` with a username/password to get a token, and use it for creating/editing/deleting posts.

**Q4**
Run `schema_and_query.sql` against MySQL/Postgres/SQLite (swap `AUTO_INCREMENT` for `SERIAL`/`AUTOINCREMENT` depending on the engine).
