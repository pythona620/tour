from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG, getLogger

from random import randint

__author__ = 'prasad'
LOGGER = getLogger(__name__)

class NumberGuessSkill(MycroftSkill):
	def get_numerical_response(self, dialog):
		while True:
			val = self.get_response(dialog)	
			return val
	@intent_handler(IntentBuilder("").require("plan").optionally("going").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start")
		# get lower bound
		source = self.get_numerical_response("get.source")
		# get upper bound
		destination = self.get_numerical_response("get.destination")
		answer =(source + destination)
		self.speak(answer)

	def stop(self):
		pass

def create_skill():
	return NumberGuessSkill()
