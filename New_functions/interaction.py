#Importing module which performs casual interaction with the user(can add more interactions)
from New_functions.bot_conversation import RecognizeSpeech_during_interaction
from gtts import gTTS
import sys
from playsound import playsound

def conversation(entities, lang):
	try:
		language = 'en'
		rate = False
		if lang == 'c':
			prog_lang = "C language"
			from Documentation.doc_testing import if_statement_func, else_statement_func,array_doc_func,for_loop_func, operator_function
			from Documentation.doc_testing import while_loop_func, break_and_continue_func,return_func, available_documentation
			#Importing functions relevant to variables
			from Documentation.doc_testing import variable_func, local_variable_func, global_variable_func, static_variable_func, automatic_variable_func, external_variable_func
			entity_func_dict = {'else': else_statement_func,'if':if_statement_func,'array':array_doc_func, 
				'for':for_loop_func, 'while':while_loop_func, 'break and continue statements':break_and_continue_func,
				'return':return_func, 'operator':operator_function, 'variables':variable_func}

		elif lang == 'py':
			prog_lang = "Python"
			from Documentation.python_doc_testing import if_statement_func, else_statement_func, elif_statement_func, python_nested_if_statements_func, for_loop_func,available_documentation
			from Documentation.python_doc_testing import range_function_func,break_and_continue_statements_and_else_clauses_on_loops_func, while_loop_func, list_doc_func, return_func, operator_function
			entity_func_dict = {'elif':elif_statement_func, 'else': else_statement_func,
							 'for':for_loop_func, 'if':if_statement_func, 'nested if':python_nested_if_statements_func,
							 'range':range_function_func,'break and continue statements and else clauses on loops':break_and_continue_statements_and_else_clauses_on_loops_func,
							 'while':while_loop_func, 'list':list_doc_func,'return':return_func, 'operator':operator_function}
		status = 0
		for entity in entities:
			print("Would you like to read about",entity,"keyword")
			speak = "Would you like to read about..." + entity + "keyword"
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			
			playsound('wit_bot.mp3', True)
			print("\n***Please speak now...\n")
			response =  RecognizeSpeech_during_interaction('myspeech.wav', 6)
			if response:
				if (response[0] == 'Agree' or response[1] == 'on') and (response[0] != 'Disagree'):
					if entity in list(entity_func_dict.keys()):
						speak = "Great!, we have got some explanation for you"
						speech_obj = gTTS(text = speak, lang = language, slow=rate)
						speech_obj.save('wit_bot.mp3')
						
						playsound('wit_bot.mp3', True)
						
						print("\n****************************************************\n")
						entity_func_dict[entity]()
						print("\n****************************************************\n")

						### For variables there are multiple functions to be called as per user preference
						if lang == 'c' and entity == 'variables':
							# Storing the functions to different variable categories
							categories = [local_variable_func, global_variable_func, static_variable_func, automatic_variable_func, external_variable_func]
							print("\n***Note : There are categories of variables supported in",prog_lang,"press 1 to read about them, else press any key to continue")
							reply = input()
							while(reply == '1'):
								print("Select the variable category about which you want to read:")
								print("1. Local variables")
								print("2. Global variables")
								print("3. Static variables")
								print("4. Automatic variables")
								print("5. External variables")
								category = int(input())
								categories[category-1]()
								print("\nTo revisit variable categories press 1, else press any key to exit from variable categories :")
								reply = input()
					else:
						print("Sorry we don't have related documentation for",entity,"keyword")
						speak = "Sorry!...We don't have related documentation for," + entity + "keyword."
						speak += ".It would be great if you could refer to the official" + prog_lang + "documentation and search for this programming keyterm"	
						speech_obj = gTTS(text = speak, lang = language, slow=rate)
						speech_obj.save('wit_bot.mp3')
						
						playsound('wit_bot.mp3', True)
						print("\n***The list of all the available documentations are : ")
						available_documentation()

				else:
					speak = "Exiting the bot, have a good day and happy coding"
					speech_obj = gTTS(text = speak, lang = language, slow=rate)
					speech_obj.save('wit_bot.mp3')
					
					playsound('wit_bot.mp3', True)
					sys.exit("\n***Happy Coding***\n")

			print("\nIf you would like to revisit the keywords recognised or read further about other possible recognised terms,press 1, else press 0 to exit\n")
			speak = "To revisit the keywords recognised for explanation,press 1, else press 0 to exit"
			speech_obj = gTTS(text = speak, lang = language, slow=rate)
			speech_obj.save('wit_bot.mp3')
			
			playsound('wit_bot.mp3', True)
			status = int(input())
			if status == 0:
				break
		return status
	except Exception as err:
		print("Exception arose is ", err)