########################################################################################################################################
#Author: Sai Charan Regunta
#Date: 21st May 2016
#Course: Principles of Programming Languages
#Description: Simple Interpreter code for "ipython Interpreter"
#Language Used: Python
#Date of Submission: 31st May 2016
#References: http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html (Infix to Postfix)
########################################################################################################################################

from termcolor import colored
from functions import *
import string
Values = {}
Values['']=''

##################################################### INFIX TO POSTFIX ################################################################
def infixToPostfix(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

################################################################ STORING ALL THE VALUES ################################################
def store(variable,value):
	#print variable
	#print value		
	for i in value:
		try:
			val= (val*10) + float(i)
		except:
			break
	Values[variable]=float(value)
########################################################################################################################################

########################################################## CALCULATION(Replacing Variables with Values)##################################
def calculation(text):
	#result=Interpreter_calc(text)			
			alpha=0
			al=0
			for alpha in range(0,25):
				if string.lowercase[alpha] in text:
					al=1
			try:
				if al:
					var=''
					Var=[]
					PostFix=[]
					flagg=0		
					v=0	
					#print text				
					PostFix=infixToPostfix(text)
					for ii in range(0,len(PostFix)	):
						#print PostFix[ii]
						if PostFix[ii] not in "0123456789+-*/%^":
							var = var + PostFix[ii]
							#print var
							flagg=1
						else:
							if flagg:
								flagg=0
								#print var
								#print text
								text=string.replace(text,var,str(Values[var]))
									#print text							
								#print Values[var]
								var=''
					#print var		 
					text=string.replace(text,var,str(Values[var]))
					return text					
					#text.replace(var,Value[var])
					#print text
					#print "+-*/%^"
			except:
				print "Variables Given in the Expression were not Defined\n"
				return "continue"
######################################################### FOR LOOP #######################################################################
def forloop(loop_variable,text,sentence):
		#print Values[loop_variable]
	        start=0
	        end=0
		increment=0
	        index=text.index('(')
	        for i in range(index+1,len(text)):
	            try:
	                start=start*10+int(text[i])
	            except:
	                index=i
	                break
		#print loop_variable
		#print start
		Values[loop_variable]=start
		#print Values[loop_variable]
	        for i in range(index+1,len(text)):
	            try:
	                end=end*10+int(text[i])
	            except:
	                index=i
	                break	        
	        for i in range(index+1,len(text)):
	            try:
	                increment=increment*10+int(text[i])
	            except:
	                index=i+1
	                break
	        if increment == 0:
	            increment=1
	        for i in range(start,end,increment):
			#print sentence[0]
			if "for" in sentence[0]:
				lp_var=sentence[0].split(' ')
				forloop(lp_var[1],sentence[0],sentence[1:])
			execute_commands(sentence)
			#print Values[loop_variable]
			Values[loop_variable] = Values[loop_variable] + increment

######################################################### COMMANDS THAT ARE EXECUTED ####################################################
def execute_command(sentence):
	if "print" in sentence:
		sentence=sentence.replace(" ",'')
		
		#print sentence
		if "\"" in sentence:
			sentence=sentence.replace("\"",'')
			#print sentence
			sentence = sentence[sentence.index('t')+1:]	
			print sentence
		elif ("+" in sentence) or ("-" in sentence) or ("*" in sentence) or ("/" in sentence) or ("**" in sentence) or ("^" in sentence) or ("%" in sentence):
			#print sentence			
			text1=sentence[sentence.index('t')+1:]
			#print text1
			alpha=0
			al=0
			for alpha in range(0,25):
				if string.lowercase[alpha] in text1:
					al=1
			if al:
				text1=calculation(text1)
			#print text1	
			result=eval(text1)
			print result
		else:
			#print "came"
			print Values[sentence[sentence.index('t')+1:]]
	elif "=" in sentence:
			text=sentence
			if ("+" in text) or ("-" in text) or ("*" in text) or ("/" in text) or ("**" in text) or ("^" in text) or ("%" in text):
				text1=text[text.index('=')+1:]
				#print text
				alpha=0
				al=0
				for alpha in range(0,25):
					if string.lowercase[alpha] in text1:
						al=1
				if al:
					text1=calculation(text1)
				result=eval(text1)
				#print result,text[:text.index('=')+1]
				store(text[:text.index('=')],str(result))
			else:
				store(text[:text.index('=')],text[text.index('=')+1:])
		
def execute_commands(sentences):
	#print sentences
	for ex in range(0,len(sentences)):
		execute_command(sentences[ex])
###########################################################################################################################################
def main():
  		
    i=1
    while True:
        try:
	    t='In [' + str(i) + ']: '
	    t=colored(t,'blue')
            text = raw_input(t)
	    word=text.split(' ')
#####################################################################################  IF LOOP ############################################
	    if word[0]=="if":
		pin=0
		if word[1] == "True":
			pin=1
		elif "==" in text:
			text=text.replace(" ",'')
			expr=text[text.index('f')+1:text.index('=')]
			try:				
				if ("+" in text) or("-" in text) or("*" in text) or("/" in text) or("^" in text) or("%" in text):
					#print "I am Here"
					#print expr
					alpha=0
					al=0
					for alpha in range(0,25):
						if string.lowercase[alpha] in text:
							al=1
					if al:
						expr=calculation(expr)
					#print expr
					value_obtained=eval(expr)
					#print value_obtained
					if value_obtained == int(text[text.index('=')+2:text.index(':')]):
						pin=1
				else:
					if Values[expr] == int(text[text.index('=')+2:text.index(':')]):
							pin=1
			except:
				#print "FK"
				pin=2
		elif "=" in text:			
			pin=2
		elif word[2] == "in":			
			word[1]=word[1].replace("\"",'')
			word[1]=word[1].replace("'",'')
			word[1]=word[1].replace(" ",'')
			len_of_search=len(word[1])
			for p in range(3,len(word)):
				word[3]=word[3]+word[p]
			word[3]=word[3].replace("\"",'')
			word[3]=word[3].replace("'",'')
			word[3]=word[3].replace(" ",'')
			#print word[3]
			check=word[3]
			for iii in range(0,len(check)-2,len_of_search):
				#print check[iii]
				if check[iii] == word[1]:
					pin=1
			if check[len(check)-1] != ":":
				pin=2
					#print check[iii]
		sentence=[]
		while 1:
			sen=raw_input(colored("   ...: ",'blue'))
			if sen=='':
				break		
			sentence.append(sen)

		if pin==1:
			if "else:" in sentence:
				t='Out['+str(i) + ']: '
				t=colored(t,'red')
			    	print t
				execute_commands(sentence[:sentence.index('else:')])	
			else:
				t='Out['+str(i) + ']: '
				t=colored(t,'red')
		    		print t
				execute_commands(sentence[:])	
		
			#print "Its There"
		elif pin==2:
			print "Syntax Error\n"
			continue
		else:
			if "else:" in sentence:
				execute_commands(sentence[sentence.index('else:')+1:])
			continue
##############################################################################  FOR LOOP #######################################
	    elif word[0]=="for" or word[0]=="while":
	        sentence=[]
		while 1:
			sen=raw_input(colored("   ...: ",'blue'))
			if sen=='':
				break		
			sentence.append(sen)		
		forloop(word[1],text,sentence)

################################################################### STORING ALL FUNCTIONS IN A FILE #######################################
	    elif word[0]=="def":
        	    filename1="functions.py"
    		    target1=open(filename1,'r+')
		    target1.read()
		    target1.write(text)
		    target1.write("\n")
		    while 1:
			t='   ...: '
	    		t=colored(t,'blue')
			inp = raw_input(t)
			if inp == "":
				break
			target1.write(inp)
			target1.write("\n")
		    target1.close()	    	    
            else:
            	text = text.replace(" ", "")
###################################################################### FUNCTION CALLING #####################################################
		if "(" in text:
			func="from functions import *"
			if "print" not in text:
				text=func+'\n'+'print '+text
			else:	
				text=func+'\n'+text
			filename="program.py"
     		        target=open(filename,'w')
		        target.write(text)
		        target.write("\n")
			target.close()
			t='Out['+str(i) + ']: '
			t=colored(t,'red')
		    	print t
	    	    	execfile('program.py')
			print
##################################################################### ASSIGNING VALUES #####################################################
		elif "=" in text:
			if ("+" in text) or ("-" in text) or ("*" in text) or ("/" in text) or ("**" in text) or ("^" in text) or ("%" in text):
				text1=text[text.index('=')+1:]
				#print text
				alpha=0
				al=0
				for alpha in range(0,25):
					if string.lowercase[alpha] in text1:
						al=1
				if al:
					text1=calculation(text1)
					if text == "continue":
						i=i+1
						continue
				result=eval(text1)
				#print result,text[:text.index('=')+1]
				store(text[:text.index('=')],str(result))
			else:
				store(text[:text.index('=')],text[text.index('=')+1:])
				print 		
				i=i+1		
				continue
######################################################################### CALCULATIONS #####################################################

		elif ("+" in text) or ("-" in text) or ("*" in text) or ("/" in text) or ("**" in text) or ("^" in text) or ("%" in text):
			alpha=0
			al=0
			for alpha in range(0,25):
				if string.lowercase[alpha] in text:
					al=1
			if al==1: 			
				text=calculation(text)
				if text == "continue":
					i=i+1
					continue
			result=eval(text)			
			t='Out['+ str(i) + ']: '
			t=colored(t,'red')
        		print t + str(int(result)) + '\n'				
############################## JUST COMMAND #####################################################

	    	else:
			if text == "quit":
				print
				break
			else:	
				t='Out['+str(i) + ']: '
				t=colored(t,'red')
				print t + str(Values[text]) + '\n'
				i=i+1
				continue
        except EOFError:
		temp='\n'+ "Do you really want to exit ([y]/n)?"
		te = raw_input(temp)
		if te == 'y':
			break
		else:
			continue		        
		
        i= i+1
    
if __name__ == '__main__':
    main()
