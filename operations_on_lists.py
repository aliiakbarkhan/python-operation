print('belongs to ali akbar khan')

'''Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you’d like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.'''

invited = ['boy1', 'boy2', 'boy3', 'boy4', 'boy5']
print('hi, ' + invited[0] + ' please come to my home for dinner')
print('hi, ' + invited[1] + ' please come to my home for dinner')
print('hi, ' + invited[2] + ' please come to my home for dinner')
print('hi, ' + invited[3] + ' please come to my home for dinner')
print('hi, ' + invited[4] + ' please come to my home for dinner')
# completed

'''You just heard that one of your guests can’t make the
dinner, so you need to send out a new set of invitations. You’ll have to think of
someone else to invite.
•	 Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can’t make it.
•	 Modify your list, replacing the name of the guest who can’t make it with
the name of the new person you are inviting.
•	 Print a second set of invitation messages, one for each person who is still
in your list.'''

print('unfortunately ' + invited[2] + ' will be unable to join us')
del invited[2]
print(invited)
invited.insert(2, 'ali')
print(invited)
# completed

'''You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
•	 Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
•	 Use insert() to add one new guest to the beginning of your list.
•	 Use insert() to add one new guest to the middle of your list.
•	 Use append() to add one new guest to the end of your list.
•	 Print a new set of invitation messages, one for each person in your list.'''

print('fortunately, by god we have got a bigger table')
invited.insert(0, 'first')
invited.insert(3, 'middle')
invited.insert(7, 'last')
print(invited)
# completed

'''You just found out that your new dinner table won’t
arrive in time for the dinner, and you have space for only two guests.
•	 Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
•	 Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you’re sorry you can’t invite
them to dinner.
•	 Print a message to each of the two people still on your list, letting them
know they’re still invited.
•	 Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program.'''

print('i am so sorry but i can only invite two of you')
invited.pop(0)
invited.pop(0)
invited.pop(0)
invited.pop(0)
invited.pop(1)
invited.pop(1)
print(invited)
print('you, Mr.' + invited[0].title() + ' is still invited')
print('you, Mr.' + invited[1].title() + ' is still invited')

del invited[0]
del invited[0]
print(invited)
# completed
