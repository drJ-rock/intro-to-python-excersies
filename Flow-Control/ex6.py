def all_caps(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string
    
print(all_caps('hi hello how are u?'))