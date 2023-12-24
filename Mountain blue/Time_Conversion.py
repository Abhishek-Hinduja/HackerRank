def timeConversion(s):
    time = s[2:8]
    last_digit = s[-2:]
    first_digit = s[0:2]
    integer = int(first_digit)
    ans = ''
    if last_digit == 'PM' and integer < 12:
        integer += 12
        ans += str(integer) + time
    elif last_digit == 'PM' and integer == 12:
        ans += str(integer) + time
    if last_digit == 'AM' and integer < 12:
        ans += first_digit + time
    elif last_digit == 'AM' and integer == 12:
        integer = integer - 12
        ans += '0' + str(integer) + time
    return ans
s = "04:59:59AM"
print(timeConversion(s))
# def timeConversion(time):
#     # Write your code here
#     a = time[-2::]
#     out = ''
    
#     if a=="PM" and int(time[0:2]) != 12:
#         b = int(time[0:2])
#         c = 12 + b
#         out = str(c) + time[2:8]
#     elif a == "PM" and int(time[0:2]) == 12:
#         out = time[0:8]
        
#     if a == "AM" and int(time[0:2]) == 12:
#         b = int(time[0:2])
#         c = b - 12
#         out = '0' + str(c) + time[2:8] 
#     elif a == "AM" and 1 <= int(time[0:2]) <= 11:
#         out = time[0:8]
#     return out




# s = "07:05:45PM"  ans = "19:05:45PM"

