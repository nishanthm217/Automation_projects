import pytest
from conftest import test_giving
@pytest.mark.usefixtures("test_giving")
class Test_baseclass:
    pass

