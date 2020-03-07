def get_item(a_list, idx):
    return a_list[idx]

print(get_item([1,2,3,4], 3))

def get_item2(a_list, idx):
    if idx>len(a_list)-1:
        return None
    else:
        return a_list[idx]

def get_item3(a_list, idx):
    if idx>len(a_list)-1:
        raise IndexError("Index too large")
    else:
        return a_list[idx]

def get_item4(a_list, idx):
    assert idx<len(a_list), "Index too large"
    return a_list[idx]

# print(get_item4([1,2,3,4], 4))

def factorial(n):
    if n<1:
        return 1
    res = 1
    for item in range(1, n+1):
        res *= item
    return res

def test_factorial():
    assert factorial(0)==1
    assert factorial(5)==120
    assert factorial(10)==3628800

if __name__ == "__main__":
    test_factorial()