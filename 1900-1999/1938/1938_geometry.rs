use std::io::{self, Read};

const LINE_COUNT: usize = 3;
const COORDINATES_PER_LINE: usize = 4;
const END_Y_INDEX: usize = 3;
const OUTPUT_DIGITS: usize = 15;
const ROTATION_COSINE: f64 = 0.5;
const TRIANGLE_RADICAND: f64 = 3.0;

fn cross(first: [f64; 2], second: [f64; 2]) -> f64 {
    first[0] * second[1] - first[1] * second[0]
}

fn integer_area(line: &[i64; COORDINATES_PER_LINE], x: i64, y: i64) -> i64 {
    (line[2] - line[0]) * (y - line[1]) - (line[END_Y_INDEX] - line[1]) * (x - line[0])
}

fn rotate(vector: [f64; 2], orientation: f64) -> [f64; 2] {
    let sine = orientation * TRIANGLE_RADICAND.sqrt() / 2.0;
    [
        ROTATION_COSINE * vector[0] - sine * vector[1],
        sine * vector[0] + ROTATION_COSINE * vector[1],
    ]
}

fn equilateral_points(lines: &[[i64; COORDINATES_PER_LINE]; LINE_COUNT]) -> [[f64; 2]; LINE_COUNT] {
    let (first, second, third) = (&lines[0], &lines[1], &lines[2]);
    let use_beginning = integer_area(second, first[0], first[1]).abs()
        >= integer_area(second, first[2], first[END_Y_INDEX]).abs();
    let base = if use_beginning {
        [first[0] as f64, first[1] as f64]
    } else {
        [first[2] as f64, first[END_Y_INDEX] as f64]
    };
    let anchor_second = [second[0] as f64, second[1] as f64];
    let anchor_third = [third[0] as f64, third[1] as f64];
    let direction_second = [
        (second[2] - second[0]) as f64,
        (second[END_Y_INDEX] - second[1]) as f64,
    ];
    let direction_third = [
        (third[2] - third[0]) as f64,
        (third[END_Y_INDEX] - third[1]) as f64,
    ];
    let positive = rotate(direction_second, 1.0);
    let negative = rotate(direction_second, -1.0);
    let (orientation, direction) =
        if cross(positive, direction_third).abs() >= cross(negative, direction_third).abs() {
            (1.0, positive)
        } else {
            (-1.0, negative)
        };
    let offset = rotate(
        [anchor_second[0] - base[0], anchor_second[1] - base[1]],
        orientation,
    );
    let rotated_anchor = [base[0] + offset[0], base[1] + offset[1]];
    let delta = [
        anchor_third[0] - rotated_anchor[0],
        anchor_third[1] - rotated_anchor[1],
    ];
    let determinant = cross(direction, direction_third);
    let second_parameter = cross(delta, direction_third) / determinant;
    let third_parameter = cross(delta, direction) / determinant;
    let point_second = [
        anchor_second[0] + second_parameter * direction_second[0],
        anchor_second[1] + second_parameter * direction_second[1],
    ];
    let point_third = [
        anchor_third[0] + third_parameter * direction_third[0],
        anchor_third[1] + third_parameter * direction_third[1],
    ];
    [base, point_second, point_third]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|word| word.parse::<i64>().unwrap());
    let mut lines = [[0; COORDINATES_PER_LINE]; LINE_COUNT];
    for line in &mut lines {
        for coordinate in line {
            *coordinate = values.next().unwrap();
        }
    }
    for [x, y] in equilateral_points(&lines) {
        println!("{:.*} {:.*}", OUTPUT_DIGITS, x, OUTPUT_DIGITS, y);
    }
}
