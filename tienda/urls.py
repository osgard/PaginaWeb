from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        url(r'^$', views.producto_list, name='index'),#aqui se pone la url que aparece en el buscador y en name= se pone el nombre de tu html
		url(r'^cliente/new/$', views.cliente_new, name='cliente_new'),
		url(r'^cliente/log/$', views.cliente_log, name='cliente_log'),
		url(r'^logout/', views.cerrar, name='log_out'),
		url(r'^producto/(?P<pk>[0-9]+)/$', views.producto_detail, name='producto_detail'),
		#url(r'^carrito/$', views.carrito_compra, name='carrito'),
		#url(r'^carrito/(?P<articulo>\d+)/(?P<cantidad>\d+)', views.actualizar_cookie),
		#url(r'^carrito/', views.carrito, name='carrito'),

    ]
    
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
