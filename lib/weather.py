def weather(loaction):
	from subprocess import call
	cmd = 'wttr.in/'+ loaction 
	call(['curl', cmd])
#weather('faridabad')

