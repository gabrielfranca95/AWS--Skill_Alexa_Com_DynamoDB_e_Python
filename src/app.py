from ask_sdk_core.skill_builder import CustomSkillBuilder
from src.services.storage import get_persistence_adapter
from src.handlers.launch import LaunchRequestHandler, HasMemoryLaunchRequestHandler
from src.handlers.capture import CaptureRecordIntentHandler
from src.handlers.help import HelpIntentHandler
from src.handlers.cancel_stop import CancelOrStopIntentHandler
from src.handlers.session_ended import SessionEndedRequestHandler
from src.handlers.error import IntentReflectorHandler, CatchAllExceptionHandler
from src.utils.logger import get_logger

# Initialize Logger
logger = get_logger(__name__)

# Initialize Skill Builder with DynamoDB Persistence
sb = CustomSkillBuilder(persistence_adapter=get_persistence_adapter())

# Register Handlers
sb.add_request_handler(HasMemoryLaunchRequestHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureRecordIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last

# Register Exception Handler
sb.add_exception_handler(CatchAllExceptionHandler())

# Expose Lambda Handler
lambda_handler = sb.lambda_handler()
