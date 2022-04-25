import pyfirmata, time

ledR = 13
ledV = 12
ledR1 = 11
ledA = 9
ledA1 = 7
ledV1 = 6
ledR2 = 5
ledA2 = 4
ledV2 = 3
ledR3 = 2


board = pyfirmata.Arduino("COM3")
time.sleep(2)
print("Comunicacion Arduino y Python Exitosa!")
board.analog[0].mode = pyfirmata.INPUT
board.digital[ledR].mode = pyfirmata.OUTPUT
board.digital[ledV].mode = pyfirmata.OUTPUT
board.digital[ledR1].mode = pyfirmata.OUTPUT
board.digital[ledA].mode = pyfirmata.OUTPUT
board.digital[ledA1].mode = pyfirmata.OUTPUT
board.digital[ledV1].mode = pyfirmata.OUTPUT
board.digital[ledR2].mode = pyfirmata.OUTPUT
board.digital[ledA2].mode = pyfirmata.OUTPUT
board.digital[ledV2].mode = pyfirmata.OUTPUT
board.digital[ledR3].mode = pyfirmata.OUTPUT

iterator = pyfirmata.util.Iterator(board)
iterator.start()

while True:
        
                board.digital[ledR].write(1)
                board.digital[ledV].write(1)
                board.digital[ledR1].write(1)
                board.digital[ledA].write(1)
                board.digital[ledA1].write(1)
                time.sleep(1)
                
                board.digital[ledV1].write(1)
                board.digital[ledR2].write(1)
                board.digital[ledA2].write(1)
                board.digital[ledV2].write(1)
                board.digital[ledR3].write(1)
                time.sleep(2)
                
                board.digital[ledR].write(0)
                board.digital[ledV].write(0)
                board.digital[ledR1].write(0)
                board.digital[ledA].write(0)
                board.digital[ledA1].write(0)
                time.sleep(1)
            
                
                board.digital[ledV1].write(0)
                board.digital[ledR2].write(0)
                board.digital[ledA2].write(0)
                board.digital[ledV2].write(0)
                board.digital[ledR3].write(0)
                time.sleep(2)
                
