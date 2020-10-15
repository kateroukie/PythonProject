import random


def reverser(given_num):
    y = ""
    num_list = list(str(given_num))
    for i in range(len(num_list) - 1, -1, -1):
        y += str(num_list[i])
    return y


def palindrome(given_num):
    if given_num == int(reverser(given_num)):
        return True
    else:
        return False


def candidate_lychrel(number):
    candidates_lychrel = (295, 394, 493, 592, 689, 691, 788, 790, 887, 978, 986)
    if number in candidates_lychrel:
        return True
    else:
        return False


def create_num():
    created_num = random.randint(1, 1000)
    while created_num == 196 or created_num == 879:
        created_num = random.randint(1, 1000)
    return created_num


if __name__ == '__main__':
    mesos_oros = 0
    ekato = 100
    metritis_gia_m_o = 0
    while ekato > 0:
        ekato -= 1
        flag = False
        counter = 0
        print("Gyros " + str(100 - ekato))
        ran_num = create_num()
        lychrel = candidate_lychrel(ran_num)
        if lychrel:
            metritis_gia_m_o += 1
            print("Random number " + str(ran_num) + " is a Lychrel candidate so can't form a palindrom number" + "\n")
        while (not flag) and not lychrel:
            reversed_num = reverser(ran_num)
            whole_sum = ran_num + int(reversed_num)
            counter += 1
            print(str(ran_num) + "+" + reversed_num + "=" + str(whole_sum))
            flag = palindrome(whole_sum)
            if not flag:
                ran_num = whole_sum
        mesos_oros += counter
        ran_num += 1
        print("Number of Additions = " + str(counter) + "\n")
    print("Average of 100 loops = " + str(mesos_oros / (100-metritis_gia_m_o)) + " additions.")
    print("\n")

