# GitHub Actions Demo (Python)

Bu repo, GitHub Actions'ı öğrenmek için küçük bir Python proje örneğidir:

- `pytest` ile test
- `ruff` ile lint/format
- `mypy` ile type-check
- GitHub Actions ile PR/push'ta otomatik CI
- Ek olarak cron ile scheduled workflow

## Lokal çalıştırma

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -e ".[dev]"
pytest
ruff check .
mypy src
```

## CLI örnekleri

```powershell
gh-actions-demo slugify "Merhaba Dünya!"
gh-actions-demo wc "Merhaba Dünya!"
```
