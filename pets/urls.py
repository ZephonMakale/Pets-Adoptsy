from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from posts.views import index, blog, post, search, post_create, post_update, post_delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index),
    path('blog/', blog, name = 'post_list'),
    path('search/', search, name = 'search'),
    path('create/', post_create, name = 'post-create'),
    path('post/<id>/', post, name = 'post_details'),
    path('post/<id>/update/', post_update, name = 'post-update'),
    path('post/<id>/delete/', post_delete, name = 'post-delete'),
    path('tinymce/', include('tinymce.urls'))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)