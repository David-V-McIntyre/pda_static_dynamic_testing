### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:                               #CardGame should not be a class


  def check_for_ace(self, card):              #as CardGame is not a class this line should not be indentend (and all subsequent lines should be unindented one level.) Additionally "self" should be removed from these tests.
    if card.value = 1:                        #"=" should be "=="
      return True
    else                                      #there should be a ":" after "else"
      return False
   

  dif highest_card(self, card1 card2):        #"dif" should be "def". There should be a comma between "card1" and "card2". Self should be removed.   
  if card1.value > card2.value:               # this IF statement should be indented, as should the three lines below it
    return card                               #This should be "card1" instead of "card"
  else:
    return card2
  


def cards_total(self, cards):                 #Self should be removed.
  total                                       #This variable is not defined
  for card in cards:
    total += card.value
    return "You have a total of" + total      #cannot concatenate string and int. Suggest using f-string or changing "total" to "str(total)" and adding a space between "of" and the closing quote mark. Additionally the return statement is not indented.
  
```
