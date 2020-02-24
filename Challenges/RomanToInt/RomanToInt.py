def romanToInt(romans: dict, s: str) -> int:
    # romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    out = 0
    i = 0
    if len(s) >= 2:
        while i < (len(s) - 2):
            if romans[s[i]] < romans[s[i + 1]]:
                out = out + romans[s[i + 1]] - romans[s[i]]
                i = i + 2
                continue
            out = out + romans[s[i]]
            i = i + 1
        if len(s) - i == 1:
            out = out + romans[s[-1]]
        else:
            if romans[s[-2]] < romans[s[-1]]:
                out = out + romans[s[-1]] - romans[s[-2]]
            else:
                out = out + romans[s[-2]] + romans[s[-1]]
    else:
        out = out + romans[s[0]]
    return out


romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
inpstr = input("Enter the Roman number which you want transfer to integer: ")
inpstr = inpstr.upper()
for i in range(len(inpstr)):
    if inpstr[i] not in romans.keys():
        print("Please enter a valid Roman number")
        exit(0)
output = romanToInt(romans, inpstr)

print(f"The integer for Roman number '{inpstr.upper()}' is :{output}")
