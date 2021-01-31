height=12.0
print(height/3)


x=0
y=10

if 0==x:
    if y==10:
        print("Yes") 
#indent matters because it determines the end of the block


x=20
if x < 2:
  print("small")
if x <10:
  print("medium")
else:
  print("something else")
#order matters so that the last function works

#TRY AND EXCEPT #to compensate for errors: so you can test specific lines of code at a time

ied=print("Hello Bob")
try: #does not make sense if you have more than 1 line of code because it already fails
  ied2=int(ied)
except:
  ied2=-1
print("first",ied)
