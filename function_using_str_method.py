def check_string(a: str):
    if (a.replace(' ', '')).isalpha():
        if a.islower():
            return a.title()
        elif a.isupper():
            return (a.lower().split(' '))

    elif a.isalnum():
        if a.isdigit():
            return a
        else:
            return a.upper()
        
