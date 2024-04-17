from string import digits

for i in digits:
    for j in digits:
        for k in digits:
            for l in digits:    # noqa: E741
                print(i,j,k,l)
            