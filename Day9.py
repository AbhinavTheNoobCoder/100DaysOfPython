#DAY 9 - Typecasting
a = "1"
b = "2"
print(a+b) #Returns "12" since this is concantenation
print(int(a)+ int(b)) #Returns 3 as this is addition. This is also an explicit type conversion.
a = 9 #int
b = 0.11 #float
print(a+b) #Returns 9.11 which is a floating point number. 9-->9.00 is an implicit type conversion.
a = str(a)
b = str(b)
print(a + b) #90.11
#float(), oct(), bin(), hex(), list(), dict(), tuple() are other methods to typecast.