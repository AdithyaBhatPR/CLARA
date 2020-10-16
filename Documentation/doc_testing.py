# from Documentation.c_documentation import if_statement
# from Documentation.c_documentation import else_statement
# from Documentation.c_documentation import array_doc
from Documentation.c_documentation import *
# import sys
### Using google text to speech
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

def array_doc_func():
	print(array_doc['definition'])
	speak = "The brief definition of array data structure is."
	speak += array_doc['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about array  ?')
	print('The subcategories available are :')
	dict_keys = list(array_doc.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in array that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",array_doc[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')


def for_loop_func():
	print(for_loop['definition'])
	speak = "The brief definition of for loop expression is."
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
		

def while_loop_func():
	print(while_loop['definition'])
	speak = "The brief definition of while loop expression is."
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
	

def break_and_continue_func():
	# print("Definition of break keyword :\n",break_and_continue['definition of break'])
	# speak = "The brief definition of break and continue keywords are."
	# speak += "Defintion of Break."
	# speak += break_and_continue['definition of break']
	# print("Definition of continue keyword :\n", break_and_continue['defintion of continue'])
	# speak += "Now providing definition of continue"
	# speak += break_and_continue['defintion of continue']
	# speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	# speech_obj.save('wit_bot.mp3')
	# #os.system("mpg123 wit_bot.mp3")
	# playsound('wit_bot.mp3', True)

	speak = "What would you like to know about from the categories mentioned below."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)
	print('What would you like to know about break and continue ?')
	print('The subcategories available are :')
	dict_keys = list(break_and_continue.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",break_and_continue[dict_keys[response-1]])
		elif response == 0:
			return 
		else:
			print('Invalid response')
		

def return_func():
	print(return_statement['definition'])
	speak = "The brief definition of return expression is."
	speak += return_statement['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	#os.system("mpg123 wit_bot.mp3")
	playsound('wit_bot.mp3', True)

	print('What would you like to know about return statements?')
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

### Functions handling the variables documentation in the c programming language

def variable_func():
	print("Variables are used to store information to be referenced and manipulated in a computer program. They also provide a way of labeling data with a descriptive name, so our programs can be understood more clearly by the reader and ourselves. It is helpful to think of variables as containers that hold information.")
	speak = "Variables are used to store information to be referenced and manipulated in a computer program."
	speak += "...Go through the categories of variables."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

def local_variable_func():
	print(local_variable['definition'])
	speak = "The brief definition of local variable expression is."
	speak += local_variable['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print('What would you like to know about local variable ?')
	print('The subcategories available are :')
	dict_keys = list(local_variable.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in local variable that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",local_variable[dict_keys[response-1]])
		elif response == 0:
			return
		else:
			print('Invalid response')


def global_variable_func():
	print(global_variable['definition'])
	speak = "The brief definition of global variable expression is."
	speak += global_variable['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print('What would you like to know about global variable loop ?')
	print('The subcategories available are :')
	dict_keys = list(global_variable.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in  global variable that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",global_variable[dict_keys[response-1]])
		elif response == 0:
			return
		else:
			print('Invalid response')


def static_variable_func():
	print(static_variable['definition'])
	speak = "The brief definition of static variable expression is."
	speak += static_variable['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print('What would you like to know about static variable loop ?')
	print('The subcategories available are :')
	dict_keys = list(static_variable.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1

	response =1
	while(response!=0):
		print('Enter the number of subcategory in  static variable that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",static_variable[dict_keys[response-1]])
		elif response == 0:
			return
		else:
			print('Invalid response')


def automatic_variable_func():
	print(automatic_variable['definition'])
	speak = "The brief definition of automatic variable expression is."
	speak += automatic_variable['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print('What would you like to know about automatic variable loop ?')
	print('The subcategories available are :')
	dict_keys = list(automatic_variable.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in automatic variable that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",automatic_variable[dict_keys[response-1]])
		elif response == 0:
			return
		else:
			print('Invalid response')

def external_variable_func():
	print(external_variable['definition'])
	speak = "The brief definition of external variable expression is."
	speak += external_variable['definition']
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)

	print('What would you like to know about external variable loop ?')
	print('The subcategories available are :')
	dict_keys = list(external_variable.keys())
	j = 1
	for i in dict_keys:
		print(j,':',i)
		j = j+1
	response =1
	while(response!=0):
		print('Enter the number of subcategory in external variable that you wish to see ,else press 0 to end explanation phase')
		response = int(input())
		if(response in range(1,len(dict_keys)+1)):
			print(dict_keys[response-1]," : ",external_variable[dict_keys[response-1]])
		elif response == 0:
			return
		else:
			print('Invalid response')

### To display the list of all the documentations available
def available_documentation():
	all_doc = ['if statement','else statement','break and continue statements ','while loop','for loop',
			'array data structure','return statement','local variable','global variable','static variable','external variable','automatic variable']
	for i in range(len(all_doc)):
		print(i+1,': ',all_doc[i])

### Just returning the list of documentations, to consider the similarity had to include else clause with break and continue, to match as entity
def documentation_list():
	all_doc = ['if statement','else statement','break and continue statements and else clauses on loops','while loop','for loop',
			'array data structure','return statement','local variables','global variables','static variables','external variables','automatic variables']

	return all_doc