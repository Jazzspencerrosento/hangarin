from django.contrib import admin
from .models import Priority, Category, Task, Note, SubTask


# ── Priority Admin ───────────────────────────────────────────
@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# ── Category Admin ───────────────────────────────────────────
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


# ── Task Admin ───────────────────────────────────────────────
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'deadline', 'priority', 'category']
    list_filter = ['status', 'priority', 'category']
    search_fields = ['title', 'description']


# ── SubTask Admin ────────────────────────────────────────────
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'parent_task_name']
    list_filter = ['status']
    search_fields = ['title']

    # Custom field to show the parent task name
    def parent_task_name(self, obj):
        return obj.parent_task.title
    parent_task_name.short_description = 'Parent Task'


# ── Note Admin ───────────────────────────────────────────────
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ['task', 'content', 'created_at']
    list_filter = ['created_at']
    search_fields = ['content']