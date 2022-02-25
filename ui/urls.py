from django.urls import path
from .views import (
    NearReportAPIView, NearReportListAPIView,
    NearSolvedReportListAPIView, MyReportListAPIView
)

urlpatterns = [
    path("main/", NearReportAPIView.as_view()),
    path("report_list/", NearReportListAPIView.as_view()),
    path("my_report_list/", MyReportListAPIView.as_view()),
    path("solved_report_list/", NearSolvedReportListAPIView.as_view()),
]