# Original challenge found here:
#https://www.hackerrank.com/challenges/merge-the-tools/

def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    substring_list = [string[i : i + k] for i in range(0, n, k)]
    for substring in substring_list:
        unique_list = ""
        for char in substring:
            if char not in unique_list:
                unique_list += char
        print(unique_list)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
