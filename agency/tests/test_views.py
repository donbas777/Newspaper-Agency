from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from agency.models import Redactor, Topic, Newspaper

INDEX_URL = reverse("agency:index")
TOPIC_URL = reverse("agency:topic-list")
NEWSPAPER_URL = reverse("agency:newspaper-list")
REDACTOR_URL = reverse("agency:redactor-list")


class PublicTest(TestCase):
    def test_index_login_required(self):
        res = self.client.get(INDEX_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_newspaper_login_required(self):
        res = self.client.get(NEWSPAPER_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_topic_login_required(self):
        res = self.client.get(TOPIC_URL)
        self.assertNotEquals(res.status_code, 200)

    def test_redactor_login_required(self):
        res = self.client.get(REDACTOR_URL)
        self.assertNotEquals(res.status_code, 200)


class PrivateTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test1",
            password="test1234",
        )
        self.client.force_login(self.user)

    def test_retrieve_topic(self):
        Topic.objects.create(
            name="test1",
        )
        Topic.objects.create(
            name="test2",
        )
        topics = Topic.objects.all()
        response = self.client.get(TOPIC_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "agency/topic_list.html")

    def test_retrieve_newspaper(self):
        topic = Topic.objects.create(
            name="test",
        )
        Newspaper.objects.create(
            title="test1",
            topic=topic
        )
        Newspaper.objects.create(
            title="test2",
            topic=topic
        )
        newspapers = Newspaper.objects.all()
        response = self.client.get(NEWSPAPER_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["newspaper-list"]), list(newspapers))
        self.assertTemplateUsed(response, "agency/newspaper_list.html")

    def test_retrieve_redactors(self) -> None:
        get_user_model().objects.create_user(
            username="test123",
            password="test1234",
            years_of_experience="3",
        )
        get_user_model().objects.create_user(
            username="test1234",
            password="test1234",
            years_of_experience="1",
        )
        redactors = Redactor.objects.all()
        response = self.client.get(REDACTOR_URL)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["redactor_list"]), list(redactors))
        self.assertTemplateUsed(response, "agency/redactor_list.html")
