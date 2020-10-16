from clara.interpreter import getlanginter
from New_functions.documenting import return_explanation

import string
import re

### Imports for voice 
from gtts import gTTS
from playsound import playsound
from New_functions.bot_conversation import RecognizeSpeech_during_interaction
from New_functions.operator_analysis import explain_in_brief

def compare_outputs(programs, inter,args, ins):
	try:
		flag = 0 ### Needed because sometimes though output match for given test cases,
				 ### But for some unseen cases it might go wrong(because repair is generated)	
		if ins != None:
			for test_case in ins:
				#NOTE: The index = len(programs)-1 is the index of incorrect program
				trace_incorrect = inter.run(programs[len(programs)-1], None, test_case, args)
				trace_correct = inter.run(programs[0], None, test_case, args)

				inc_len = len(trace_incorrect)-1
				c_len = len(trace_correct)-1
				#Now compare outputs for each test cases and on encountering first mismatch return 
				### For multiple test cases it should be of form --ins "[[21,31],[44,43]]", here there are 2 test cases
				incorrect_ans = trace_incorrect[inc_len][2]["$out'"].replace('\\n',' , ').strip(' , ')
				correct_ans = trace_correct[c_len][2]["$out'"].replace('\\n',' , ').strip(' , ')

				while correct_ans == incorrect_ans:
					inc_len = inc_len-1
					c_len = c_len-1
					if c_len < 0 or inc_len < 0:
						 break
					incorrect_ans = trace_incorrect[inc_len][2]["$out'"].replace('\\n',' , ').strip(' , ')
					correct_ans = trace_correct[c_len][2]["$out'"].replace('\\n',' , ').strip(' , ')


				if correct_ans != incorrect_ans:
					flag = 1
					### Had implemented for better output but it cannot be generalized
					# # To remove the input part from the output which we are displaying
					# correct_inpt_part = trace_correct[0][2]["$out'"].replace('\\n',' , ').strip(' , ')
					# incorrect_inpt_part = trace_incorrect[0][2]["$out'"].replace('\\n',' , ').strip(' , ')

					# # print(correct_inpt_part)
					# # print(incorrect_inpt_part)
					# correct_ans = correct_ans.replace(correct_inpt_part,'')
					# incorrect_ans = incorrect_ans.replace(incorrect_inpt_part,'')
					
					#Including the speech to bring focus of user to look at repair
					speak = "Note. Have a look at your output and expected output."
					speech_obj = gTTS(text = speak, lang = 'en', slow=False)
					speech_obj.save('wit_bot.mp3')

					print("\n** The comparison between output generated by your code and the expected output **\n")
					print("Testcase for which you went wrong takes input :", test_case)
					print("The output of your program is :=",incorrect_ans) 
					print("The correct output expected is :=", correct_ans)
					print("----------------------------------------------------------------\n")
					playsound('wit_bot.mp3', True)
					break
			if flag == 0:
				print("\n*Outputs match, but since repairs are generated, it might not work when passed through exhaustive test cases\n")
		else:
			print("\n*There are no outputs printed, possibly the solution is just returned to function which calls\n")

	except Exception as err:
		print("\nCouldn't generate trace for your program, hence can't compare outputs\n")

def incorrect_return(programs,rep_prog, inter, args, ins):
	### The trace would be useful only if a common function naming is followed(usually given to implement specific function)
	print("There is an incorrect value returned",end = ".")
	speak = "There is incorrect value returned by the function."
	speech_obj = gTTS(text = speak, lang = 'en', slow=False)
	speech_obj.save('wit_bot.mp3')
	playsound('wit_bot.mp3', True)
	###Calling function to take user preference
	explain_in_brief("return expressions", return_explanation.__doc__)

	print("Press 1 to continue with comparing correct and incorrect return value.\n")
	print("NOTE : Press 1 only if given programming template for this problem is followed, else press any key to continue\n")
	reply = input()
	if reply == '1':
		# extracting the index of the referenced program to generate repair 
		referenced_prog = rep_prog[1]
		index = 1
		if '.c' in referenced_prog:
			index = referenced_prog.split('.c')[0][-1] #This gives the representative program number in cluster
		elif '.py' in referenced_prog:
			index = referenced_prog.split('.py')[0][-1] #This gives the representative program number in cluster
		index = int(index)
		index = index-1
		try:	
			if ins != None:
				for test_case in ins:
					trace_incorrect = inter.run(programs[-1], None, test_case, args)
					### Have to look for getting the program which is being referenced from the cluster
					trace_correct = inter.run(programs[index], None, test_case, args)

					c_len = len(trace_correct)-1
					#Now compare outputs for each test cases and on encountering first mismatch return 
					### For multiple test cases it should be of form --ins "[[21,31],[44,43]]", here there are 2 test cases
					i = 0
					incorrect_return = trace_incorrect[i][2]["$ret'"]
					correct_return = trace_correct[i][2]["$ret'"]

					while correct_return == incorrect_return:
						i = i+1
						if i > c_len:
							break
						incorrect_return = trace_incorrect[i][2]["$ret'"]
						correct_return = trace_correct[i][2]["$ret'"]

					if correct_return != incorrect_return:
						funcName = trace_correct[i][0]
						print("It is returned by the function named,",funcName )
						print("Testcase for which you went wrong is :", test_case)
						print("Your program is returning :",incorrect_return)
						print("But expected return value is :", correct_return)
						break

			elif args != None:
				for test_case in args:
					# print("testcase :", test_case)
					trace_incorrect = inter.run(programs[-1],None, ins, test_case)
					trace_correct = inter.run(programs[index],None, ins , test_case)

					# ### The last trace of the function includes the final return value
					c_len = len(trace_correct)-1
					#Now compare outputs for each test cases and on encountering first mismatch return 
					### For multiple test cases it should be of form --ins "[[21,31],[44,43]]", here there are 2 test cases
					i = 0
					incorrect_return = trace_incorrect[i][2]["$ret'"]
					correct_return = trace_correct[i][2]["$ret'"]

					while correct_return == incorrect_return:
						i = i +1
						if i > c_len:
							break 
						incorrect_return = trace_incorrect[i][2]["$ret'"]
						correct_return = trace_correct[i][2]["$ret'"]

					if correct_return != incorrect_return:
						funcName = trace_correct[i][0]
						print("It is returned by the function named,",funcName )
						print("\nTestcase for which you went wrong is :", test_case)
						print("Your program is returning :",incorrect_return)
						print("But expected return value is :", correct_return)
						break

			print("\n--------------------------------------------------------------------------\n")
		except Exception as err:
			print("\nCouldn't generate appropriate trace, usually occurs when common programming template is not followed\n")
	else:
		return 

def display_location(clara_feedback):
	diff_locs = [' the condition of the if-statement ',' inside the if-branch starting ',' after the if-statement beginning ',
				' inside the else-branch starting ',' the condition of ', ' *after* the ',
				' update of the ',' inside the body of the ', ' at ', ' at line ', ' around the beginning of ']

	place = 0
	for loc in diff_locs:
		if loc in clara_feedback:
			place = loc
			segment = clara_feedback.split(loc)[1]
			break

	if place != 0:
		segment = place + segment
		location = segment.split(" (cost")[0]
		
		return location
	else:
		print("Couldn't trace exact location, it would be displayed in the final repair\n")
