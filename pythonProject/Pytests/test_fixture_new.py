import pytest

from Pytests.conftest import test_giving_data
from Pytests.Baseclass import Test_Logger

@pytest.mark.usefixtures('test_giving_data')
class Test_getter(Test_Logger):
    def test_getter(self, test_giving_data):
        log = self.test_logger()
        log.info(test_giving_data[0])
        print(test_giving_data[1])

