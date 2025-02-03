basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
print('orange' in basket)
print('crabgrass' in basket)

a = set('abracadabra')
b = set('alacazam')
print(a) # unique letters in a
print(a-b) # letters in a but not b
print(a|b) # letters in a or b or both
print(a&b) # letters in both a and b
print(a^b) # letters in a or b but not both
