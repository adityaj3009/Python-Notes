def fun(normal, *args, **kwargs):
    print(normal)
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print(key,value)


har = ["adi", "shravani","aditya","len"]
info = "Students are"
kw = {"adi":"monitor", "shravani":"students", "aditya":"student"}

fun(info, *har, **kw)