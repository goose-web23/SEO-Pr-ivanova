from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView
from . import views
from venue.sitemaps import StaticViewSitemap, HallSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "halls": HallSitemap,
}
app_name = "venue"

urlpatterns = [
    path("", views.home, name="home"),


    path("home/", views.home, name="home_duplicate"),

    path("halls/", views.hall_list, name="hall_list"),
    # SEO-ЗАДАНИЕ (ЧПУ): замените <int:pk> на <slug:slug> (см. venue/models.py)
    path("halls/<int:pk>/", views.hall_detail, name="hall_detail"),
    path("halls/<slug:slug>/", views.hall_detail, name="hall_detail"),
    
    path("menu/", views.menu, name="menu"),
    path("events/", views.events, name="events"),
    path("afisha/", views.poster_list, name="poster_list"),
    # SEO-ЗАДАНИЕ (ЧПУ): и здесь <int:pk> → <slug:slug>
    path("afisha/<int:pk>/", views.poster_detail, name="poster_detail"),
    path("afisha/<slug:slug>/", views.poster_detail, name="poster_detail"),
    path("gallery/", views.gallery, name="gallery"),
    path("contacts/", views.contacts, name="contacts"),
    path("booking/", views.booking, name="booking"),

    path(
        'robots.txt',
        TemplateView.as_view(template_name='robots.txt', content_type='text/plain'),
        name='robots',
    ),
    path(
        "sitemap.xml",
        sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
]
