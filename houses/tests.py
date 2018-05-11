from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from houses.models import Fraternity

# Create your tests here.
class ModelTests(TestCase):

    def setUp(self):
        self.test_f = Fraternity.objects.create(
            english_name="TEST FULL NAME",
            nickname="TEST_NICKNAME",
            letters=SimpleUploadedFile("TEST_LETTERS", b"\x00\x01\x02\x03"),
            primary_color="#FFFFFF",
            secondary_color="#000000"
        )

    def test_lower_representation(self):
        """
        Test to see if the function correctly converts the english name to a
        lower representation
        """
        self.assertEqual(self.test_f.lower_repr(), 'testfullname')