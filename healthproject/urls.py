from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # accounts
    path("", include("accounts.urls", namespace="accounts")),
    # profiles
    path("profile/", include("profiles.urls", namespace="profiles")),
    # plans
    path("plans/", include("plans.urls", namespace="plans")),
    # coaches
    path("coaches/", include("coaches.urls", namespace="coaches")),
    # workoutbank
    path("workouts/", include("workoutbank.urls", namespace="workouts")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
