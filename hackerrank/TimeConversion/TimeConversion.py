'''
status: solved
'''

def fmat(time):
    time = list(time)

    newtime = [int(time[0] + time[1]), int(time[3] + time[4]), int(time[6] + time[7])]

    if time[8] == "P":
        newtime[0] += 12

    return newtime


def demat(time):
    f1, f2, f3 = time[0] * -1, time[1] * -1, time[2] * -1

    if f1 < 0:
        f1 = 24 + f1
    if f2 < 0:
        f2 = 60 + f2
    if f3 < 0:
        f3 = 60 + f3

    ftime = str(f1) + ":" + str(f2) + ":" + str(f3)

    return ftime


def converse(t1, t2):
    t1, t2 = fmat(t1), fmat(t2)

    newt = [t1[0] - t2[0], t1[1] - t2[1], t1[2] - t1[2]]

    return demat(newt)


print(converse("07:05:45AM", "11:30:35PM"))