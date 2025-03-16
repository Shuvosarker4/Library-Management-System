from rest_framework.routers import SimpleRouter
from library.views import BookViewSet,AuthorViewSet,BorrowRecordViewSet,MemberViewSet
from django.urls import path,include

router = SimpleRouter()
router.register('books',BookViewSet,basename='book-list')
router.register('authors',AuthorViewSet,basename='author-list')
router.register('borrow',BorrowRecordViewSet,basename="borrow-list")
router.register('members',MemberViewSet,basename='member-list')

urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
