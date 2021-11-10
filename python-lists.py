# Original challenge can be found here:
# https://www.hackerrank.com/challenges/python-lists/

if __name__ == '__main__':
    N = int(input())
    command_list = []
    for _ in range(N):
        command_list.append(input().split())
    
    my_list = []
    for command in command_list:
        if command[0] == "print":
            print(my_list)
            
        elif command[0] == "append":
            my_list.append(int(command[1]))
            
        elif command[0] == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        
        elif command[0] == "remove":
            my_list.remove(int(command[1]))
            
        elif command[0] == "sort":
            my_list.sort()
            
        elif command[0] == "reverse":
            my_list.reverse()
        
        elif command[0] == "pop":
            my_list.pop()
       
