def splitter(text):
	return text.split('.')

def replacer(text):
	text = text.replace('\n','@')
	text = text.replace(' ','#')
	text = text.replace('\t','+')
	return text

def mainRunner(filename):
	contents = open(filename,'r').read()
	contents = replacer (contents)
	contents = splitter(contents)
	
	output = open('_satz.'.join(filename.rsplit('.',1)),'w')
	for line in contents:
		output.write(line+'\n')
	output.flush()
	output.close()

mainRunner('PythonText.txt')



def mainRunner2(filename):
	contents = open(filename, 'r').read()
	contents = restore(contents)
	
	output = open('_antiHashTag.'.join(filename.rsplit('.',1)),'w')
	output.write(contents)
	output.flush()
	output.close()


def restore(text):
	text = text.replace('@','\n').replace('#',' ')
	text = text.replace('+', '\t')
	return text

mainRunner2('PythonText_satz.txt')