# Her er der defineret en funktion med navnet addNumbers. Funktionen tager
# imod 2 parametre number1 og number2. Og funktionen returnerer en
# værdi.
def adderNumbers(number1, number2):
    return (number1 + number2)

def adderNumbersAndPrintResult(number1, number2):
    tal3 = adderNumbers(tal1, tal2)
    print(str(tal1) + " + " + str(tal2) + " = " + str(tal3))

def getRemainder(number1, number2):
    return(number1 % number2)


if __name__ == '__main__':
    tal1 = 10
    tal2 = 20
    adderNumbersAndPrintResult(tal1, tal2)

    tal1 = 40
    tal2 = 60
    adderNumbersAndPrintResult(tal1, tal2)


