#Fixture
import pytest

@pytest.fixture
def setup():
    print("I setup from same file")
    return "pass"

def test_initialCheck(setup):
    assert setup == "pass"

@pytest.mark.skip
def test_initialCheck2(preSetupWork):
    assert preSetupWork == "fail"