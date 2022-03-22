from django.urls import path

from account.views import (
    account_view,
    edit_account_view,
    edit_profile_image_view,
    crop_image,
)

app_name = 'account'

urlpatterns = [
    path('<user_id>/', account_view, name="view"),
    path('<user_id>/edit/', edit_account_view, name="edit"),
    path('<user_id>/edit_profile_image', edit_profile_image_view, name="edit_image"),
    path('<user_id>/edit/cropImage/', crop_image, name="crop_image"),
]
