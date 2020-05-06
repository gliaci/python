class ValidInput:

    def __init__(self):
        pass

    def isNotBlank(self, input):
        return input != None and input != "" and input != " "

    def isPositiveNumber(self, input):
        try:
            result = int(input)
            return result > 0
        except:
            return False

    def isInPositiveRangeNumber(self, input, fromNumber, toNumber):
        try:
            result = int(input)
            if result < fromNumber or result > toNumber:
                raise ValueError
            return True
        except ValueError:
            return False
        except:
            return False

