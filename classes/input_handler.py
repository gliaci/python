import sys

sys.path.append("../")
import getpass
from classes import valid_input


class InputHandler:

    def __init__(self):
        self.validInput = valid_input.ValidInput()

    def inputNotBlankString(self, inputName):
        prompt = None
        while prompt == None:
            try:
                prompt = input("{}: ".format(inputName))
                if self.validInput.isNotBlank(prompt):
                    return prompt
                raise ValueError
            except ValueError:
                prompt = None
                print("Invalid {}!".format(inputName))

    def inputPassword(self):
        return getpass.getpass("Password: ")

    def inputInRangeNumber(self, promtMessage, fromNumber, toNumber):
        prompt = None
        while prompt == None:
            try:
                prompt = input(promtMessage)
                if self.validInput.isInPositiveRangeNumber(prompt, fromNumber, toNumber):
                    return int(prompt)
                raise ValueError
            except ValueError:
                prompt = None
                print("Choose a number >= {} and <= {}".format(fromNumber, toNumber))
