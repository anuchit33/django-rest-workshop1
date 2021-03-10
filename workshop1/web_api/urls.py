from django.conf.urls import url, include
from django.conf import settings

from web_api.views import (
    UserList,
)


urlpatterns = [
    url(r'^user/$', UserList.as_view(),name="user-list"),    
]
