import pytest
@pytest.fixture
def setup():
    print("You can start right here")
    yield
    print("Let end this now")

def test_use_fixture(setup):
    assert 1==1
