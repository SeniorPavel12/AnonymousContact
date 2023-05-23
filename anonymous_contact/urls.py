"""anonymous_contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('community/', include('community.urls')),
    path('discussion/', include('discussion.urls')),
    path('user/', include('my_user.urls')),
    path('', include('various.urls')),
]

#это то что выводит print(admin_site.urls) (т.e здесь так то представление вроде есть(<URLPattern 'add_post/' [name='add_post']>))
'''[<URLPattern '' [name='index']>, <URLPattern 'login/' [name='login']>, <URLPattern 'logout/' [name='logout']>, <URLPattern 'password_change/' [name='password_change']>, <URLPattern 'password_change/done/' [name='password_change_done
']>, <URLPattern 'autocomplete/' [name='autocomplete']>, <URLPattern 'jsi18n/' [name='jsi18n']>, <URLPattern 'r/<int:content_type_id>/<path:object_id>/' [name='view_on_site']>, <URLResolver <URLPattern list> (None:None) 'discussion/
post/'>, <URLPattern '^(?P<app_label>discussion)/$' [name='app_list']>, <URLPattern '(?P<url>.*)$'>, <URLPattern 'add_post/' [name='add_post']>]'''



