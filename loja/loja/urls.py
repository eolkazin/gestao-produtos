from django.contrib import admin
from django.urls import path
from produtos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Rota para o painel de administração do Django
    path('admin/', admin.site.urls),

    # Rota para a lista de itens, que chama a view 'listar_itens'
    path('', views.listar_itens, name='listar_itens'),

    # Rota para a página de cadastro de um novo item, que chama a view 'cadastrar_item'
    path('cadastrar/', views.cadastrar_item, name='cadastrar'),

    # Rota para deletar um item específico, passando o 'id' do item na URL
    path('deletar/<int:id>/', views.deletar_item, name='deletar_item'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)