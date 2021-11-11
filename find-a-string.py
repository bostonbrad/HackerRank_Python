# Original challenge found here:
# https://www.hackerrank.com/challenges/find-a-string/

def count_substring(string, sub_string):
    string_len = len(string)
    substring_len = len(sub_string)
    substring_count = 0
    for i in range(len(string)):
        if string[i : i + substring_len] == sub_string:
            substring_count += 1
    return(substring_count)
    

if __name__ == '__main__':
