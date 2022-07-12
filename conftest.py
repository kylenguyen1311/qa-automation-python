import pytest
@pytest.hookimpl()
def pytest_sessionstart():
    print("let's start now")

def pytest_sessionfinish():
    print("let's end this now")
