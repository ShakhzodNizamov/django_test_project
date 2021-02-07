from django.urls import path

from . import views

urlpatterns = [
    path("", views.MainPage.as_view()),
    path('new_post/', views.CreatePostPage.as_view(), name='new_post_page'),
    path('detail/<int:post_id>/', views.PostDetailPage.as_view(), name='detail'),
    path('add_post/<str:username>/', views.AddPost.as_view(), name='add_post'),
    path('add_comment/<int:post_id>/', views.AddComment.as_view(), name='add_comment'),
    # path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    # path("search/", views.Search.as_view(), name='search'),
    # path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    # path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    # path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
]