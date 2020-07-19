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


class ArticleField:
    """The `ArticleField` class for the Advanced Requirements."""

    def __init__(self, field_type: typing.Type[typing.Any]):
        pass


class Article:
    """The `Article` class you need to write for the qualifier."""

    def __init__(self, title: str, author: str, publication_date: datetime.datetime, content: str):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.content = content

    def __repr__(self):
        return f'<Article title="{self.title}" author=\'{self.author}\' publication_date=\'{self.publication_date.isoformat()}\'>'

    def __len__(self):
        return len(self.content)

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
