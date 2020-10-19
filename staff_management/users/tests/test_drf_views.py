import pytest
from django.test import RequestFactory

from staff_management.users.api.views import UserViewSet
from staff_management.users.models import User

pytestmark = pytest.mark.django_db


class TestUserViewSet:
    def test_get_queryset(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        assert user in view.get_queryset()

    def test_me(self, user: User, rf: RequestFactory):
        view = UserViewSet()
        request = rf.get("/fake-url/")
        request.user = user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "id": user.id,
            "email": user.email,
            "full_name": user.full_name,
            "url": f"http://testserver/api/users/{user.id}/",
        }
