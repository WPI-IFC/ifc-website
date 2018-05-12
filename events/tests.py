from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import now
from django.contrib.auth.models import Permission, User
from django.urls import reverse

from houses.models import Fraternity
from officers.models import Blog
from events.models import OfficerEvent, HouseEvent

# Create your tests here.
class ViewTests(TestCase):

    def setUp(self):
        self.house = Fraternity.objects.create(
            english_name="TEST FULL NAME",
            nickname="TEST_NICKNAME",
            letters=SimpleUploadedFile("TEST_LETTERS", b"\x00\x01\x02\x03"),
            primary_color="#FFFFFF",
            secondary_color="#000000"
        )
        content_type = ContentType.objects.get_for_model(Fraternity)
        permission = Permission.objects.create(
            codename="TEST FULL NAME",
            name="TEST FULL NAME",
            content_type=content_type
        )
        self.house_user = User.objects.create_user(username="testU", password="test123")
        self.house_user.user_permissions.add(permission)

        self.client.login(username="testU", password="test123")

    def test_only_create_own(self):
        """
        Only alow a Fraternity to make events for itself
        """
        wrong_house = Fraternity.objects.create(
            english_name="TEST FULL NAME TWO",
            nickname="TEST_NICKNAME2",
            letters=SimpleUploadedFile("TEST_LETTERS", b"\x00\x01\x02\x03"),
            primary_color="#FFFFFF",
            secondary_color="#000000"
        )

        data = {
            "title": "Test Event",
            "d_time": now(),
            "description": "aaaaaaaaa",
            "splash_img": SimpleUploadedFile("TEST_SPLASH", b"\x00\x01\x02\x03")
        }

        response = self.client.post(reverse("event-chapter-new", args=(wrong_house.lower_repr(),)), data)
        self.assertEqual(response.status_code, 403)

        self.assertEqual(HouseEvent.objects.all().count(), 0)
