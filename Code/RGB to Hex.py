
def rgb(r, g, b):
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    hex_value = "#{:02X}{:02X}{:02X}".format(r, g, b)
    return hex_value


print(rgb(0, 0, 0))
