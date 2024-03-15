def oxford_comma(items):
    if len(items) > 2:
        items[-1] = "and " + items[-1]
        return ", ".join(items)
    elif len(items) == 2:
        items.insert(-1, "and")
        return " ".join(items)
    else:
        return "".join(items)
