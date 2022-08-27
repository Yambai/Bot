import markovify
from datetime import date

def markovf(user_text):
	
	today = date.today()
	today = str(today).split('-')[2]
	with open("messages.txt") as f:
		text = '.\n'.join(f.read().split('§'))
	text_model = markovify.Text(text)
	return text_model.make_short_sentence(28000)
	#return text_model.make_short_sentence(140, tries=100)
#print(markovf('1'))