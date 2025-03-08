from django.contrib import admin
from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", include("hello.urls")),
    path('admin/', admin.site.urls),

	#path("hello/<name>", views.hello_there, name="hello_there")

]

urlpatterns += staticfiles_urlpatterns()
