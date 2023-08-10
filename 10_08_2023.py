# Join Method is used to iterate the list or tuple and concatenate the string
# Split Method is used to split a string into a list of substrings

### Finding the Percentage

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split() ##  * is an unpacking operator here first value assigned to name and remaining value will assigned to line
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     length = len(student_marks[query_name])
#     values = student_marks[query_name]
#     ans = 0
#     for item in values:
#         ans += item
#     ans = ans/length
#     print("{:.2f}".format(ans)) ## {::.2f}.format it is used to format the answer for 2 decimal places


# def swap_case(s):
#     Making_list = list(s)
#     swaped_case = []
#     for char in Making_list:
#         if ord(char) >= 65 and ord(char) <= 90:
#             swaped_case.append(char.lower())
#         else:
#             swaped_case.append(char.upper())
#     return "".join(swaped_case)

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     # print(result)

### Find the occurence of the substring in the string

# def count_substring(string, sub_string):
#     string_length = len(string)
#     sub_string_length = len(sub_string)
#     count = 0
#     for i in range(string_length-sub_string_length+1): ## We don't have to iterate full string 
#         if string[i:i+sub_string_length] == sub_string:
#             count += 1
#     return count

# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)