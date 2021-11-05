# Original challenge found here:
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    my_set = set(arr)
    max_element = max(my_set)
    my_set.remove(max_element)
    runner_up = max(my_set)
    print(runner_up)
