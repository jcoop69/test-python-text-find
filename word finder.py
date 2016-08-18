>>> text = "this is a python text. hoperfully it will find a word. that word is 'snake' FIND IT!!!"
>>> start = text.find("'")
>>> end = text.find("'",start+1)
>>> _start = start + 1
>>> word = text[_start:end]
>>> print word
