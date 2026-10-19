use std::io::{self, Read};

const DIAGONAL_WEIGHT: f64 = 2.0;
const PAIR_WEIGHT: f64 = 3.0;
const NORMALIZER: f64 = 27.0;

fn expectation(vertices: &[(i64, i64)]) -> f64 {
    let (origin_x, origin_y) = vertices[0];
    let (mut previous_x, mut previous_y) = (vertices[1].0 - origin_x, vertices[1].1 - origin_y);
    let (mut weighted_x, mut weighted_y) = (0_i128, 0_i128);
    let mut doubled_area = 0_i64;
    let mut numerator = 0.0;
    for &(x, y) in &vertices[2..] {
        let (x, y) = (x - origin_x, y - origin_y);
        let area = previous_x * y - previous_y * x;
        let (sum_x, sum_y) = (previous_x + x, previous_y + y);
        let between = weighted_x * sum_y as i128 - weighted_y * sum_x as i128;
        let d = area as f64;
        numerator += DIAGONAL_WEIGHT * d * d * d + PAIR_WEIGHT * d * between as f64;
        weighted_x += area as i128 * sum_x as i128;
        weighted_y += area as i128 * sum_y as i128;
        doubled_area += area;
        previous_x = x;
        previous_y = y;
    }
    let total = doubled_area as f64;
    numerator / (NORMALIZER * total * total)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let vertices: Vec<(i64, i64)> = (0..count)
        .map(|_| {
            let x = tokens.next().unwrap().parse().unwrap();
            let y = tokens.next().unwrap().parse().unwrap();
            (x, y)
        })
        .collect();
    println!("{:.12}", expectation(&vertices));
}
