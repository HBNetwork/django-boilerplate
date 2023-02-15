import pytest


@pytest.mark.djangodb
class TestCaseExample:
    def test_example(self):
        assert 2 == 1 + 1
