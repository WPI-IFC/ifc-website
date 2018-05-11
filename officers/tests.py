from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.utils.timezone import now

from officers.models import Biography,Blog, Post
# Create your tests here.

class ViewTesting(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="testU", password="test123")
        self.blog = Blog.objects.create(
            current_owner=self.user,
            position_title="TEST_POSITION",
            slug="test-slug"
        )
        self.post = Post.objects.create(
            blog=self.blog,
            published=now(),
            last_edit=now(),
            author=self.user,
            author_string=self.user.username,
            title="TEST_POST_TITLE 1",
            body="TEST POST BODY 1"
        )
        self.client = Client()
        self.client.login(username="testU", password="test123")

    def test_post_authoring(self):
        data = {
            'title': "TEST_POST_TITLE 2",
            'body': "TEST POST BODY 2"
        }

        self.client.post("/about/officer/{}/new/".format(self.blog.slug), data)

        posts = Post.objects.all().filter(author=self.user)
        self.assertEqual(posts.count(), 2)

    def test_unauthorized_post_authoring(self):
        """
        Error if the user tries to make a post to a blog that does
        not belong to them.
        """
        User.objects.create_user(username="bad_user", password="test123")
        self.client.login(username="bad_user", password="test123")

        data = {
            'title': "TEST_POST_TITLE 2",
            'body': "TEST POST BODY 2"
        }

        response = self.client.post("/about/officer/{}/new/".format(self.blog.slug), data)
        self.assertEqual(response.status_code, 403)

        posts = Post.objects.all().filter(author=self.user)
        self.assertEqual(posts.count(), 1)

    def test_post_editing(self):
        data = {
            'title': "TEST_POST_TITLE 1.5",
            'body': "TEST POST BODY 1.5"
        }

        self.client.post("/about/officer/{}/{}/edit/".format(
            self.post.blog.slug,
            self.post.id
        ), data)

        updated_post = Post.objects.get(id=self.post.id)
        self.assertGreater(updated_post.last_edit, self.post.published)
        self.assertEquals(updated_post.title, data['title'])
        self.assertEqual(updated_post.body, data['body'])

    def test_unauthorized_edits(self):
        User.objects.create_user(username="bad_user", password="test123")
        self.client.login(username="bad_user", password="test123")

        data = {
            'title': "TEST_POST_TITLE 1.5",
            'body': "TEST POST BODY 1.5"
        }

        response = self.client.post("/about/officer/{}/{}/edit/".format(
            self.post.blog.slug,
            self.post.id
        ), data)
        self.assertEqual(response.status_code, 403)

        updated_post = Post.objects.get(id=self.post.id)
        self.assertEqual(updated_post.last_edit, self.post.published)
        self.assertNotEqual(updated_post.title, data['title'])
        self.assertNotEqual(updated_post.body, data['body'])