# helpshift

Application for Cards for wallet:

You have a limited number of slots for your credit cards in your wallet. The number of credit cards you have is always increasing. But you want a
way to store only the ones you actually use.
This is a python program that implements this application.

#How to run the program?

$ python wallet.py

# Different functions in the program:

1. Reset: Specify the number of slots you have in your wallet and remove any previously saved cards. By default, the number of slots
is set to 3.
2. Add new card: A card is identified by a unique number. When you add a new card, the program returns that unique number
(because cards can have the same name).
3. Use existing card: Use a card by specifying the card's unique number.
4. Show cards for wallet: Print the name and the unique number of each card that you should put in your wallet. The program 
intelligently choose the cards that are used most recently.

