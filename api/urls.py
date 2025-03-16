from rest_framework.routers import SimpleRouter
from library.views import BookViewSet,AuthorViewSet,BorrowRecordViewSet,MemberViewSet

router = SimpleRouter()
router.register('books',BookViewSet,basename='book-list')
router.register('authors',AuthorViewSet,basename='author-list')
router.register('borrow',BorrowRecordViewSet,basename="borrow-list")
router.register('members',MemberViewSet,basename='member-list')

urlpatterns = router.urls
