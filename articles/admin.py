from django.contrib import admin

from articles.models import Article, Category, Like


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name',)
    search_fields = ('name',)


class CategoryInline(admin.TabularInline):
    model = Article.subjects.through
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = (CategoryInline,)
    list_display = ('title', 'day', 'month', 'year')
    list_filter = ("subjects__name", 'day', 'month', 'year')
    list_fields = ('title', 'url', 'photo_url', 'gif_url', 'day', 'month', 'year')
    fieldsets = (
        (None, {
            "fields": (
                "title", "url",
                "abstract",
                ("photo_url", "gif_url"),
                ("day", "month", "year"),
            ),
        }),
    )

    search_fields = ('title', 'url', 'abstract')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
