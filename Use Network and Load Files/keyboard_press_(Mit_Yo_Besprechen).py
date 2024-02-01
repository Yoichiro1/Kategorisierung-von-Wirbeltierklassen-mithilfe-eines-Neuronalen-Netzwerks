def select_file():
 print('PLACEHOLDER') #PASTE YO'S CODE HIER
def adjust_file():
   print('PLACEHOLDER')
def Manual_Test():
   print('PLACEHOLDER')
#Source: https://stackoverflow.com/questions/24072790/how-to-detect-key-presses
while True:  
    try:  # used try so that if user pressed other than the given key error will not be shown
        if kb.is_pressed('x'):
            select_file()
            adjust_file()
            Manual_Test()
            print("TEST COMPLETED")
            break  
    except:
     break  # if user pressed a key other than the given key the loop will break
