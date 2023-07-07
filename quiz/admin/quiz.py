from django.contrib.admin import (
    ModelAdmin,
    register,
)

from quiz.admin.categories import SortableAdminMixin
from quiz.models.quiz import Quiz


@register(Quiz)
class QuizModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }