import re

def parse():
    result = 0
    re_str = r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don't\(\))"
    with open("input", 'r') as f:
        sinput = f.read()
        matches = re.findall(re_str, sinput)
        sum = True
        for match in matches:
            if match[0] != '' and sum:
                result += int(match[1]) * int(match[2])
            elif match[3] == "do()":
                sum = True
            elif match[4] == "don't()":
                sum = False
    
    return result

print(parse())