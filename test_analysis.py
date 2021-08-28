import json
import pytest
import speaker_data from analysis

file_data = [json.load(open('./332.json', 'r'))]

@pytest.fixture
def speakers():
    return speaker_data(file_data)

def test_speaker_data(speakers):
    
    assert 1 == 1