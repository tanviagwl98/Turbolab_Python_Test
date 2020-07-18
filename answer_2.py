def remove_outer_layer(input_string):
    a = []
    count = 0
    for i in input_string:
        if i == '(' and count > 0:
            a.append(i)
        if  i == ')' and count > 1:
            a.append(i)
        if i == '(':
            count = count + 1
        else:
            count = count - 1        
    return "".join(a)

if __name__ == '__main__':
    input_string = input()
    result = remove_outer_layer(input_string)
    print(str(result) + '\n')
    
    
   # OUTPUT for - (())()
   # ()
