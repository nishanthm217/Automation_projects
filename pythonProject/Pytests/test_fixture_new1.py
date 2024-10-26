import pytest

@pytest.mark.fixture("givingData")
class Test_get_params:
    def test_get_params(self,givingData):
        print(givingData[1])