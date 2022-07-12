import pytest
@pytest.fixture(autouse=True, scope="function")
def setup():
    print("You can start right here")
    yield
    print("Let end this now")

@pytest.fixture(scope="session")
def db():
    return 1

def test_use_fixture_1(setup, db):
    print(db)
    assert db == 2

def test_use_fixture_2(setup, db):
    print(db)
    assert db == 2

