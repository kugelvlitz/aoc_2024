def get_num_safe_reports():
    safe_reports = 0
    allowed_strikes = 1 # 0 for part 1, 1 for part 2
    with open("input", "r") as f:
        index = 0
        while True:
            report = f.readline()
            index += 1
            if report:
                nums = report.replace('\n', '').split(" ")
                increasing = True
                strikes = 0
                for i in range(0, len(nums)):
                    if i == len(nums)-1:
                        if strikes == 1:
                            print(nums[i], index)
                        safe_reports += 1 
                        break
                    
                    diff = int(nums[i]) - int(nums[i+1]) 
                    if i == 0:
                        if diff > 0:
                            increasing = False
                        elif diff == 0:
                            strikes += 1
                    if abs(diff) > 3 or (diff == 0 and i != 0) or (diff > 0 and increasing == True) or (diff < 0 and increasing == False):
                        strikes += 1

                    if strikes > allowed_strikes:
                        break
            else:
                break
    
    return safe_reports

print(get_num_safe_reports())
                        