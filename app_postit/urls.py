from django.urls import path
from . import views
from .views import editar_quadro, deletar_quadro

urlpatterns = [
    path('upload/', views.upload_planilha, name='upload_planilha'),
    path('selecionar_colunas/', views.selecionar_colunas, name='selecionar_colunas'),
    path('salvar_colunas/', views.salvar_colunas, name='salvar_colunas'),  # Adicione esta linha
    path('listar_quadros/', views.listar_quadros, name='listar_quadros'),
    path('criar_quadro/', views.criar_quadro, name='criar_quadro'),
    path('exibir_quadros/<int:quadro_id>/', views.exibir_quadro, name='exibir_quadros'),
    path('exibir_dados/', views.exibir_dados, name='exibir_dados'),
    path('exportar_dados/', views.exportar_dados, name='exportar_dados'),
    path('', views.home, name='home'),
    path('quadro/<int:quadro_id>/editar/', editar_quadro, name='editar_quadro'),
    path('quadro/<int:quadro_id>/deletar/', deletar_quadro, name='deletar_quadro'),
    path('salvar_personalizado/<int:quadro_id>/', views.salvar_personalizado, name='salvar_personalizado'),
    path("quadro/<int:quadro_id>/atualizar_planilha/", views.atualizar_planilha, name="atualizar_planilha"),

]
