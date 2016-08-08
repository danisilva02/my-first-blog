from django.conf.urls import url
from blog import views

urlpatterns = [
    url(r'^$', views.home, name='blog.home'),
    #url(r'/category/(?P<category_id>\d+)', views.show_post_category, name='blog.post_by_categoty'),
    url(r'(?P<slug>[\w-]+)/$', views.show_post_detalhe, name='blog.show_post_detalhe'),
]