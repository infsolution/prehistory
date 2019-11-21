from django.urls import path
from game import views
urlpatterns = [
	path('usuario/', views.UserList.as_view(), name = views.UserList.name),
	path('usuario/<int:pk>/', views.UserDetail.as_view(), name = views.UserDetail.name),
	path('avatar/', views.AvatarList.as_view(), name = views.AvatarList.name),
	path('avatar/<int:pk>/', views.AvatarDetail.as_view(), name = views.AvatarDetail.name),
	path('knowing/', views.KnowingList.as_view(), name = views.KnowingList.name),
	path('knowing/<int:pk>/', views.KnowingDetail.as_view(), name = views.KnowingDetail.name),
	path('item/', views.ItemList.as_view(), name = views.ItemList.name),
	path('item/<int:pk>/', views.ItemDetail.as_view(), name = views.ItemDetail.name),
	path('avatarknowing/', views.AvatarKnowingList.as_view(), name =  views.AvatarKnowingList.name),
	path('avatarknowing/<int:pk>/',views.AvatarKnowingDetail.as_view(), name = views.AvatarKnowingDetail.name),
	path('avataritem/', views.AvatarItemList.as_view(), name =  views.AvatarItemList.name),
	path('avataritem/<int:pk>/',views.AvatarItemDetail.as_view(), name = views.AvatarItemDetail.name),
	path('logado/', views.CustomObtainAuthToken.as_view(), name=views.CustomObtainAuthToken.name),
]
