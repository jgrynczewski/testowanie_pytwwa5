def a_sum(x, y):
    return x+y

assert a_sum(4, 5) == 9, "FAILED"
print("PASS")

assert a_sum(-3, 5) == 2, "FAILED"
print("PASS")

def kw_sum(x, y):
    return (x+y)**2

assert kw_sum(2, 2) == 16, "FAILED"
assert kw_sum(0, 0) == 0, "FAILED"
assert kw_sum(-3, -1) == 16, "FAILED"

def replace_a(s1):
    return s1.replace("a", "x")

assert "a" not in replace_a("aasaa"), "FAILED"0

# Asercje nie służą tylko do testowania

def div(x, y):
    assert y!=0, "Zero division not allowed"
    return x/y

print(div(4, ))
