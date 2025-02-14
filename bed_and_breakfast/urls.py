"""
URL configuration for bed_and_breakfast project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path, include

from application.views.CategoryView import CategoryView
from application.views.SubInfoView import PolicyViews, ContactViews
from application.views.BnbInfoView import BnbInfoView
from application.views.LoginView import AuthView, ForgetPasswordHandler
from application.views.HomeView import HomeView
from application.views.ResultView import ResultView
from application.views.BookView import BookView, HandleNewReview
from application.views.UserView import UserView, UserInfoView, UserOrderHistoryView, UserViewedHistoryView, \
    UserReviewHistoryView, UserWishListView, UpdateUserView
from application.views.LogoutView import logout_view
from application.views.AddNewBnb import AddNewBnb
from application.views.RegisterView import RegisterView
from application.views.OwnerManagementView import OwnerManagementView, UpdateBnBView, AcceptBookingView, \
    UpdateStatusBnBView
from application.views.InfoOwnerBnBView import InfoOwnerBnBView

# Lưu ý: Nếu muốn hiển thị các trang lỗi custom thì phải set DEBUG = False và phải set ALLOWED_HOSTS
# (Trong môi trường dev thì hãy đặt ALLOWED_HOSTS = ["localhost"])
# Xem https://docs.djangoproject.com/en/5.1/ref/views/#django.views.defaults.page_not_found
# Xem định nghĩa default các public url ở .venv/Lib/django/conf/urls/__init__.py

handler400 = 'application.views.ErrorView.get_error_400_page'
handler403 = 'application.views.ErrorView.get_error_403_page'
handler404 = 'application.views.ErrorView.get_error_404_page'
handler500 = 'application.views.ErrorView.get_error_500_page'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name=''),
    path('rooms/<int:bnbid>', BnbInfoView.as_view(), name='product'),
    path('categories/<str:category_name>', CategoryView.as_view(), name='category'),
    path('privacy/', PolicyViews.as_view(template_name='other_template/privacy-policy.html'), name='privacy-policy'),
    path('terms-of-use/', PolicyViews.as_view(template_name='other_template/terms.html'), name='terms-of-use'),
    path('policy/', PolicyViews.as_view(template_name='other_template/other-policy.html'), name='terms-of-use'),
    re_path(r'^(?P<type>login|register|forgot-password)/$', AuthView.as_view(), name='auth'),
    path('about-us/', ContactViews.as_view(template_name='other_template/about-us.html'), name='about-us'),
    path('contact/', ContactViews.as_view(template_name='other_template/contact-us.html'), name='contact-us'),
    path('result/<str:query>', ResultView.as_view(), name='result'),
    path('book/', BookView.as_view(), name='book'),
    path('user/', UserView.as_view(), name='user'),
    path('user/user-information/', UserInfoView.as_view(template_name='user/user-information.html'), name='user-info'),
    path('user/order-history/', UserOrderHistoryView.as_view(template_name='user/user-order-history.html'),
         name='user-order-history'),
    path('user/viewed-history/', UserViewedHistoryView.as_view(template_name='user/user-viewed-history.html'),
         name='user-viewed-history'),
    path('user/review-history/', UserReviewHistoryView.as_view(template_name='user/user-reviewed-history.html'),
         name='user-review-history'),
    path('user/wishlist/', UserWishListView.as_view(template_name='user/user-wishlist.html'), name='user-wishlist'),
    path('user/update/',UpdateUserView.as_view(),name='user-update'),
    path('logout/', logout_view, name='logout'),
    path('user/wishlist', UserWishListView.as_view(template_name='user/user-wishlist.html'), name='user-wishlist'),
    path('post-new-booking/', HandleNewReview.as_view(), name='handle-new-booking'),
    path('owner-management/', OwnerManagementView.as_view(), name='owner-management'),
    path('owner-management/dashboard',
         OwnerManagementView.as_view(template_name='manage_of_owner/owner-management-dashboard.html'),
         name='owner-management-dashboard'),
    path('owner-management/info-owner',
         OwnerManagementView.as_view(template_name='manage_of_owner/info-owner-bnb.html'),
         name='owner-management-info-owner'),
    path('owner-management/edit-bnb/id=<int:bnbid>',
         OwnerManagementView.as_view(template_name='manage_of_owner/form-bnb.html'),
         name='owner-management-edit-bnb'),
    path('owner/<int:ownerid>', InfoOwnerBnBView.as_view(), name='info-owner'),

    # Các URL dưới đây chỉ được dùng cho POST AJAX
    path('owner-management/edit-bnb/update-bnb', UpdateBnBView.as_view(), name='owner-management-update-bnb'),
    path('owner-management/accept-booking', AcceptBookingView.as_view(), name='owner-management-accept-booking'),
    path('owner-management/update-status-bnn', UpdateStatusBnBView.as_view(),
         name='owner-management-update-status-bnn'),
    path('add-new-bnb/', AddNewBnb.as_view(), name='add-new-bnb'),
    path('validate-register/<str:type>', RegisterView.as_view(), name='validate-register'),
    path('request-forgot-password/', ForgetPasswordHandler.as_view(), name='request-forgot-password'),

]
