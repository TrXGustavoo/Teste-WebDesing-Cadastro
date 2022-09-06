from django.contrib import admin
from .models import Profile

# Register your models here.

@admin.action(description='Ativar gluten')
def ativar_gluten(modelamin, request, queryset):
    queryset.update(intolerancia_a_Gluten=True)

@admin.action(description='Ativar Lactose')
def ativar_lactose(modelamin, request, queryset):
    queryset.update(intolerancia_a_Lactose=True)

@admin.action(description='Desativar gluten')
def desativar_gluten(modelamin, request, queryset):
    queryset.update(intolerancia_a_Gluten=False)

@admin.action(description='Desativar Lactose')
def desativar_lactose(modelamin, request, queryset):
    queryset.update(intolerancia_a_Lactose=False)

class profileAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'idade',
        'intolerancia_a_Gluten',
        'intolerancia_a_Lactose',
    ]
    list_filter = [
        'nome_completo',
        'idade',
        'intolerancia_a_Gluten',
        'intolerancia_a_Lactose',
    ]
    search_fields = [
        'nome_completo',
        'idade',
        'intolerancia_a_Gluten',
        'intolerancia_a_Lactose',
    ]
    actions = [
        ativar_gluten,
        ativar_lactose,
        desativar_gluten,
        desativar_lactose,
    ]
admin.site.register(Profile, profileAdmin)

