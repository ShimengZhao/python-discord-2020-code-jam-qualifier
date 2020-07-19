"""
Use this file to write your solution for the Summer Code Jam 2020 Qualifier.

Important notes for submission:

- Do not change the names of the two classes included below. The test suite we
  will use to test your submission relies on existence these two classes.

- You can leave the `ArticleField` class as-is if you do not wish to tackle the
  advanced requirements.

- Do not include "debug"-code in your submission. This means that you should
  remove all debug prints and other debug statements before you submit your
  solution.
"""
import datetime
import typing
import re
from collections import Counter
from functools import total_ordering


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        self.field_type = field_type
        self.attribute_name = None

    def __get__(self, instance, owner):
        val = instance.__dict__[self.attribute_name]
        return val

    def __set__(self, instance, value):
        if not issubclass(type(value), self.field_type):
            raise TypeError(
                f"expected an instance of type '{self.field_type.__name__}' for attribute '{self.attribute_name}', got '{type(value).__name__}' instead")
        else:
            instance.__dict__[self.attribute_name] = value

    def __set_name__(self, owner, name):
        self.attribute_name = name


@total_ordering
class Article:
    """The `Article` class you need to write for the qualifier."""
    __latest_id = -1

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        Article.__latest_id += 1

        self.title = title
        self.author = author
        self.publication_date = publication_date
        self._content = content
        self.id = Article.__latest_id
        self.last_edited = None

    def __repr__(self):
        return f'<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.publication_date.isoformat()}\'>'

    def __len__(self):
        return len(self.content)

    def __eq__(self, other):
        return self.publication_date == other.publication_date

    def __lt__(self, other):
        return self.publication_date < other.publication_date

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value
        self.last_edited = datetime.datetime.now()

    def short_introduction(self, n_characters: int) -> str:
        raw_characters = self.content[:n_characters + 1]
        if n_characters == 0:
            return ""
        else:
            if raw_characters[-1] == " " or raw_characters[-1] == "\n":
                return raw_characters[:-1]
            else:
                while len(raw_characters) > 0:
                    if raw_characters[-1] == " " or raw_characters[-1] == '\n':
                        return raw_characters[:-1]
                    raw_characters = raw_characters[:-1]
                return ""

    def most_common_words(self, n_words: int) -> dict:
        word_list = re.findall(r'\w+', self.content.lower())
        result = Counter(word_list).most_common(n_words)
        return dict(result)
