# Technical Assessment - Brian Makumi

## Question 1: Programming Fundamentals

**Task:** Remove duplicates from `12, 7, 12, 3, 5, 7, 8, 3, 9`, sort ascending, print the result.

Code: [`q1_programming_fundamentals/dedupe_sort.py`](./q1_programming_fundamentals/dedupe_sort.py)

```python
def dedupe_and_sort(numbers):
    unique_numbers = set(numbers)
    return sorted(unique_numbers)
```

**Output:** `[3, 5, 7, 8, 9, 12]`

**Approach:** A set in Python can't have duplicate values, so turning the list into a set gets rid of duplicates automatically. Then I just sort it with `sorted()` to get the numbers in order. It's a two-line fix, no need to write a manual loop checking for duplicates when Python already has a data type built for exactly this.

Why I went this route: I could've looped through the list and built a new one by checking `if x not in seen`, but that's O(n) per check, so O(n²) overall on a big list. Using a set is basically free, O(n) to build it, so unless order needs to be preserved from the original list (which the task doesn't ask for), there's no reason not to use it.

---

## Question 2: Django API Development

**Task:** CRUD API for blog posts with authentication and authorization.

Code: [`q2_django_api/`](./q2_django_api/)

- `blog_api/models.py` - the `BlogPost` model (title, content, author, timestamps)
- `blog_api/serializers.py` - turns model instances into JSON and back
- `blog_api/permissions.py` - custom rule so only the post owner can edit/delete
- `blog_api/views.py` - the viewset that handles all the CRUD logic
- `blog_api/urls.py` - routes for the API
- `project_settings_snippet.py` - the settings changes needed to plug this app into a project

**How it works:**

For authentication, I used DRF's token auth. A user logs in with their username/password at `/api/auth-token/` and gets a token back. From then on they attach that token to their requests (`Authorization: Token <token>`) so the API knows who they are.

Authentication alone just tells you *who* someone is - it doesn't say what they're allowed to do. That's where authorization comes in. I stacked two permission checks:
- Anyone can read posts (`GET`), but you need to be logged in to create one.
- Even if you're logged in, you can only edit or delete a post if you're the one who wrote it. I wrote a small custom permission class for that (`IsOwnerOrReadOnly`) since DRF doesn't have this exact rule built in.

I also made sure the author field is set automatically from whoever is logged in, rather than trusting whatever the client sends, otherwise someone could just claim to be a different author in their request.

Why token auth and not just session auth: sessions rely on cookies, which work fine for a browser but get awkward for a mobile app or a separate frontend calling the API. A token is just a header you attach to every request, so it works the same way regardless of what's consuming the API. If this were staying purely as a Django-rendered site, I'd probably have just used sessions instead.

**Endpoints:**

| Method | URL | What it does | Needs login? |
|--------|-----|---------------|---------------|
| GET | `/api/posts/` | list posts | No |
| POST | `/api/posts/` | create a post | Yes |
| GET | `/api/posts/<id>/` | view one post | No |
| PUT/PATCH | `/api/posts/<id>/` | update a post | Yes, must be the author |
| DELETE | `/api/posts/<id>/` | delete a post | Yes, must be the author |

---

## Question 3: Mobile App Design

**Context:** A simple app for a small shop owner in Kenya - add products, record sales, see today's total.

### 1. Screens

1. **Home / Dashboard**
2. **Add Product**
3. **Record Sale**
4. **Today's Sales**

### 2. What's on each screen

- **Home:** today's total sales front and center, plus quick buttons to record a sale or add a product.
- **Add Product:** name, price, and starting stock (optional).
- **Record Sale:** pick the product from a list, enter quantity, app shows the total before you confirm.
- **Today's Sales:** a running list of what's been sold today, with a total at the bottom.

### 3. Making it easy for a non-technical owner

1. Keep it visual and simple - big buttons, minimal text, everything reachable in a tap or two from the home screen. No digging through settings menus.
2. Support the local language and use a big numeric keypad instead of a tiny keyboard. It should also work offline, since not every shop has stable internet - sales get saved locally and sync later.

### 4. A mistake that could happen, and how to prevent it

Someone might tap the wrong product or mistype the quantity, say, meant to sell 2 but typed 20. That would throw off the whole day's total.

To catch this, the app should show a confirmation screen before saving the sale ("2 x Sugar = KSh 240 - confirm?"). And just in case something still slips through, an "undo last sale" button on the Today's Sales screen makes it easy to fix without digging through a menu.

I added the undo button on top of the confirmation step because a confirmation screen only helps if the owner actually reads it; in a busy shop with a customer waiting, people tap through confirmations without looking. So the real fix is making the mistake cheap to reverse, not just harder to make.

---

## Question 4: Relational Databases

**Task:** Design a schema for students, courses, and enrollments.

Code: [`q4_relational_databases/schema_and_query.sql`](./q4_relational_databases/schema_and_query.sql)

### 1 & 2. Tables and columns

**students**
| Column | Type |
|---|---|
| student_id | INTEGER (PK) |
| first_name | VARCHAR |
| last_name | VARCHAR |
| email | VARCHAR, unique |
| date_of_birth | DATE |

**courses**
| Column | Type |
|---|---|
| course_id | INTEGER (PK) |
| course_name | VARCHAR |
| description | TEXT |
| credits | INTEGER |

**enrollments** (links the two)
| Column | Type |
|---|---|
| enrollment_id | INTEGER (PK) |
| student_id | INTEGER, FK → students |
| course_id | INTEGER, FK → courses |
| enrollment_date | DATE |

### 3. Primary keys

`students.student_id`, `courses.course_id`, `enrollments.enrollment_id`

### 4. Connecting students to courses

A student can take many courses, and a course can have many students, that's a many-to-many relationship, which you can't model with a plain foreign key on either table. So I added an `enrollments` table in between. Each row just says "this student is in this course," with a foreign key pointing to each side. I also added a unique constraint on the pair so nobody gets enrolled in the same course twice by accident.

I went with a separate `enrollments` table instead of, say, a comma-separated list of course IDs on the student row, because that would make the "list students in a course" query basically impossible to write cleanly in SQL, and it breaks the moment you want to store anything about the enrollment itself (like the date). A junction table costs one extra table but keeps every future query simple.

### 5. Query: students enrolled in "Introduction to Programming"

```sql
SELECT s.student_id, s.first_name, s.last_name, s.email
FROM students s
JOIN enrollments e ON s.student_id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE c.course_name = 'Introduction to Programming';
```

This joins students to their enrollments, then joins those enrollments to courses so we can filter down to just the one course we care about.
