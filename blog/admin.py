from django.contrib import admin
from .models import Category,Post, Copyuser
# Register your models here.

#for configuratiom of categoru admin

class CategoryAdmin(admin.ModelAdmin):
    list_display=('image_tag','title', 'description' ,'url','add_date')
    search_fields=('url',)
    list_filter = ('url',)


@admin.register(Copyuser)
class CopyuserAdmin(admin.ModelAdmin):
    list_display = ('cu_id', 'first_name', 'last_name', 'email', 'phone', 'address', 'pin',)
    search_fields = ('email',)




class PostAdmin(admin.ModelAdmin):
    list_display=('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

    class Media:
        js = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js','js/script.js',)










admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
