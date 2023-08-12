from django.urls import path
from .views import (AllNoutbooksView,
                    DetailNoutbooksView,
                    UpdateNoutbooksView,
                    CreatedNoutbookView,
                    DeletedNoutbookView,
                    GetByApiView,
                    GetCustomer)


urlpatterns = [
    path('get_all/',AllNoutbooksView.as_view(),name='AllNoutbooks'),
    path('get_by_id/<int:id>/',DetailNoutbooksView.as_view(),name='DetailNoutbooks'),
    path('update/<int:id>/',UpdateNoutbooksView.as_view(),name='UpdateNoutbooksView'),
    path('created/',CreatedNoutbookView.as_view(),name='CreatedNoutbookView'),
    path('delete/<int:id>/',DeletedNoutbookView.as_view(),name='DeletedNoutbookView'),
    path('search/',GetByApiView.as_view(),name='GetByApiView'),
    path('get_all_customer/',GetCustomer.as_view(),name='get_all_customer'),
]