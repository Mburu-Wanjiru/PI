print("Good Morning Mburu")

print ('i love you')

#pip is used to install exennsion

#printing a poem
print("Twinkle, Twinkle, Little Star")
print("BY JANE TAYLOR")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")

print("When the blazing sun is gone,")
print("When he nothing shines upon,")
print("Then you show your little light,")
print("Twinkle, twinkle, all the night.")
print("")
print("Then the traveler in the dark")
print("Thanks you for your tiny spark,")
print("How could he see where to go,")
print("If you did not twinkle so?")

print("In the dark blue sky you keep,")
print("Often through my curtains peep")
print("For you never shut your eye,")
print("Till the sun is in the sky.")

print("As your bright and tiny spark")
print("Lights the traveler in the dark,")
print("Though I know not what you are,")
print("Twinkle, twinkle, little star.")





print("Good Morning Mburu")

print ('i love you')

#pip is used to install exennsion

#printing a poem
print("Twinkle, Twinkle, Little Star")
print("BY JANE TAYLOR")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")

print("When the blazing sun is gone,")
print("When he nothing shines upon,")
print("Then you show your little light,")
print("Twinkle, twinkle, all the night.")
print("")
print("Then the traveler in the dark")
print("Thanks you for your tiny spark,")
print("How could he see where to go,")
print("If you did not twinkle so?")

print("In the dark blue sky you keep,")
print("Often through my curtains peep")
print("For you never shut your eye,")
print("Till the sun is in the sky.")

print("As your bright and tiny spark")
print("Lights the traveler in the dark,")
print("Though I know not what you are,")
print("Twinkle, twinkle, little star.")




print("Good Morning Mburu")

print ('i love you')

#pip is used to install exennsion

#printing a poem
print("Twinkle, Twinkle, Little Star")
print("BY JANE TAYLOR")
print("Twinkle, twinkle, little star,")
print("How I wonder what you are!")
print("Up above the world so high,")
print("Like a diamond in the sky.")

print("When the blazing sun is gone,")
print("When he nothing shines upon,")
print("Then you show your little light,")
print("Twinkle, twinkle, all the night.")
print("")
print("Then the traveler in the dark")
print("Thanks you for your tiny spark,")
print("How could he see where to go,")
print("If you did not twinkle so?")

print("In the dark blue sky you keep,")
print("Often through my curtains peep")
print("For you never shut your eye,")
print("Till the sun is in the sky.")

print("As your bright and tiny spark")
print("Lights the traveler in the dark,")
print("Though I know not what you are,")
print("Twinkle, twinkle, little star.") 


#10-10-2023
#variables in python
aa=234
print(aa)
bb=23.45
print(bb)
cc="jim"
print(cc)
#
# Datatypes in python
#types include -->int,floating,strings,booleans,none
print("arithmetic operations --> +,-,*,/")
a=16
b=4
print("a+b = ",a+b)
### a+b =  20

print("a-b = ",a-b)
### a-b =  12

print("a*b = ",a*b)
### a*b =  64

print("a/b = ",a/b)
### a/b =  4.0



#assignment operators
print('assignment operators --> = , += , -= ')
d=12
c=16

print('d =',d)
### d = 12

c+=d
print('c+=d',  c)
###c+=d 28

c-=d
print('c-=d',  c)
### c-=d 16


print('comparison operator --> == , > , < , >= ,<= , !=')
e=25
f=45

print('e==f  ',e==f)
### e==f   False

print('e > f  ',  e>f)
### e > f   False

print('e < f  ', e<f)
### e < f   True

print('e >= f  ',e>=f )
### e >= f   False

print('e < = f  ' ,e<=f)
### e < = f   True
 
print('e != f  ', e!=f)
### e != f   True


print('Logical Operrators ---> and , or , not ')
g=900
h=105

# and checks if all is true and responds with a truthy value
# or checks a true value and returns it
# not returns completely opposite of the given constant

print('g==h and g>h ',g==h and g>h)
### g==h and g>h  False

print('g==h and g>h ',g==h or g>h)
### g==h and g>h  True

print('not g>h  ',not g>h)
### not g>h   False



###A program to add two numbers
i=int(input('input i '))
j=int(input('input j '))
print('i+j= ',i+j)

### A program to see the remainder of a num that is divided by 2
z=int(input('enter the number'))
print('Rem Num',z % 2)

### A program to find average of 3 inputs
x=int(input('num i '))
y=int(input('num ii'))
v=int(input('num iii'))
sum=x+y+z

print('Average = ', sum/3)





### working with strings

                                 # Slicing
nam='James Mburu Wanjiru'
print(nam[0])
##J
print(nam[0:3])
##Jam
print(nam[2:8])
##mes Mb
print(nam[1:9:1])
## ames Mbu
print(nam[0:10:2])
## JmsMu
print(nam[-1])
## u
print(nam[1:-3])
## ames Mburu Wanj
print(nam[1:-2:3])
## asbuai
print(nam[0:])
## James Mburu Wanjiru
print(nam[:7])
## James M


######## STRINGS FUNCTIONS  IN PYTHON
print('..........LEN ()..........')
#checks the length of a string
jim='James Mburu Wanjiru'
print(len(jim))
# 19

print('..........endswith ()    startswith()..........')
#reference the arguements using string provided and returns a boolean
mose='Moses Mbugua'
print(mose.startswith('Mos'))
# true
print(mose.endswith('za'))
# false


print('......count ().............')
# returns the number of occurence of named arguement
kim='Peter Kimani'
print(kim.count('e'))
# 2


print('..........capitalize ()..........')
#this puts the 1st character to capital letters
na='my name is Jim.'
print(na.capitalize())
# My name is Jim.


print('..........find()..........')
# checks the said arguement in a string and returns the the index of the first character.
shosh='Grace Wamaitha mburu'
print(shosh.find('mburu'))
# 15


print('..........replace()..........')
#replace the said argument with the new word
guka='James Mburu Mbugua'
print(guka.replace('james','jim'))
# jim Mburu Mbugua



