import json
import pytest
from analysis import Conversation

file_data = json.load(open('./332.json', 'r'))

@pytest.fixture
def conversation():
    return Conversation(file_data)

def test_speaker_data(conversation):
    conversation_data = conversation.data
    assert conversation.title == 'Metropolitan Area Planning Commission Demo Conversation'
    assert conversation_data['Jess']['num_words'] == 1820
    assert conversation_data['Jess']['duration'] == 936.3000000000006

# TODO: Add test for query with multiple files