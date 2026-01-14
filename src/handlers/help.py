import ask_sdk_core.utils as ask_utils
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_model import Response

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
