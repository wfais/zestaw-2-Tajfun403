vals = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'IX': 9,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
}

vals = dict(sorted(vals.items(), key=lambda item: item[1], reverse=True))

twoLetterVals = {k: v for k, v in vals.items() if len(k) == 2}
oneLetterVals = {k: v for k, v in vals.items() if len(k) == 1}

reverseVals = {v: k for k, v in vals.items()}
reverseVals = dict(sorted(reverseVals.items(), reverse=True))

def CheckIsRomanValid(rzymskie: str):
    if rzymskie.__contains__("IIII") or rzymskie.__contains__("VV") or rzymskie.__contains__("XXXX") or \
       rzymskie.__contains__("LL") or rzymskie.__contains__("CCCC") or rzymskie.__contains__("DD") or \
       rzymskie.__contains__("MMMM"):
        return False
    allowedChars: set = {'I', 'V', 'X', 'L', 'C', 'D', 'M'}
    for char in rzymskie:
        if char not in allowedChars:
            return False
    return True

def rzymskie_na_arabskie(rzymskie):
    if not CheckIsRomanValid(rzymskie):
        raise ValueError("Invalid Roman numeral")
    sum = 0
    i = 0
    lastVal = 42069
    while i < len(rzymskie):
        for roman, value in vals.items():
            letterCount = len(roman)
            if rzymskie[i:i+letterCount] == roman:
                newVal = value
                if newVal > lastVal:
                    raise ValueError("Invalid Roman numeral")
                lastVal = newVal
                sum += lastVal
                i += letterCount
                break
        else:
            raise ValueError("Invalid Roman numeral")
    return sum

def arabskie_na_rzymskie(arabskie):
    if arabskie < 1 or arabskie > 3999:
        raise ValueError("Input out of range")
    
    rzymskie = ""
    while arabskie > 0:
        for value in reverseVals.keys():
            if arabskie >= value:
                arabskie -= value
                rzymskie += reverseVals[value]
                break
    return rzymskie

if __name__ == '__main__':
    try:
        # Przykłady konwersji rzymskiej na arabską
        rzymska = "MCMXCIV"
        print(f"Liczba rzymska {rzymska} to {rzymskie_na_arabskie(rzymska)} w arabskich.")
        
        # Przykłady konwersji arabskiej na rzymską
        # arabska = 1994
        # print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")

        # Przykłady konwersji arabskiej na rzymską
        arabska = 3999
        print(f"Liczba arabska {arabska} to {arabskie_na_rzymskie(arabska)} w rzymskich.")
        
    except ValueError as e:
        print(e)
