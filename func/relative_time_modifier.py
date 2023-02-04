from func.relative_time_object import RelativeTimeObject
from datetime import datetime
import re

class RelativeTimeModifier:
    
    # takes a provided relative time modification string and applies it to the current timestamp
    @staticmethod
    def parse(input: str) -> datetime:
        rtm = RelativeTimeModifier
        rtm.__isString("parse", "input", input)

        # Split the input string into it's component parts
        elementList = rtm.__splitInput(input)

        # remove the initial now() element and set the timestamp
        elementList.pop(0)
        rto = RelativeTimeObject(datetime.utcnow())

        # work through the rest
        operations = [rtm.__parseInputElement(x) for x in elementList]
        for (value, unit) in operations:
            if value is None:
                rtm.__applySnap(rto, unit)
            else:
                rtm.__applyAdjustment(rto, unit, value)

        return rto.toDatetime()

    # tests the input string format and extracts operations into a list
    @staticmethod
    def __splitInput(input: str) -> list[str]:
        # force lowercase - case doesn't matter here, so it's easier than /i
        input = input.lower()
        
        # test the full format
        # date unit regex accepts 
        #   y(ear), mon(th), d(ay) 
        #   h(our), m(inute), s(econd)
        drx = '(?:mon|m(?!on)|[dhys])'
        matchrx = f"now\(\)(([+\-]\d+{drx})|@{drx})*"
        if re.fullmatch(matchrx, input) is None:
            raise ValueError(f'Invalid relative time string provided ("{input}")')
        
        splitrx = f"((?:now\(\))|(?:[+\-]\d+{drx})|(@{drx}))"
        return [x[0] for x in re.findall(splitrx, input)]

    # converts an extracted operation to a limited command ( value, unit )
    #   note: snap operations will have a value of None
    @staticmethod
    def __parseInputElement(input: str) -> tuple:
        # split into contituent parts
        elements = re.split('(\d+|@)', input)

        # first character is the operation (add, subtract, snap)
        # final characters is the time unit to apply
        operation = elements[0]
        unit = elements[-1]
        value = None

        # for addition and subtraction, the unit value is the middle item
        if operation == '+':
            value = int(elements[1])
        if operation == '-':
            value = int(elements[1]) * -1

        return ( value, unit )

    # applies an adjustment operation to a RelativeTimeObject
    @staticmethod
    def __applyAdjustment(rto: RelativeTimeObject, unit: str, offset: int):
        if unit == 'y':
            rto.adjustYears(offset)
        if unit == 'mon':
            rto.adjustMonths(offset)
        if unit == 'd':
            rto.adjustDays(offset)
        if unit == 'h':
            rto.adjustHours(offset)
        if unit == 'm':
            rto.adjustMinutes(offset)
        if unit == 's':
            rto.adjustSeconds(offset)        

    # applies a snap operation a RelativeTimeObject
    @staticmethod
    def __applySnap(rto: RelativeTimeObject, unit: str):
        if unit == 'y':
            rto.snapToYear()
        if unit == 'mon':
            rto.snapToMonth()
        if unit == 'd':
            rto.snapToDay()
        if unit == 'h':
            rto.snapToHour()
        if unit == 'm':
            rto.snapToMinute()
        if unit == 's':
            rto.snapToSecond()

    # tests an inpute value to ensure only strings are accepted
    @staticmethod
    def __isString(method: str, param: str, value: any) -> bool:
        if type(value) is not str:
            raise TypeError(f"\"{method}\" requires parameter \"{param}\" to be of type str")
        return True
