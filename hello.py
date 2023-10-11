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


print('..........in keyword..........')
# checks the ekement is in a string ;;returns a boleam
jimna='wanjiru james mburu'
print('mburu' in jimna)
# true


print('..........not in ..........')
# checks the said character in a string ;;returns boolean
aaa='James  Mburu mbugua '
print('mbugu' not in aaa)
# true


print('.......... upper()..........')
# converts the whole string to upper case
mose='moses mbugua wanjiru'
print(mose.upper())
# MOSES MBUGUA WANJIRU





print('.......... lower()..........')
# converts the whole string to LOWER case
moses='MOSES MBUGUA WANJIRU'
print(moses.lower())
#  moses mbugua wanjiru


print('.......... strip()..........')
# removing un necessary white space
mosess='   moses mbugua wanjiru    '
print(mosess.strip())
# moses mbugua wanjiru


print('.......... split()..........')
# puts each single strings to differnt strings
mo='moses mbugua wanjiru'
print(mo.split())
 #['moses' ,'mbugua', 'wanjiru']

#project 1
#to display  a good morning
mburu=input('Enter your name')
print('Good Afternoon',mburu)
#  Good Afternoon mburu


#project2
namee=input('Enter your name')
datee=input('enter the date')
temparate=''' 
Dear <name>\n\tI am delighted to invite you to my birthday ceremony.\nit will be hosted in kyu traina on date <date>.
 '''
print(temparate.replace('<name>',namee).replace('<date>'))



## list in python
#container used to store data.
print('........indexing in list.........')
l1=[7,3,5,3,1,2]
print(l1[0])
# 7
print(l1[1])
#3
print(l1[2])
#5
print(l1[3])
#3
print(l1[4])
#1
print(l1[5])
#2
print(l1[0:4])
# 7,3,5,3
print(l1[70])
#error
