def formalGreeting():
	print("How are you?")

def casualGreeting():
	print("What's up?")

def greet(self, greetFormal, greetCasual):
		if (self == 'formal'):
			self.greetFormal()
		else:
			if (self == 'casual'):
				self.greetCasual()
				
greet('casual', formalGreeting, casualGreeting)
			
