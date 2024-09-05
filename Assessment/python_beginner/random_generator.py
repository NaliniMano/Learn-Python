import random
random_list=[]
def random_gen(start,end,count):
    for x in range(count):
        random_list.append(random.randint(start,end))
    return random_list

count_of_random_no=int(input("Enter count of random number"))
random_start=int(input("Enter  random  no start range"))
random_end=int(input("Enter random no end range"))

print("Random number list",random_gen(random_start,random_end,count_of_random_no))

