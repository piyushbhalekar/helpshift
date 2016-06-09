import time

class Card:
	card_no = 0
	card_name = ''
	card_usage = 0
	transaction_time= ''
	def __init__(self, no, name,date_time):
		self.card_no = no
		self.card_name = name
		self.transaction_time=date_time

class wallet:
	max_usage = 1
	count = 3
	card_cnt = 0
	cur_unique_number = 1
	
	'''
	card_data : dictionary that maps Card Number to respective instance of the Card
	            with the same Card Number
	'''
	card_data = {}
	card_list = []

	'''
	reset (): Reset the wallet
	Parameters:
	slot -int
	'''
	def reset(self, cnt):
		self.card_data.clear()
		self.card_list = list()
		self.count = int(cnt)
		
	'''
	add(): Adds a new card
	Parameters:
	card_no - int
	card_name - str
	'''
	def add(self,card_no,card_name):
		
		card_new = Card(card_no,card_name,time.asctime( time.localtime(time.time())))
		if(self.card_cnt < self.count):
			
			self.card_data[card_new.card_no] = card_new
			self.sort()
			self.card_cnt += 1

		else:
			
			key = self.card_list[0]
			del self.card_data[key]
			try:
				del self.card_list[0]
			except KeyError:
				print '(!) Card List is empty! Cannot delete element.'
				print '(!) Exiting program.'
				exit(0)
			self.card_data[card_new.card_no] = card_new
			self.sort()
		
	'''
	sort(): sorting the cards on basis of usage and transaction time
	Parameters:
	
	'''
			
	def sort(self):
			card_list_new = []
			
			for i in range(self.max_usage + 1):
				cards = {}
				for data in self.card_data:
					if (self.card_data[data].card_usage == i ):
						cards[self.card_data[data].transaction_time] = self.card_data[data].card_no # map trans time -> card no

				for key in sorted(cards.keys()):

					card_list_new.append(cards[key])
			self.card_list = card_list_new[:]		
			
	'''
	use(): use existing card in the wallet
	Parameters:
	card_no - int
	'''	
			
	def use(self,card_no):
		try:
			if not self.card_list:
				print "Wallet is empty"
			else:
			
		
				for data in self.card_list:
					if self.card_list[data]==card_no:
		
						self.card_data[card_no].card_usage += 1
						if(self.card_data[card_no].card_usage > self.max_usage):
							self.max_usage = int(self.card_data[card_no].card_usage)
						self.card_data[card_no].transaction_time = time.asctime( time.localtime(time.time()))
						self.sort()
						return
		except:
		
			print "card is not present"
		
	'''
	show(): show existing cards in wallet
	'''
	
	def show(self):
		
		op = self.card_list[::-1]
		if not op:
			print "No cards in wallet\n"
		else:
			k = 1
			for i in op:
				print ('%d. %s (Card-id: %d)'% (k,self.card_data[i].card_name,self.card_data[i].card_no))
				k += 1

def main():
	print "Default number of slots is 3\n"
	w = wallet()	
	while(1):
		
		op = raw_input("1) Reset \n2) Add a new card \n3) Use existing card \n4) Show cards for wallet\nEnter your choice(^C to exit) ->>")
		if(op == '1'):
			cnt = raw_input("Enter the slot :")
			if(cnt == 'null'):
				cnt = 3
			w.reset(int(cnt))
		
		elif(op == '2'):
			
			name = raw_input("Enter the Card Name :")
			
			no = w.cur_unique_number
			w.cur_unique_number += 1
			
			try:
				if name.isalpha():
					w.add(int(no),name)
					print 'Unique ID of {0} is {1}'.format(name, no)
				else:
					print "Enter Valid Card Name"
			except ValueError:
				print '(!) Invalid input data'
				
			
		
		elif(op == '3'):
			no = raw_input("Enter the card number to use :")
			if no.isdigit():
				w.use(int(no))
			else:
				print "Enter unique card number"
		elif(op == '4'):
			w.show()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print '\n(!) Exit'
		exit(0)
