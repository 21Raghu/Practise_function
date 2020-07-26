def string_formation(s1, s2):
    if len(s2) > len(s1): s1, s2 = s2, s1 #my first string should always bigger to get the correct result.
    k = 0
    for i in s1:
        if i in s2:
            s2 = s2.replace(i, '', 1)
        else:
            k = 1
            break

    if k == 0:
        return "Yes"
    else:
        return "No"
