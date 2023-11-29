def handling():
    try:

        a = 10
        b = 20
        c = 0

        d = (a+b) / c
        print(d)
    except:
        print("This is not possible")
    else:
        print("There is no exception else is executed")

    finally:
        print("Finally always executed")


handling()

