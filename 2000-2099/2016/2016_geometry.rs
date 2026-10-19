use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

const DIMENSIONS: usize = 3;
const CIRCLES: usize = 3;
const PERIOD_SHIFTS: i32 = 2;
const TAU: f64 = 2.0 * std::f64::consts::PI;
type Vector = [f64; DIMENSIONS];

fn add(mut a: Vector, b: Vector) -> Vector {
    for i in 0..DIMENSIONS {
        a[i] += b[i];
    }
    a
}
fn sub(mut a: Vector, b: Vector) -> Vector {
    for i in 0..DIMENSIONS {
        a[i] -= b[i];
    }
    a
}
fn scale(mut a: Vector, value: f64) -> Vector {
    for x in &mut a {
        *x *= value;
    }
    a
}
fn sum_three(a: f64, b: f64, c: f64) -> f64 {
    let (mut sum, mut correction) = (0_f64, 0_f64);
    for value in [a, b, c] {
        let next = sum + value;
        correction += if sum.abs() >= value.abs() {
            (sum - next) + value
        } else {
            (value - next) + sum
        };
        sum = next;
    }
    sum + correction
}
fn dot(a: Vector, b: Vector) -> f64 {
    sum_three(a[0] * b[0], a[1] * b[1], a[2] * b[2])
}
fn cross(a: Vector, b: Vector) -> Vector {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}
fn unit(a: Vector) -> (Vector, f64) {
    let length = dot(a, a).sqrt();
    (scale(a, 1.0 / length), length)
}
fn above(
    center: Vector,
    radius: f64,
    radial: Vector,
    tangent: Vector,
    angle: f64,
    height: f64,
) -> f64 {
    let amplitude = radius * radial[2].hypot(tangent[2]);
    if amplitude == 0.0 {
        return if center[2] >= height {
            radius * angle
        } else {
            0.0
        };
    }
    let ratio = (height - center[2]) / amplitude;
    if ratio <= -1.0 {
        return radius * angle;
    }
    if ratio >= 1.0 {
        return 0.0;
    }
    let (half, phase, mut measure) = (ratio.acos(), tangent[2].atan2(radial[2]), 0.0);
    for shift in -PERIOD_SHIFTS..=PERIOD_SHIFTS {
        let left = phase - half + f64::from(shift) * TAU;
        let right = phase + half + f64::from(shift) * TAU;
        measure += (angle.min(right) - 0.0_f64.max(left)).max(0.0);
    }
    radius * measure
}
fn solve(speed: f64, acceleration: f64, centers: [Vector; CIRCLES]) -> f64 {
    let start = scale(centers[0], -1.0);
    let mut squared = dot(start, start);
    let (mut radial, mut radius) = unit(start);
    let mut raw = [-centers[0][1], centers[0][0], 0.0];
    let mut tangent = unit(cross(raw, radial)).0;
    let (height, mut answer) = (speed * speed / (2.0 * acceleration), 0.0);
    for i in 0..CIRCLES {
        let (mut angle, mut rho, mut distance) = (TAU, 0.0, 0.0);
        let (mut relative, mut normal, mut toward) =
            ([0.0; DIMENSIONS], [0.0; DIMENSIONS], [0.0; DIMENSIONS]);
        if i + 1 < CIRCLES {
            relative = sub(centers[i + 1], centers[i]);
            let (n, normal_length) = unit(raw);
            normal = n;
            let (direction, cross_length) = unit(cross(raw, relative));
            toward = unit(cross(direction, normal)).0;
            rho = cross_length / normal_length;
            distance = dot(relative, raw) / normal_length;
            angle = dot(toward, tangent).atan2(dot(toward, radial));
            if angle <= 0.0 {
                angle += TAU;
            }
        }
        answer += above(centers[i], radius, radial, tangent, angle, height);
        if i + 1 < CIRCLES {
            let difference = sum_three(squared, -dot(relative, relative), distance * distance);
            let delta = difference / (radius + rho);
            radius = delta.hypot(distance);
            radial = scale(
                sub(scale(toward, delta), scale(normal, distance)),
                1.0 / radius,
            );
            squared = sum_three(delta * delta, distance * distance, 0.0);
            if distance == 0.0 {
                if delta < 0.0 {
                    raw = scale(raw, -1.0);
                }
            } else {
                raw = add(scale(normal, delta), scale(toward, distance));
            }
            tangent = unit(cross(raw, radial)).0;
        }
    }
    answer
}
fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..count {
        let speed: f64 = tokens.next().unwrap().parse().unwrap();
        let acceleration: f64 = tokens.next().unwrap().parse().unwrap();
        let mut centers = [[0.0; DIMENSIONS]; CIRCLES];
        for center in &mut centers {
            for x in center {
                *x = tokens.next().unwrap().parse().unwrap();
            }
        }
        writeln!(output, "{:.12}", solve(speed, acceleration, centers)).unwrap();
    }
    print!("{}", output);
}
