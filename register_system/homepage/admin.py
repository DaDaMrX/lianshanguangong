from django.contrib import admin
from .models import Notice, NoticeFile, HomePage, HomePageImage

class NoticeFileInLine(admin.TabularInline):
    model = NoticeFile

class NoticeAdmin(admin.ModelAdmin):
    inlines = [
        NoticeFileInLine,
    ]

admin.site.register(Notice, NoticeAdmin)


class HomePageWithImage(admin.TabularInline):
    model = HomePageImage

class HomePageAdmin(admin.ModelAdmin):
    model = HomePage
    inlines = [
        HomePageWithImage
    ]
    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)
    def has_delete_permission(self, request, obj=None):
        return False if self.model.objects.count() > 0 else super().has_delete_permission(request)

admin.site.register(HomePage, HomePageAdmin)