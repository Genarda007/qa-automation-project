# QA Automation Project

Automated UI testing project built with Python, Pytest, and Playwright using the SauceDemo application.

## Test Coverage

* Valid login
* Invalid login (negative test)
* Locked out user (negative test)
* Inventory page title verification
* Add item to cart

## Project Structure

* `pages/` — Page Object Model classes
* `tests/` — Test cases
* `conftest.py` — Pytest fixtures
* `pytest.ini` — Pytest configuration

## Tech Stack

* Python
* Pytest
* Playwright

## Installation

```bash
pip install -r requirements.txt
playwright install
```

## Run Tests

```bash
pytest
```

## Generate HTML Report

```bash
pytest --html=report.html --self-contained-html
```

## Results

Current test suite:

* 5 tests passing
* Cross-browser automation ready
* Page Object Model design pattern implemented

