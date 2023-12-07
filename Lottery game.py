import secrets
import sys
secureNumber=secrets.SystemRandom()

while True:
    print('____Welcome to the game____')
    press1=int(input('Press 1 to read the rules or Press 2 to play the game:'))
    if press1==1:
      print('>User age must be at least 18')
      print('>Deposit money more than 5000')
      print('>You must use more than 1000 each time you play:')
    if press1==2:
        uName=input('Please enter your name:')
        uAge=int(input('Please enter your age:'))

        while len(uName)>2 and uAge>17: 
            print('You can play the game now:')
            print('Welcome :3',uName)
            while True:
              uMoney=int(input('Please enter your deposit:'))
              while uMoney>4999:
                print('This is your amount $', uMoney)
                inputMoney=int(input('Please deposit money to PLAY:'))
                luckyNumber=int(input('Please enter your Lucky Number:'))
                systemNumber=secureNumber.randint(a=10,b=99)
                if luckyNumber==20:
                  print('YOU WON!!!')
                  uMoney=(inputMoney*10)+(uMoney-inputMoney)
                  print('Here is ALL YOUR MONEY :3',uMoney)
                  toQuit=int(input('Press 0 to PLAY AGAIN :3'))
                  if toQuit != 0:
                    sys.exit('GG')
                  else:
                    continue
                print('Ohh noo. Please try again. The lucky number is',systemNumber)
                uMoney=uMoney-inputMoney
                if uMoney<1000:
                  print('Not enough money $',uMoney)
                  break
              
              print('Please deposit more money:')
        
        print('Please read the rules carefully again:')
        