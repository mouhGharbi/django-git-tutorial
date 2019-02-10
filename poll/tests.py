import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question


class QuestionTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.deltatime(days=30)
        future_question = Question(question_published_date=time,
                                   question_content="for testing")
        self.assertIs(future_question.was_published_recently(), False)
# Create your tests here.
