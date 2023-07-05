import RPi.GPIO as GPIO
import time
from ubidots import ApiClient
GPIO.setmode(GPIO.BOARD)
wtr_sen=3
led=5
buz=7
api = ApiClient(token="BBFF-dAFgsoCOtZjgQi86OhFnDcJl5Cq9Z0") 
data1= api.get_variable("6156b83183f41f000b8c7003")
GPIO.setup(wtr_sen,GPIO.IN)
GPIO.setup(buz,GPIO.OUT)
GPIO.setup(led,GPIO.OUT)
while(1):
        data=GPIO.input(wtr_sen)
        print(data)
        if(data==1):
                print "Raining"
                response= data1.save_value({"value":data})
                while(1):
                        data = GPIO.input(wtr_sen)
                        GPIO.output(buz,1)
                        GPIO.output(led,1)
                        time.sleep(0.5)
                        GPIO.output(led,0)
			GPIO.output(buz,0)
                        time.sleep(0.5)
                        if(data == 0):
                                break
        		else:
                		print "no rain"
                		GPIO.output(led,0)
                		GPIO.output(buz,0)
                		time.sleep(1)
                		response = data1.save_value({"value":data})