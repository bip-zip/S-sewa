
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth.urls')),
    path('articles/', include('articles.urls')),
    path('records/', include('records.urls')),
]



from django.contrib import admin

admin.site.site_header = 's-sewa'                    # default: "Django Administration"
admin.site.index_title = 's-sewa'                 # default: "Site administration"
admin.site.site_title = 's-sewa adminsitration' # default: "Django site admin"

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)