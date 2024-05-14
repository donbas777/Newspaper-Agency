from django.contrib.auth import get_user_model
from django.test import TestCase

from agency.forms import (
    NewspaperSearchForm,
    RedactorCreationForm,
    RedactorSearchForm,
    TopicSearchForm,
)


class FormTests(TestCase):
    def setUp(self):
        self.test_user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234",
        )

    def test_redactor_creation_form(self):
        form = RedactorCreationForm(
            data={
                "username": "test_username",
                "password1": "test_password",
                "password2": "test_password",
                "years_of_experience": "3",
                "first_name": "test_first",
                "last_name": "test_last"
            }
        )
        self.assertTrue(form.is_valid())

    def test_redactor_search_form(self):
        form = RedactorSearchForm(
            data={
                "username": "test_username"
            }
        )
        self.assertTrue(form.is_valid())

    def test_newspaper_search_form(self):
        form = NewspaperSearchForm(
            data={
                "title": "test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_topic_search_form(self):
        form = TopicSearchForm(
            data={
                "name": "Test"
            }
        )
        self.assertTrue(form.is_valid())
