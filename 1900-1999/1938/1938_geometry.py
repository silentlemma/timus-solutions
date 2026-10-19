import math
import sys

LINE_COUNT = 3
COORDINATES_PER_LINE = 4
END_Y_INDEX = 3
ROTATION_COSINE = 0.5
ROTATION_SINE = math.sqrt(3.0) / 2
OUTPUT_DIGITS = 15


def cross(first, second):
    return first[0] * second[1] - first[1] * second[0]


def rotate(vector, orientation):
    cosine, sine = ROTATION_COSINE, orientation * ROTATION_SINE
    return cosine * vector[0] - sine * vector[1], sine * vector[0] + cosine * vector[1]


def equilateral_points(lines):
    first, second, third = lines
    anchor_second = second[0], second[1]
    direction_second = second[2] - second[0], second[END_Y_INDEX] - second[1]
    anchor_third = third[0], third[1]
    direction_third = third[2] - third[0], third[END_Y_INDEX] - third[1]
    beginning, ending = (first[0], first[1]), (first[2], first[END_Y_INDEX])
    beginning_offset = beginning[0] - second[0], beginning[1] - second[1]
    ending_offset = ending[0] - second[0], ending[1] - second[1]
    base = (
        beginning
        if abs(cross(direction_second, beginning_offset))
        >= abs(cross(direction_second, ending_offset))
        else ending
    )
    positive = rotate(direction_second, 1)
    negative = rotate(direction_second, -1)
    orientation, direction = (
        (1, positive)
        if abs(cross(positive, direction_third))
        >= abs(cross(negative, direction_third))
        else (-1, negative)
    )
    rotated_offset = rotate((second[0] - base[0], second[1] - base[1]), orientation)
    rotated_anchor = base[0] + rotated_offset[0], base[1] + rotated_offset[1]
    delta = third[0] - rotated_anchor[0], third[1] - rotated_anchor[1]
    determinant = cross(direction, direction_third)
    second_parameter = cross(delta, direction_third) / determinant
    third_parameter = cross(delta, direction) / determinant
    point_second = (
        anchor_second[0] + second_parameter * direction_second[0],
        anchor_second[1] + second_parameter * direction_second[1],
    )
    point_third = (
        anchor_third[0] + third_parameter * direction_third[0],
        anchor_third[1] + third_parameter * direction_third[1],
    )
    return base, point_second, point_third


def main():
    values = list(map(int, sys.stdin.buffer.read().split()))
    lines = [
        values[start : start + COORDINATES_PER_LINE]
        for start in range(0, LINE_COUNT * COORDINATES_PER_LINE, COORDINATES_PER_LINE)
    ]
    for x, y in equilateral_points(lines):
        print(f"{x:.{OUTPUT_DIGITS}f} {y:.{OUTPUT_DIGITS}f}")


if __name__ == "__main__":
    main()
