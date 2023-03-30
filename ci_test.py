import pytest

@pytest.fixture
def x(request):
    x = 1
    def fin():
        x = None
    request.addfinalizer(fin)
    return x

def test_addition(x):
    assert x + 1 == 2
