import logging
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class CaptureRecordIntentHandler(AbstractRequestHandler):
    """Handler for Capture Record Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureRecordIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        desconhece = slots["desconhece"].value

        attributes_manager = handler_input.attributes_manager
        
        current_attributes = {
            "desconhece": desconhece,
        }

        attributes_manager.persistent_attributes = current_attributes
        attributes_manager.save_persistent_attributes()

        speak_output = 'uhmmmmmmmmm, entendi que {desconhece} .'.format(desconhece=desconhece)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )
