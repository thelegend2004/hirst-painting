import colorgram

colors = colorgram.extract("hirsty.jpeg", 30)
formatted_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    formatted_colors.append((r, b, g))

