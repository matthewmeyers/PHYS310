import pylab
import time

x=[1,2,3]
y=[3,4,5]
z=[5,6,7]
pylab.plot(x,y)
pylab.axis([1,3,1,7])
pylab.show(block=False)
pylab.hold(False)
time.sleep(.5)
pylab.plot(x,z)
pylab.axis([1,3,1,7])
pylab.draw()  #<- I forgot this in the previous email.
pylab.show(block=False)
time.sleep(1)