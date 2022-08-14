import pytest
import yaml


class TestDate:

    @pytest.mark.parametrize(('a', 'b'), yaml.safe_load(open("./TestS1/TestOne/data.yaml")))
    def test_date(self, a, b):
        print(a + b)
