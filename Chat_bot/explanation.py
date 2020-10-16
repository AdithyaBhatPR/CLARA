#Linking the entities identified with the explanation to provide from documentation

import pyttsx3

# initialisation 
engine = pyttsx3.init()

#Customizing properties
engine.setProperty('voice', 'english+f4')
engine.setProperty('rate', 150)

def recognise_and_explain(entities, lang):
	if lang == 'c':
		from Documentation.doc_testing import if_statement_func, else_statement_func,array_doc_func
		#from Documentation.doc_testing import *
	elif lang == 'py':
		from Documentation.python_doc_testing import if_statement_func, else_statement_func, elif_statement_func, python_nested_if_statements_func, for_loop_func
		from Documentation.python_doc_testing import range_function_func,break_and_continue_statements_and_else_clauses_on_loops_func, while_loop_func, list_doc_func
		#from Documentation.python_doc_testing import *
	#print(entities)

	## Creating dictionary of entity as key and function call as value
	try:
		entity_func_dict = {'elif':elif_statement_func, 'else': else_statement_func,
						 'for':for_loop_func, 'if':if_statement_func, 'nested_if':python_nested_if_statements_func,
						 'range':range_function_func,'break_and_continue_statements_and_else_clauses_on_loops':break_and_continue_statements_and_else_clauses_on_loops_func,
						 'while':while_loop_func, 'list':list_doc_func, 'array':array_doc_func}

		### Include entities return, variable, operator

		print("From the query obtained, the keyterms recognized are:")
		engine.say("From the query obtained, the keyterms recognized are.....")
		for i in range(len(entities)):
			entities[i] = (entities[i].split(':')[0]).replace('_entity', '')
			print(i+1,':=',entities[i])
			engine.say(entities[i])

		engine.runAndWait()
		engine.say("To strengthen the conceptual understanding with these programming terminologies,")
		engine.say("it is suggested that you go through the detailed explanation of these.")
		engine.runAndWait()
		#print(entities)
		reading = 1
		while(reading):
			for entity in entities:
				print("\nTo continue reading about,",entity,"Press 1, else press any key to continue :\n")
				reply = input()
				if reply == '1':
					entity_func_dict[entity]()
			print("\nIf you would like to revisit the keywords recognised to read it out,press 1, else press 0 to exit\n")
			engine.say("If you would like to revisit the recoginsed keyterm explanation ,press 1, else press 0 to exit")
			engine.runAndWait()
			reading = int(input())

		print("\n***Happing Learning***\n")
		engine.say("Have a Good day. Happy learning and coding")
		engine.runAndWait()

	except Exception as err:
		print("Exception arose is,",err)
		


