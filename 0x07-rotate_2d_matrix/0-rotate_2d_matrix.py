#!/usr/bin/python3
'''Rotate 2D Matrix'''


def rotate_2d_matrix(matrix):
    '''rotating a 2d matrix 90° clockwise
    Returns: Nothing'''
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            # saves topleft value
            topLeft = matrix[top][left + i]
            # moves bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]
            # moves bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]
            # moves top right to bottom right
            matrix[bottom][right - i] = matrix[top + i][right]
            # moves top left to top right
            matrix[top + i][right] = topLeft
        right -= 1
        left += 1
