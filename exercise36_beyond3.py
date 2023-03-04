keys_input = input()


def function(x):
    list_of_keys = list(keys_input)
    for i in range(len(list_of_keys)):
        if x == list_of_keys[i]:
            return i+1


def dictkey_method(keys):
    dictionary = {x: function(x) for x in keys}
    print(dictionary)


dictkey_method(keys_input)
