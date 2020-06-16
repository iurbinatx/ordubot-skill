from mycroft import MycroftSkill, intent_file_handler


class Ordubot(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('ordubot.intent')
    def handle_ordubot(self, message):
        self.speak_dialog('ordubot')


def create_skill():
    return Ordubot()

