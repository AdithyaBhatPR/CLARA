#interactive feedback for operator errors
#Challenge to give a good explanation and reason behind the operator error occured, would like to look at 
#test case output for giving comparison between change in output with operator change
from New_functions.documenting import arithmetic_op, relational_op
### Importing voice based dependencies
from New_functions.bot_conversation import RecognizeSpeech_during_interaction
import time
from gtts import gTTS
from playsound import playsound

### Function used in common to take user preference 
def explain_in_brief(category, documentation):
	speak = "Would You like to go through brief explanation of "+ category+".or just continue without reading."
	speak += "Please give your preference now."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')

	print("Would You like to go through brief explanation of",category,"or just continue without reading\n")
	playsound('wit_bot.mp3', True)
	talk = 1
	spoke = 0
	# Giving user 3 chances to speak out incase it wasn't recorded properly
	while(talk != 4):
		if(spoke):
			speak = "Please tell your preference response now."
			speech_obj = gTTS(text = speak, lang = 'en', slow=False)
			speech_obj.save('wit_bot.mp3')
			playsound('wit_bot.mp3', True)

		spoke = 1
		print("\n***Please speak now...\n")
		reply =  RecognizeSpeech_during_interaction('myspeech.wav', 6)
		if reply:
			if (reply[0] == 'Agree' or reply[1] == 'on') and (reply[0] != 'Disagree'):
				speak += "Providing brief explanation."
				print("Go through this brief explanation of",category)
				print("\n------------------------------------------------------------------------------------\n")
				print(documentation)
				#return_explanation()
				print("\n------------------------------------------------------------------------------------\n")

				speak = documentation
				speech_obj = gTTS(text = speak, lang = 'en', slow=False)
				speech_obj.save('wit_bot.mp3')
				playsound('wit_bot.mp3', True)
				break
			else:
				break
		else:
			print("Sorry, couldn't interpret your response or record your voice")
			if(talk < 3):
				speak = "Sorry...couldn't interpret your response or record your voice, please try again."
			else:
				speak = "Sorry...couldn't interpret your response or record your voice."

			speech_obj = gTTS(text = speak, lang = 'en', slow=False)
			speech_obj.save('wit_bot.mp3')
			playsound('wit_bot.mp3', True)
			#Increment to consider the chances taken up
			talk += 1
	return

