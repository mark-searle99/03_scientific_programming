#!/usr/bin/env python
# -*- coding: utf-8 -*-


from geometry import MyPolygon


def test_coordinates():
    # Given
    coordinates = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    # When
    my_poly = MyPolygon(coordinates)
    # Then
    assert my_poly.coordinates == coordinates


def test_envelope():
    assert False
