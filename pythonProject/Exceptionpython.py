
#Assertion is also one of the way and fail if you do not meet that condition.
#The condition should be true, else it will fail.


ItemsCart = 0

if ItemsCart !=2:
    pass

#we know that above condition would fail:
#So, we can use assertion here
assert(ItemsCart==2)
#---> We can write like this....
#It gives the assertion error

#It is very important with test automation framework

print("___________________")
#try, catch

#If a code fails in try block and then it will send the control back to catch block.
#Try block will help tp actually get the error, but it won't fail the test cases.

try:
    with open('filelog.txt','r') as reader:
        reader.read()
except Exception as e:
    print(e)
    #print("I reached this block because there is a failure in the block")

#Finally, will run irrespective of errors in try and except:
#If there is requirement to delete the cookies, we can put that in finally block.
finally:
    print("Cleaning up the resources!")








