from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from houses.models import Fraternity
from houses.forms import HouseForm

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


class FormTests(TestCase):

    def setUp(self):
        self.form_data = {
            "english_name": "Sigma Pi",
            "primary_color": "#000000",
            "secondary_color": "#111111",
        }

    def test_non_google_link(self):
        self.form_data["calendar_link"] = "https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#IFRAME"
        form = HouseForm(self.form_data)
        self.assertFalse(form.is_valid())

    def test_simple_malicious_xss(self):
        calendar_string = ('https://calendar.google.com/calendar/embed?src=TEST%40gmail.com&ctz=America%2FNew_York'
                            '"</iframe><IFRAME SRC="javascript:alert(\'XSS\');"></IFRAME>'
                            '"<iframe src="abc.com')
        self.form_data["calendar_link"] = calendar_string
        form = HouseForm(self.form_data)
        self.assertFalse(form.is_valid())

    def test_simple_success(self):
        self.form_data["calendar_link"] = "https://calendar.google.com/calendar/embed?src=TEST%40gmail.com&ctz=America%2FNew_York"
        form = HouseForm(self.form_data)
        self.assertTrue(form.is_valid())
