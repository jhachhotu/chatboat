

class ChatbotEngine:
    def __init__(self, intent_classifier, handlers: dict):
        self.intent_classifier = intent_classifier
        self.handlers = handlers

    def process(self, message):
        """
        message: Message object
        """
        intent = self.intent_classifier.classify(message.text)

        handler = self.handlers.get(intent)
        if not handler:
            return "Sorry, I didn't understand your request."

        return handler.handle(message)
