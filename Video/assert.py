from math import sqrt, pi

# def area_squara(r):
#     assert r > 0, 'A length must be positive'
#     return r * r

# def area_circle(r):
#     assert r > 0, 'A length must be positive'
#     return pi * r * r 

# def area_hexagon(r):
#     assert r > 0, 'A length must be positive'
#     return r * r * 3 * sqrt(3) / 2

"""Generalization."""
def area_squara(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexgon(r):
    return area(r, 3 * sqrt(3) / 2)

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant


