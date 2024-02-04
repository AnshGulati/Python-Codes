def doubler(x):
    return x*2
L = [1, 2, 3, 4, 5, 6]
mod_list = map(doubler, L)
print(list(mod_list))