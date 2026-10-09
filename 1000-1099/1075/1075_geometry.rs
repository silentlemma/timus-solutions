use std::io::{self, Read};

const DIM: usize = 3;

type Vec3 = [f64; DIM];

fn sub(a: Vec3, b: Vec3) -> Vec3 {
    [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
}

fn dot(a: Vec3, b: Vec3) -> f64 {
    a[0] * b[0] + a[1] * b[1] + a[2] * b[2]
}

fn cross(a: Vec3, b: Vec3) -> Vec3 {
    [
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    ]
}

fn norm(a: Vec3) -> f64 {
    dot(a, a).sqrt()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut read = || [it.next().unwrap(), it.next().unwrap(), it.next().unwrap()];
    let (a, b, c) = (read(), read(), read());
    let r = it.next().unwrap();
    let (u, v) = (sub(a, c), sub(b, c));
    let angle = norm(cross(u, v)).atan2(dot(u, v));
    let (da, db) = (norm(u), norm(v));
    // seen from C, the tangents from A and B cover these angles; when the angle
    // ACB fits in them, the segment AB misses the ball
    let reach = (r / da).acos() + (r / db).acos();
    let mut length = norm(sub(a, b));
    if angle > reach {
        length = (da * da - r * r).sqrt() + (db * db - r * r).sqrt() + r * (angle - reach);
    }
    println!("{:.2}", length);
}
