from django.urls import path
from .views import ProfileView, ChangePasswordView, AddArticleView, PublishedPostsView, ArticleDeleteView, DraftPostsView, RejectedPostsView, InvestigationPostsView, EditArticleView

urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('add-article/', AddArticleView.as_view(), name='add_article'),
    path('edit-article/<int:pk>/', EditArticleView.as_view(), name='edit_article'),
    path('published-posts/', PublishedPostsView.as_view(), name='published_posts'),
    path('draft-posts/', DraftPostsView.as_view(), name='draft_posts'),
    path('rejected-posts/', RejectedPostsView.as_view(), name='rejected_posts'),
    path('investigation-posts/', InvestigationPostsView.as_view(), name='investigation_posts'),
    path('articles/delete/<int:pk>/', ArticleDeleteView.as_view(), name='article-delete'),
]
