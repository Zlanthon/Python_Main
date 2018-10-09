#Metoden herunder virker på klassen math_Class trækker 2 fra hinanden.
class math_Class():
    def subtractNumbers (self, Number1, Number2):
        return (Number1 - Number2)

#Ved brug af self, SKAL man lavet et objekt af klasse efterfølgende
#Eksempelvis lommeregner = Math.math_Class()
#Hvorefter du kan kalde objektet fx. lommeregner.multiply_Numbers eller lommeregner.subtractNumbers
#uden self kan man kalde klassen uden at lave et objekt,
#Eksempelvis Math.math_Class.multiply_NumbersClass
    def multiply_Numbers(self, number1, number2):
        return (number1 * number2)

    def multiply_NumbersClass(number1, number2):
        return (number1 * number2)