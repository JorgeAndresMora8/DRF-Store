from django.urls import path
from watchlist_app.api.views import ProductListAV, ProductDetailAV, CategoryListAV, CategoryDetailAV, ReviewList, ReviewDetail, CreateReview
urlpatterns = [
    path('list/', ProductListAV.as_view(), name='product-list'), 
    path('<int:pk>/', ProductDetailAV.as_view(), name='product-detail'),
    path('category/', CategoryListAV.as_view(), name='category-list'), 
    path('category/<int:pk>', CategoryDetailAV.as_view(), name='category-detail'), 
    
    path("<int:pk>/review-create", CreateReview.as_view(), name=""),
    path('<int:pk>/review', ReviewList.as_view(), name='review-list'), 
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
]