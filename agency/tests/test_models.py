from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.models import Newspaper, Topic


class RedactorModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        get_user_model().objects.create(
            username="test",
            password="test1234",
            years_of_experience="2"
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.get(id=1)
        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_get_absolute_url(self):
        redactor = get_user_model().objects.get(id=1)
        self.assertEqual(
            redactor.get_absolute_url(), "/redactor/1/"
        )


class TopicModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        Topic.objects.create(
            name="test_name",
        )

    def test_topic_str(self):
        topic = Topic.objects.get(id=1)
        self.assertEqual(
            str(topic),
            f"{topic.name}"
        )


class NewspaperModelTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        topic = Topic.objects.create(
            name="test_name",
        )
        redactor = get_user_model().objects.create(
            username="test",
            password="test1234",
            years_of_experience="2"
        )
        newspaper = Newspaper.objects.create(
            model="test_model",
            topic=topic
        )
        newspaper.redactors.add(redactor)

    def test_newspaper_str(self):
        newspaper = Newspaper.objects.get(id=1)
        self.assertEqual(str(newspaper), newspaper.title)
