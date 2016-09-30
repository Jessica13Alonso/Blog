from django.contrib import admin
from .models import Post, Comentario
# Register your models here.

class PostAdmin (admin.ModelAdmin):
	list_display = (
			'titulo',
			'slug',
			'creado'
		)
	prepopulated_fields = {'slug': ('titulo',)}
	list_filter = ('creado', 'titulo')
	search_fields = ('titulo', 'contenido', 'slug')

admin.site.register(Post, PostAdmin)
admin.site.register(Comentario)