import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hangarin.settings')
django.setup()

from faker import Faker
from django.utils import timezone
from tasks.models import Priority, Category, Task, Note, SubTask

fake = Faker()

# ── 1. Seed Priority ─────────────────────────────────────────
print("Seeding priorities...")
priority_names = ["High", "Medium", "Low", "Critical", "Optional"]
priorities = []
for name in priority_names:
    p, created = Priority.objects.get_or_create(name=name)
    priorities.append(p)
print(f"  ✔ {len(priorities)} priorities added.")

# ── 2. Seed Category ─────────────────────────────────────────
print("Seeding categories...")
category_names = ["Work", "School", "Personal", "Finance", "Projects"]
categories = []
for name in category_names:
    c, created = Category.objects.get_or_create(name=name)
    categories.append(c)
print(f"  ✔ {len(categories)} categories added.")

# ── 3. Seed Tasks ────────────────────────────────────────────
print("Seeding tasks...")
for _ in range(10):
    task = Task.objects.create(
        title=fake.sentence(nb_words=5),
        description=fake.paragraph(nb_sentences=3),
        deadline=timezone.make_aware(fake.date_time_this_month()),
        status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
        priority=fake.random_element(elements=priorities),
        category=fake.random_element(elements=categories),
    )

    # ── 4. Seed Notes for each Task ──────────────────────────
    for _ in range(2):
        Note.objects.create(
            task=task,
            content=fake.paragraph(nb_sentences=2),
        )

    # ── 5. Seed SubTasks for each Task ───────────────────────
    for _ in range(3):
        SubTask.objects.create(
            parent_task=task,
            title=fake.sentence(nb_words=4),
            status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
        )

print("  ✔ 10 tasks with notes and subtasks added.")
print("\n✅ Database seeded successfully!")