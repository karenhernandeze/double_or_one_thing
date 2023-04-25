# Input Test Cases Number
tests = int(input())

for i in range(tests):
    string = input()
    v = string[0] # r  
    j = 0
    
    while j + 1 < len(string): 
        prev = v[-1] 
        next = string[j + 1] 
        difference = ord(next) - ord(prev)

        # If the difference between the one previously and the next char is greater than 0
        # it means only one character should be added, to comply with the lexicographical order 
        if difference > 0:
            v += prev + next
        elif difference < 0:
            v += next
        # This is the case, where we could have a word with two repetitive letters that are the same
        else:
            h = prev + string[j + 1:]
            g = string[j + 1:]
            if h <= g:
                v += prev + next
            else:
                v += next
        j += 1
        
    print("Case #{}: {}".format(i + 1, v))