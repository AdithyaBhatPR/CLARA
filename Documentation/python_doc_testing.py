# from Documentation.python_documentation import if_statement
# from Documentation.python_documentation import else_statement
# from Documentation.python_documentation import elif_statement
# from Documentation.python_documentation import python_nested_if_statements
# from Documentation.python_documentation import range_function
# from Documentation.python_documentation import break_and_continue_statements_and_else_clauses_on_loops
# from Documentation.python_documentation import while_loop
# from Documentation.python_documentation import for_loop
# from Documentation.python_documentation import list_doc
from Documentation.python_documentation import *
#import sys
from gtts import gTTS
import os
from playsound import playsound

def if_statement_func():
	print(if_statement['definition'])
	speak = "The brief definition of if is."
	speak += if_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about if statement ?')
	print('The subcategories available are :')
	dict_keys = list(if_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in IF that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",if_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

#if_statement_func()

def else_statement_func():
	print(else_statement['definition'])
	speak = "The brief definition of else statement is."
	speak += else_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about else statement ?')
	print('The subcategories available are :')
	dict_keys = list(else_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in ELSE that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",else_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

#else_statement_func()


def elif_statement_func():
	print(elif_statement['definition'])
	speak = "The brief definition of elif statement is."
	speak += elif_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about elif statement ?')
	print('The subcategories available are :')
	dict_keys = list(elif_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in ELIF that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",elif_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

# elif_statement_func()

def python_nested_if_statements_func():
	print(python_nested_if_statements['definition'])
	speak = "The brief definition of nested if statements is."
	speak += python_nested_if_statements['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about nested if statement ?')
	print('The subcategories available are :')
	dict_keys = list(python_nested_if_statements.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in Nested IF that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",python_nested_if_statements[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

# python_nested_if_statements_func()
def range_function_func():
	print(range_function['definition'])
	speak = "The brief definition of range inbuilt function is."
	speak += range_function['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about range function ?')
	print('The subcategories available are :')
	dict_keys = list(range_function.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in range that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",range_function[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


# python_nested_if_statements_func()
def break_and_continue_statements_and_else_clauses_on_loops_func():
	speak = "What would you like to know about from the categories mentioned below."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	print('What would you like to know about break and continue statements and else clauses on loops ?')
	print('The subcategories available are :')
	dict_keys = list(break_and_continue_statements_and_else_clauses_on_loops.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",break_and_continue_statements_and_else_clauses_on_loops[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def while_loop_func():
	print(while_loop['definition'])
	speak = "The brief definition of while loop is."
	speak += while_loop['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about while loop ?')
	print('The subcategories available are :')
	dict_keys = list(while_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in while loop that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",while_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


def for_loop_func():
	print(for_loop['definition'])
	speak = "The brief definition of for loop is."
	speak += for_loop['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about for loop ?')
	print('The subcategories available are :')
	dict_keys = list(for_loop.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in FOR loop that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",for_loop[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
	
def list_doc_func():
	print(list_doc['definition'])
	speak = "The brief definition of list data structure is."
	speak += list_doc['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about list ?')
	print('The subcategories available are :')
	dict_keys = list(list_doc.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in list that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",list_doc[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def return_func():
	print(return_statement['definition'])
	speak = "The brief definition of return expressions is."
	speak += return_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about return statement ?')
	print('The subcategories available are :')
	dict_keys = list(return_statement.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in return that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",return_statement[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

def operator_function():
	speak = "Providing categories of operator supported in C programming language."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print("Select the type of operator about which you want to read in detail :\n")
	dict_keys = list(operator_entity.keys())[1:]
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory of operator that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",operator_entity[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')

###Functions to handle variables in python 
def variables_in_python():
	print("Local Variables:")
	speak = "Displaying about the local variables."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	print("\n-----------------------------------------------------------------------\n")
	print(local_variable['contents'])
	print("\n-----------------------------------------------------------------------\n")

	print("Global Variables:")
	speak = "Displaying about the global variables."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	print("\n-----------------------------------------------------------------------\n")
	print(global_variable['contents'])
	print("\n-----------------------------------------------------------------------\n")

	print("Non-local variable:")
	speak = "Displaying about the non-local variables."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	print("\n-----------------------------------------------------------------------\n")
	print(nonlocal_variables['contents'])
	print("\n-----------------------------------------------------------------------\n")

### To display the list of all the documentations available
def available_documentation():
	all_doc = ['if statement','else statement','elif statement','nested if statement','range function','break and continue statements and else clauses on loops','while loop','for loop',
	'list data structure','return statement']
	for i in range(len(all_doc)):
		print(i+1,': ',all_doc[i])

### Just returning the list of documentations
def documentation_list():
	all_doc = ['if statement','else statement','elif statement','nested if statement','range function','break and continue statements and else clauses on loops','while loop','for loop',
	'list data structure','return statement']

	return all_doc
