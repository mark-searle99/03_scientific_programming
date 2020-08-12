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
    # Given
    coordinates = [(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)]
    # Test polygon
    my_poly = MyPolygon(coordinates)
    # Envelope of test polygon
    my_poly_env = my_poly.envelope()
    # Run tet with list comprehension, add all elements to list that are outside of envelope
    test_list = [i for i in coordinates if i[0] < my_poly_env[0] or i[1] < my_poly_env[1] or i[0] > my_poly_env[2] or i[1] > my_poly_env[3]]
    # Assert whether list is empty
    assert not test_list

