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
			
	@intent_handler(IntentBuilder("").require("plan").optionally("going").optionally("Suggest"))
	def handle_start_game_intent(self, message):
		self.speak_dialog("start")

		# get lower bound
		lowerBound = self.get_numerical_response("get.lower")
		# get upper bound
		upperBound = self.get_numerical_response("get.upper")

		answer = self.speak(lowerBound, upperBound)
# 		userGuess = lowerBound - 1
# 		while userGuess != answer:
# 			userGuess = self.get_numerical_response("guess")
# 			if userGuess < answer:
# 				self.speak_dialog("too.low")
# 			elif userGuess > answer:
# 				self.speak_dialog("too.high")
# 		self.speak_dialog("correct")

	def stop(self):
# 		lowerBound, upperBound = 0, 100
# 		answer = 0
# 		userGuess = answer
# 		return True
		pass

def create_skill():
	return NumberGuessSkill()
