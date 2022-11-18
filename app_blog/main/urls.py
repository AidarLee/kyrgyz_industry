from django.urls import path
from . import views
urlpatterns = [
        path('', views.index, name='index'),
        path('accounts/login/', views.login_page, name='login_page'),
        path('accounts/login/success/', views.authorization, name='authorizate'),
        path('accounts/logout/', views.logout_page, name = 'logout_page'),
        path('detail/', views.detail, name='detail'),
        path('admin-panel/main/', views.admin_index_page, name='admin_panel'),
        # News View
        path('admin-panel/news/all/', views.NewsListView.as_view(), name='news_all'),
        path('admin-panel/news/create/', views.NewsCreateView.as_view(), name='news_create'),
        path('admin-panel/news/detail/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
        path('admin-panel/news/update/<int:pk>/', views.NewsUpdateView.as_view(), name='news_update'),
        path('admin-panel/news/delete/<int:id>/', views.news_delete, name='news_delete'),
        
        # News Gallery View
        path('admin-panel/gallery/news/', views.NewsGalleryListView.as_view(), name='newsgallery_all'),
        path('admin-panel/gallery/news/create/', views.NewsGalleryCreateView.as_view(), name='newsgallery_create'),
        path('admin-panel/gallery/news/update/<int:pk>/', views.NewsGalleryUpdateView.as_view(), name='newsgallery_update'),
        path('admin-panel/gallery/news/delete/<int:id>/', views.newsgallery_delete, name='newsgallery_delete'),
        
        # News Image View
        path('admin-panel/image/news/', views.NewsImageListView.as_view(), name='newsimage_all'),
        path('admin-panel/image/news/create/', views.NewsImageCreateView.as_view(), name='newsimage_create'),
        path('admin-panel/image/news/update/<int:pk>/', views.NewsImageUpdateView.as_view(), name='newsimage_update'),
        path('admin-panel/image/news/delete/<int:id>/', views.newsimage_delete, name='newsimage_delete'),
        
        # Contests View
        path('admin-panel/contests/', views.ContestListView.as_view(), name='contests_all'),
        path('admin-panel/contests/create/', views.ContestCreateView.as_view(), name='contests_create'),
        path('admin-panel/contests/update/<int:pk>/', views.ContestUpdateView.as_view(), name='contests_update'),
        path('admin-panel/contests/delete/<int:id>/', views.contests_delete, name='contests_delete'),
        
        # Project-Image View
        path('admin-panel/image/projects/', views.ProjectImageListView.as_view(), name='projectimage_all'),
        path('admin-panel/image/projects/create/', views.ProjectImageCreateView.as_view(), name='projectimage_create'),
        path('admin-panel/image/projects/update/<int:pk>/', views.ProjectImageUpdateView.as_view(), name='projectimage_update'),
        path('admin-panel/image/projects/delete/<int:id>/', views.projectimage_delete, name='projectimage_delete'),
        
        # Project-Gallery View
        path('admin-panel/gallery/projects/', views.ProjectGalleryListView.as_view(), name='projectgallery_all'),
        path('admin-panel/gallery/projects/create/', views.ProjectGalleryCreateView.as_view(), name='projectgallery_create'),
        path('admin-panel/gallery/projects/update/<int:pk>/', views.ProjectGalleryUpdateView.as_view(), name='projectgallery_update'),
        path('admin-panel/gallery/projects/delete/<int:id>/', views.projectgallery_delete, name='projectgallery_delete'),
        
        # Projects View
        path('admin-panel/projects/', views.ProjectListView.as_view(), name='projects_all'),
        path('admin-panel/projects/create/', views.ProjectCreateView.as_view(), name='projects_create'),
        path('admin-panel/projects/update/<int:pk>/', views.ProjectUpdateView.as_view(), name='projects_update'),
        path('admin-panel/projects/delete/<int:id>/', views.projects_delete, name='projects_delete'),
]