def feedback_comp_operator(segments, operator,clara_feedback,cleaned_feedback,ins, args):
	op = operator.split(' (')[1].split(')')[0]
	if op in segments[0]:
		speak = "Looks like you have used an incorrect relational operator, or this operator might not be required."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		print("Looks like you have used an incorrect relational operator, or this operator might not be required.")
		playsound('wit_bot.mp3', True)
		###Calling function to take user preference
		explain_in_brief("relational operator", relational_op.__doc__)

		print("\n------------------------------------------------------------------------------------")
		speak = "Providing more details about error."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("The operator you have used is :", operator)
		print("Because of this the conditional expression is incorrectly evaluated and led to incorrect output")
		print("------------------------------------------------------------------------------------\n")

		#provide better explanation for reason behind this
	else:
		print("\n------------------------------------------------------------------------------------")
		speak = "Providing more details about error here."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("There is a requirement for a comparison operation to be performed between operands, for expression to be evaluated as True or False.")
		print("The relational operator required is :", operator)
		print("------------------------------------------------------------------------------------\n")
		time.sleep(5)
		###Calling function to take user preference
		explain_in_brief("relational operator", relational_op.__doc__)

	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = input()
	if (reply == '1'):
		speak = "The repair generated for incorrect expression is."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("\nThe feedback generated is : ")
		print(cleaned_feedback, "\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_arth_operator(segments,operator,clara_feedback,cleaned_feedback, ins, args): #depending on whether args passed or ins passed use accordingly one of them will be None
	op = operator.split(' (')[1].split(')')[0]
	if op in segments[0]:
		speak = "Looks like you have used an incorrect arithmetic operator, or this operator might not be required."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		print("Looks like you have used an incorrect arithmetic operator, or this operator might not be required.")
		playsound('wit_bot.mp3', True)
		###Calling function to take user preference
		explain_in_brief("arithmetic operator", arithmetic_op.__doc__)

		print("\n------------------------------------------------------------------------------------")
		speak = "Providing more details about error."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("The incorrect operator used in program is :", operator)
		print("------------------------------------------------------------------------------------\n")

		#provide better explanation for reason behind this
	else:
		print("\n------------------------------------------------------------------------------------")
		speak = "Providing more details about error here."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("There is a requirement for an",operator,"operation to be performed at the specified location")
		print("------------------------------------------------------------------------------------\n")
		time.sleep(5)
		###Calling function to take user preference
		explain_in_brief("arithmetic operator", arithmetic_op.__doc__)

	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = input()
	if (reply == '1'):
		speak = "The repair generated for incorrect expression is."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("\nThe feedback generated is : ")
		print(cleaned_feedback,"\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_logic_operator(segments, operator, clara_feedback,cleaned_feedback,ins, args):
	if operator in segments[0]:
		print("Looks like you have used an incorrect logical operator")
		print("The incorrect operator used in program is :", operator)
	else:
		print("A logical operation is to be performed by the operator :",operator)
	#provide better explanation for reason behind this
	print("\nPress 1 to look at the repair generated, else press 0 to exit")
	reply = input()
	if (reply == '1'):
		speak = "The repair generated for incorrect expression is."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("\nThe feedback generated is : ")
		print(cleaned_feedback,"\n")
		print("****************************************************\n")
	else:
		print("*** Happy Coding!!! ***\n")
		return 0

def feedback_incorrect_value(n1, n2, clara_feedback,cleaned_feedback,ins, args):
	speak = "Looks like you have used incorrect constant value."
	speak += ".Go through the details mentioned below."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	print("Looks like you have used incorrect constant value")
	playsound('wit_bot.mp3', True)

	print("\n------------------------------------------------------------------------------------")
	print("Literal :",n1,",might have been assigned to a variable or used as one of the operand")
	print("This might be one of the reason for incorrect output")
	print("It is suggested that you analyze the expression")
	print("\n------------------------------------------------------------------------------------")
	#provide better explanation for reason behind this
	print("\nPress 1 to continue once you are done reading.")
	done = input()
	if(done == '1'):
		print("\n------------------------------------------------------------------------------------")
		print("You can look at clara generated repair or prefer to quit, if you wish to debug on own")
		print("Please tell your preference now.")
		speak = "You can look at clara generated repair or prefer to quit, if you wish to debug on own"
		speak += ".Please tell your preference now."
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		talk = 1
		spoke = 0
		# Giving user 3 chances to speak out incase it wasn't recorded properly
		while(talk != 4):
			if(spoke):
				speak = "Please give your response now."
				speech_obj = gTTS(text = speak, lang = 'en', slow=False)
				speech_obj.save('wit_bot.mp3')
				playsound('wit_bot.mp3', True)

			spoke = 1
			print("\n***Please speak now...\n")
			reply =  RecognizeSpeech_during_interaction('myspeech.wav', 6)
			if reply:
				if (reply[0] == 'Agree' or reply[1] == 'on') and (reply[0] != 'Disagree'):
					speak = "The repair generated for incorrect expression is."
					speech_obj = gTTS(text = speak, lang = 'en', slow=False)
					speech_obj.save('wit_bot.mp3')
					playsound('wit_bot.mp3', True)
					print(cleaned_feedback,"\n")
					print("****************************************************\n")
					return 
				else:
					print("*** Happy Coding!!! ***\n")
					return 0
			else:
				print("Sorry, couldn't interpret your response or record your voice")
				if(talk < 3):
					speak = "Sorry...couldn't interpret your response or record your voice, please try again."
				else:
					speak = "Sorry...couldn't interpret your response or record your voice."

				speech_obj = gTTS(text = speak, lang = 'en', slow=False)
				speech_obj.save('wit_bot.mp3')
				playsound('wit_bot.mp3', True)
				#Increment to consider the chances taken up
				talk += 1
	print("\n------------------------------------------------------------------------------------")
