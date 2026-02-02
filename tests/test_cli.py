from gh_actions_demo.cli import main


def test_cli_slugify(capsys) -> None:
    rc = main(["slugify", "Merhaba Dünya!"])
    assert rc == 0
    assert capsys.readouterr().out.strip() == "merhaba-dunya"


def test_cli_wc(capsys) -> None:
    rc = main(["wc", "Merhaba Dünya!"])
    assert rc == 0
    assert capsys.readouterr().out.strip() == "2"
