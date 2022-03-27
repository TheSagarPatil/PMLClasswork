"""
x = 0
while x != 6:
    print(x)
    x += 1
else:
	print('finish')
a = list((1,2,3))
a.reverse()
print(a)
x,y,z = a
print(x,y,z)

class duck(object):
    def talk(self):
        print('quacked')

class cat(object):
    def talk(self):
        print('meow')
class whale:
    pass

d = duck()
c = cat()

c.talk()
d.talk()

class animal():
    @staticmethod
    def talk(obj):
        if hasattr(obj, 'talk') :
            obj.talk()


a = animal()
w = whale()

a.talk(d)
a.talk(c)
a.talk(w)

z = {'a','1'}
print(hasattr(z, 'a'))
print( 'a' in z )
print( hash( frozenset( z ) ) )
"""
import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415) 555-4242.')
print( mo.group(1) )

re.compile('(\(parantheses\))')

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('I am Batman, she is Tina Fey')
print(mo1.group())
