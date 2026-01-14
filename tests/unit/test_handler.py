import pytest
import sys
import os
from unittest.mock import MagicMock, patch

# Ensure src is in path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from ask_sdk_model import RequestEnvelope, User, Session, Context
from ask_sdk_core.handler_input import HandlerInput

# Mock the storage before importing app, or patch it
# We'll patch get_persistence_adapter to return a mock to avoid AWS calls

@patch('src.services.storage.get_persistence_adapter')
def test_launch_request(mock_get_adapter):
    # Setup mock adapter
    mock_adapter = MagicMock()
    mock_get_adapter.return_value = mock_adapter
    
    # Import app after patching
    from src.app import lambda_handler
    
    # Create a mock event
    event = {
        "session": {
            "new": True,
            "sessionId": "SessionId",
            "application": {"applicationId": "AppId"},
            "user": {"userId": "UserId"},
        },
        "request": {
            "type": "LaunchRequest",
            "requestId": "RequestId",
            "timestamp": "2020-01-01T00:00:00Z",
            "locale": "pt-BR"
        },
        "context": {
            "System": {
                "application": {"applicationId": "AppId"},
                "user": {"userId": "UserId"},
                "device": {"supportedInterfaces": {}}
            }
        },
        "version": "1.0"
    }

    # Since HasMemoryLaunchRequestHandler tries to read attributes, 
    # we need the mock adapter to behave nicely or the attributes manager to return something.
    context = {}
    
    # Invoke lambda
    response = lambda_handler(event, context)
    
    # Verify response
    assert response is not None
    assert "response" in response
    assert "outputSpeech" in response["response"]
    assert "ssml" in response["response"]["outputSpeech"]
    # We expect the basic welcome because we aren't mocking the persistence content to show 'HasMemory' flow
    # The HasMemory handler checks attributes, if the mock adapter returns empty, it falls through to LaunchRequestHandler
    assert "não me recordo de ter aprendido algo ainda" in response["response"]["outputSpeech"]["ssml"]
