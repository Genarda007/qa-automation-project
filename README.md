![Tests](https://github.com/Genarda007/qa-automation-project/actions/workflows/tests.yml/badge.svg)

# QA Automation Project

A Playwright + pytest automation framework targeting [Saucedemo.com](https://www.saucedemo.com), built using Page Object Model architecture.

## Tech Stack
- Python 3
- Playwright
- pytest
- pytest-html
- Page Object Model (POM)
- GitHub Actions CI/CD

## Project Structure
## Test Coverage
| Test | Type | Marker |
|---|---|---|
| Valid login | Positive | Smoke |
| Invalid login | Negative | Smoke |
| Locked out user | Negative | Regression |
| Inventory title | Positive | Regression |
| Add item to cart | Positive | Regression |
| Multiple users login (3 users) | Data-driven | Regression |

## How to Run

### Setup
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### Run all tests
```bash
pytest tests/ -v
```

### Run smoke tests only
```bash
pytest tests/ -v -m smoke
```

### Run with HTML report
```bash
pytest tests/ -v --html=reports/report.html --self-contained-html
```

## Defects Found
See [defect_log.md](defect_log.md) for documented bugs found during exploratory testing.

## CI/CD
Tests run automatically on every push to main via GitHub Actions.