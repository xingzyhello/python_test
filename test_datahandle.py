
def test_datahandle():
    pass
    a = 1;
    print(id(a))
    print(type(a))
    b = 2;
    print(id(1))
    print(id(2))




print("start")
test_datahandle()
print("end")


l = [1,3,5,6,7]
print(id(l))
print(id(l[:]))

ll = l
print(l)
print(ll)

ll[0] = 100
print(l)
print(ll)



