from django.urls import path
from page.views import (
    home_view,
    about_us_view,
    contact_us_view,
    vision_view,
    page_view
)

urlpatterns = [
    path('',home_view,name='home'),
    # path('hakkimizda/',about_us_view,name='about_us'),
    # # path('iletisim/',contact_us_view,name='contact_us'),
    # path("vizyonumuz/", vision_view,name='vision'),
    path('<slug:slug>/',page_view),
]