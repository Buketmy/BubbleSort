int_list:list = [2,4,5,1,3]
control_list:list = [2,4,5,1,3]
control_list.sort()
# if int_list[0] < int_list[1]:
#     int_list.sort()
#     print(int_list)
while True:
    for i in range(len(int_list)-1):
        first_element:int = int_list[i]
        second_element:int = int_list[i+1]
        if(first_element>second_element):
            int_list[i] = second_element
            int_list[i+1] = first_element
    print(int_list)
    if(control_list==int_list):
        break
