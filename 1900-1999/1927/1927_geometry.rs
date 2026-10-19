use std::io::{self, Read};

const SEGMENT_COORDINATES: usize = 4;
type Segment = [i64; SEGMENT_COORDINATES];

fn intersection_area(first: &Segment, second: &Segment) -> f64 {
    let (vx, vy) = (
        first[2] - first[0],
        first[SEGMENT_COORDINATES - 1] - first[1],
    );
    let (wx, wy) = (
        second[2] - second[0],
        second[SEGMENT_COORDINATES - 1] - second[1],
    );
    let determinant = vx * wy - vy * wx;
    if determinant != 0 {
        let numerator = (vx * vx + vy * vy) * (wx * wx + wy * wy);
        return numerator as f64 / determinant.abs() as f64;
    }
    let a = vx * first[0] + vy * first[1];
    let b = vx * first[2] + vy * first[SEGMENT_COORDINATES - 1];
    let c = vx * second[0] + vy * second[1];
    let d = vx * second[2] + vy * second[SEGMENT_COORDINATES - 1];
    if a.min(b).max(c.min(d)) < a.max(b).min(c.max(d)) {
        -1.0
    } else {
        0.0
    }
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut values = text
        .split_whitespace()
        .map(|token| token.parse::<i64>().unwrap());
    let mut first = [0; SEGMENT_COORDINATES];
    let mut second = [0; SEGMENT_COORDINATES];
    for coordinate in &mut first {
        *coordinate = values.next().unwrap();
    }
    for coordinate in &mut second {
        *coordinate = values.next().unwrap();
    }
    println!("{:.10}", intersection_area(&first, &second));
}
