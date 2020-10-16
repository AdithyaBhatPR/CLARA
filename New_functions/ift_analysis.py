#Effective detailed ift feedback implementation and conditional expressions
#also provide comparison for some test case between correct implementation output and incorrect implementation output

import sys
from New_functions.documenting import conditional_statement, ift_explanation, boolean
from Documentation.doc_testing import if_statement_func, else_statement_func
from Documentation.python_doc_testing import if_statement_func, else_statement_func, elif_statement_func, python_nested_if_statements_func
##Voice based interaction imports
from New_functions.bot_conversation import RecognizeSpeech_during_interaction
from New_functions.operator_analysis import explain_in_brief
from gtts import gTTS
from playsound import playsound

def ift_feedback(clara_feedback,cleaned_feedback, ins,args, lang):
	print(ift_explanation.__doc__)
	speak = "The brief explanation of if-then-else is."
	speak += ift_explanation.__doc__
	speak += "Please select your option for any further explanation required."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print("\n----------------------------------------------------------------\n")
	print("1 : Brief explanation\n") ##Brief explanation provides same as bot
	print("2 : Detailed complete explanation\n")
	print("3 : To look at repair directly\n")
	print("Enter the option number to select, else any other key to continue : ")
	reply = input()
	reply_1 = '0'
	if reply == '1':
		print("\n------------------------------------------------------------------------------------\n")
		print(ift_explanation.__doc__)
		speak = "As it's control flow depends on the evaluation of the condition specified."
		speak += "Which is evaluated in conditional expressions.Read about conditional statements below"
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		print("\n------------------------------------------------------------------------------------\n")
		print("Defining Conditional statements :\n")
		print(conditional_statement.__doc__)
		print("\n------------------------------------------------------------------------------------\n")
		print("Press 1 if you need detailed explanation, else press any key to continue\n")
		reply_1 = input()
	if reply == '2' or reply_1 == '1':
		if lang == 'c':
			print("\n---------------------------------------------------------------------------------------------------\n")
			if_statement_func()
			print("\n\n***Continue reading about else keyword***\n\n")
			else_statement_func()
			print("\n---------------------------------------------------------------------------------------------------\n")
		elif lang == 'py':
			print("1 : IF statements")
			print("2 : ELSE statements")
			print("3 : ELIF statements")
			print("4 : Nested IF statements")
			print("Choose one of the options from above, to continue reading about it, else press 0 to quit reading :")
			try:		
				choice = input()
				while(choice != '0'):
					print("\n---------------------------------------------------------------------------------------------------\n")
					if choice == '1':
						if_statement_func()
					elif choice == '2':
						else_statement_func()
					elif choice == '3':
						elif_statement_func()
					elif choice == '4':
						python_nested_if_statements_func()
					else:
						print('Invalid choice, choose one from above options')
					print("\nSelect from the options below if you wish to read more, else 0 to quit\n")
					print("1 : IF statements")
					print("2 : ELSE statements")
					print("3 : ELIF statements")
					print("4 : Nested IF statements")
					choice = input()
					print("\n---------------------------------------------------------------------------------------------------\n")
			except exception as err:
				print("Exception arosed is :", err)

	if reply == '3':
		print(cleaned_feedback,"\n")
		print("****************************************************\n")
		speak = "Have a look at the generated repair for your program"
		speech_obj = gTTS(text = speak, lang = 'en', slow=False)
		speech_obj.save('wit_bot.mp3')
		playsound('wit_bot.mp3', True)
		return 

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
	while(talk != 3):
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
			if(talk < 2):
				speak = "Sorry...couldn't interpret your response or record your voice, please try again."
			else:
				speak = "Sorry...couldn't interpret your response or record your voice."

			speech_obj = gTTS(text = speak, lang = 'en', slow=False)
			speech_obj.save('wit_bot.mp3')
			playsound('wit_bot.mp3', True)
			#Increment to consider the chances taken up
			talk += 1

def incorrect_conditional_exp(clara_feedback, ins, args):
	print("\n---------------------------------------------------------------------------------------------------\n")
	print("\nLooks like you have used incorrect conditional expression.\n")
	print("\n---------------------------------------------------------------------------------------------------\n")
	speak = "Looks like you have used incorrect conditional expression."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	explain_in_brief("conditional expression", conditional_statement.__doc__)

	speak = "Conditional expressions evaluate to boolean type."
	print("\nConditional expressions evaluate to boolean type.\n")
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	explain_in_brief("boolean expression",boolean.__doc__)
	### To implement a wait based on user preference, have considered user giving their preference as input
	### that is making it more user pase
	print("Press 1 to continue with possibly any further related repairs, else press 0 to exit")
	reply = input()
	if reply == '0':
		print("*** Happy Coding!!! ***\n")
		return 0
	return
