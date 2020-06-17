import logging
import ask_sdk_core.utils as ask_utils
import os
from ask_sdk_s3.adapter import S3Adapter
s3_adapter = S3Adapter(bucket_name=os.environ["S3_PERSISTENCE_BUCKET"])

from ask_sdk_core.skill_builder import CustomSkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "olá, eu não me recordo de ter aprendido algo ainda.\
        o que deseja que eu aprenda ?"
        reprompt_text = "diga: alexa, comece ensine frases! para ouvir o que\
        eu aprendi!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )

class HasMemoryLaunchRequestHandler(AbstractRequestHandler):
    """Handler for launch after they have set their birthday"""

    def can_handle(self, handler_input):
        # extract persistent attributes and check if they are all present
        attr = handler_input.attributes_manager.persistent_attributes
        attributes_are_present = ("desconhece" in attr)

        return attributes_are_present and ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        attr = handler_input.attributes_manager.persistent_attributes
        desconhece = attr['desconhece']
        #aprendido = attr['aprendido'] # month is a string, and we need to convert it to a month index later
        #mais = attr['maisfrase']

        # TODO:: Use the settings API to get current date and then compute how many days until user's bday
        # TODO:: Say happy birthday on the user's birthday

        speak_output = "eu aprendi que {desconhece} .".format(desconhece=desconhece)
        handler_input.response_builder.speak(speak_output)

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask"add a reprompt if you want to keep the session open for the user to respond")
                .response
        )

class CaptureRecordIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("CaptureRecordIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        desconhece = slots["desconhece"].value
        #aprendido = slots["aprendido"].value
        #maisfrase = slots["maisfrase"].value

        attributes_manager = handler_input.attributes_manager

        birthday_attributes = {
            "desconhece": desconhece,
            #"aprendido": aprendido,
            #"maisfrase": maisfrase,
        }

        attributes_manager.persistent_attributes = birthday_attributes
        attributes_manager.save_persistent_attributes()

        speak_output = 'uhmmmmmmmmm, entendi que {desconhece} .'.format(desconhece=desconhece)#, aprendido=aprendido)
        #reprompt_text= "a última coisa que me recordo de ter aprendido, foi que {desconhece}.".format(desconhece=desconhece)

        return (
            handler_input.response_builder
                .speak(speak_output)
                #.ask(reprompt_text)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Para me ensinar uma frase, é bem simples. \
        Utilize as palavras: alexa, comece ensine frases, aprenda que o sol está bonito! E pronto. \
        quando Você pedir, eu irei repetir a frase, o sol está bonito! Ah, e se quiser que eu diga esta \
        frase novamente? é só dizer, alexa, comece ensine frases! e eu irei dizer sempre a ultima frase\
        aprendida."
        reprompt_text=" se ainda estiver com dúvidas, para me ensinar a primeira frase, é só dizer \
        alexa, comece ensine frases. aguarde para que eu peça que me ensine uma frase.\
        depois disto é só dizer: aprenda que o sol está bonito! e eu direi que o sol está bonito. logo após, \
        sempre que quiser me ensinar uma frase nova, é só dizer: alexa, comece ensine frases e aprenda que \
        flores são bonitas. e eu guardarei que flores são bonitas. a frase que quiser me ensinar deve ser seguida\
        de, aprenda que. dessa forma eu vou conseguir guardar diversas frases que for me ensinando ao longo do tempo."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(reprompt_text)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Adeus!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "Você acabou de acionar " + intent_name + "."

        return (
            handler_input.response_builder
                .speak(speak_output)
                # .ask("add a reprompt if you want to keep the session open for the user to respond")
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> bool
        return True

    def handle(self, handler_input, exception):
        # type: (HandlerInput, Exception) -> Response
        logger.error(exception, exc_info=True)

        speak_output = "Desculpe, tive problemas para fazer o que você pediu. Por favor, tente novamente."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.


sb = CustomSkillBuilder(persistence_adapter=s3_adapter)

sb.add_request_handler(HasMemoryLaunchRequestHandler())
sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(CaptureRecordIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler()) # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()