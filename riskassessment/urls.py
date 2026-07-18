from django.urls import path

from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="home"),
    path(
        "information-centre/",
        views.information_centre,
        name="information-centre",
    ),
    path("read-more-1/", views.readmore1, name="readmore1"),
    path("read-more-2/", views.readmore2, name="readmore2"),
    path("read-more-3/", views.readmore3, name="readmore3"),
    path("read-more-4/", views.readmore4, name="readmore4"),
    path("read-more-5/", views.readmore5, name="readmore5"),
    path("read-more-6/", views.readmore6, name="readmore6"),
]