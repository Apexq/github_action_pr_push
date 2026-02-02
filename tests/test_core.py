from gh_actions_demo.core import slugify, word_count


def test_slugify_basic() -> None:
    assert slugify("Merhaba Dünya!") == "merhaba-dunya"


def test_slugify_strips_dashes() -> None:
    assert slugify("---Hello---") == "hello"


def test_word_count() -> None:
    assert word_count("Merhaba   Dünya!") == 2
