def create_name(first, last):
    """The function of this function is to add name and surname"""
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("SHERQO'ZIYEV", "SHODMON")
print(full_name)