from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
# from staff_management.applicant.views import ApplicantCreateView #, ApplicantDetailsView 
from staff_management.applicant.views import ApplicantUpdateView, applicant_detail_view ,ApplicantUserListView,ApplicantUserJsonView

app_name = "applicant"
urlpatterns = [
    # path("detail/<int:id>", view=ApplicantCreateView.as_view(), name="detail"),
    path("update/", view=ApplicantUpdateView.as_view(), name="update"),
    path("detail/<int:id>/", view=applicant_detail_view, name="detail"),
	re_path(r'^app-user-list/', ApplicantUserListView.as_view(), name='app-user-list'),
	re_path(r'^appuser-list-json/$', ApplicantUserJsonView.as_view(), name='appuser-list-json'),

]


if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
