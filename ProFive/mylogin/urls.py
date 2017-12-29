from django.conf.urls import url
from mylogin import views
# from django.contrib import admin

app_name = 'mylogin'

urlpatterns = [
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.user_login,name='user_login'),
    # url(r'^admin/', admin.site.urls),
]
