from django.contrib.admin import (
    ModelAdmin,
    register,
)

from quiz.models.categories import Category


class SortableAdminMixin:
    pass


@register(Category)
class CategoryModelAdmin(SortableAdminMixin, ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }