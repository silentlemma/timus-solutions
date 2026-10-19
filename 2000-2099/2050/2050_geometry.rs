use std::io::{self, Read, Write};

const DIMENSION: usize = 3;
const POINTS: usize = 4;
const AXIS_THRESHOLD: f64 = 1900.0;
const AXIS_STEP: f64 = 2.0;
const ANGLE: usize = 180;
type Vector = [f64; DIMENSION];
type Answer = [Vector; 2];

fn dot(a: &Vector, b: &Vector) -> f64 {
    a.iter().zip(b).map(|(x, y)| x * y).sum()
}

fn normalize(mut a: Vector) -> Vector {
    let length = dot(&a, &a).sqrt();
    for value in &mut a {
        *value /= length;
    }
    a
}

fn axis(middle: Vector, displacement: Vector, direction: Vector, difference: Vector) -> Answer {
    let coefficient = dot(&displacement, &direction) / (2.0 * dot(&direction, &direction));
    let unit = normalize(direction);
    let mut center = [0.0; DIMENSION];
    for i in 0..DIMENSION {
        center[i] = middle[i] + coefficient * difference[i];
    }
    let projection = dot(&center, &unit);
    let mut result = [[0.0; DIMENSION]; 2];
    for i in 0..DIMENSION {
        result[0][i] = center[i] - projection * unit[i];
        result[1][i] = result[0][i] + AXIS_STEP * unit[i];
    }
    result
}

fn solve(points: [Vector; POINTS]) -> Answer {
    let [a, b, c, d] = points;
    let mut first = [0.0; DIMENSION];
    let mut second = first;
    let mut middle = first;
    let mut displacement = first;
    for i in 0..DIMENSION {
        first[i] = b[i] - a[i];
        second[i] = d[i] - c[i];
        middle[i] = (a[i] + c[i]) / 2.0;
        displacement[i] = c[i] - a[i];
    }
    if dot(&first, &second) < 0.0 {
        for value in &mut second {
            *value = -*value;
        }
    }
    let (u, v) = (normalize(first), normalize(second));
    let mut plus = [0.0; DIMENSION];
    let mut minus = plus;
    for i in 0..DIMENSION {
        plus[i] = u[i] + v[i];
        minus[i] = u[i] - v[i];
    }
    let mut result = axis(middle, displacement, plus, minus);
    if dot(&result[0], &result[0]) > AXIS_THRESHOLD * AXIS_THRESHOLD {
        result = axis(middle, displacement, minus, plus);
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let mut points = [[0.0; DIMENSION]; POINTS];
    for row in &mut points {
        for value in row {
            *value = tokens.next().unwrap().parse().unwrap();
        }
    }
    let mut out = io::BufWriter::new(io::stdout().lock());
    for row in solve(points) {
        writeln!(out, "{:.15} {:.15} {:.15}", row[0], row[1], row[2]).unwrap();
    }
    writeln!(out, "{}", ANGLE).unwrap();
}
