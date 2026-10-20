use std::io::{self, Read};

const TRIANGLE_SIDES: usize = 3;

#[derive(Clone, Copy, Eq, Ord, PartialEq, PartialOrd)]
struct Point {
    x: i64,
    y: i64,
}

fn cross(a: Point, b: Point, c: Point) -> i64 {
    (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x)
}

fn chain_length(points: impl Iterator<Item = Point>) -> usize {
    let mut chain: Vec<Point> = Vec::new();
    for point in points {
        while chain.len() >= 2 && cross(chain[chain.len() - 2], chain[chain.len() - 1], point) < 0 {
            chain.pop();
        }
        chain.push(point);
    }
    chain.len()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut points = Vec::with_capacity(n);
    for _ in 0..n {
        points.push(Point {
            x: tokens.next().unwrap().parse().unwrap(),
            y: tokens.next().unwrap().parse().unwrap(),
        });
    }
    points.sort_unstable();

    // Keeping collinear points also gives the correct count for a single line.
    let boundary =
        chain_length(points.iter().copied()) + chain_length(points.iter().rev().copied()) - 2;
    println!("{}", TRIANGLE_SIDES * n - TRIANGLE_SIDES - boundary);
}
