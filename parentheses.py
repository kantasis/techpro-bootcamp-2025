def validate(text):
   open_counter = 0
   close_counter = 0
   for character in text:
      if character == '(':
         open_counter = open_counter + 1
      if character == ')':
         close_counter = close_counter + 1
      if close_counter > open_counter:
         return False
   return close_counter == open_counter

print(validate('()'))
print(validate('())'))
print(validate('(()'))
print(validate('()()'))
print(validate(')()('))
print(validate('(()(()()))'))



