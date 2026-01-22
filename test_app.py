from app import add
from app import mul


def test_add():
    assert add(2, 3) == 5

def test_mul():
    assert mul(2, 3) == 6