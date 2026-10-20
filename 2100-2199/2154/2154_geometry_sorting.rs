use std::cmp::Ordering;
use std::io::{self, Read};

const SPACE: u8 = b' ';
const MINUS: u8 = b'-';
const ZERO: u8 = b'0';

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
    nx: i64,
    ny: i64,
}

struct Input {
    data: Vec<u8>,
    position: usize,
}

impl Input {
    fn next_int(&mut self) -> i64 {
        while self.position < self.data.len() && self.data[self.position] <= SPACE {
            self.position += 1;
        }
        let mut sign = 1;
        if self.data[self.position] == MINUS {
            sign = -1;
            self.position += 1;
        }
        let mut value = 0;
        while self.position < self.data.len() && self.data[self.position] > SPACE {
            value = value * 10 + i64::from(self.data[self.position] - ZERO);
            self.position += 1;
        }
        value * sign
    }
}

fn distance(a: Point, b: Point) -> f64 {
    let area = (a.x * b.y - a.y * b.x).abs();
    let dx = a.x - b.x;
    let dy = a.y - b.y;
    area as f64 / ((dx * dx + dy * dy) as f64).sqrt()
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, position: 0 };
    let n = input.next_int() as usize;
    let mut points = Vec::with_capacity(n);
    let mut has_origin = false;
    for _ in 0..n {
        let x = input.next_int();
        let y = input.next_int();
        let (nx, ny) = if y < 0 || y == 0 && x < 0 {
            (-x, -y)
        } else {
            (x, y)
        };
        points.push(Point { x, y, nx, ny });
        has_origin |= x == 0 && y == 0;
    }
    let mut answer = 0.0;
    if !has_origin {
        // Opposite rays have the same direction modulo a half turn.
        points.sort_unstable_by(|a, b| {
            let cross = a.nx * b.ny - a.ny * b.nx;
            if cross > 0 {
                Ordering::Less
            } else if cross < 0 {
                Ordering::Greater
            } else {
                Ordering::Equal
            }
        });
        answer = f64::INFINITY;
        for i in 0..n {
            answer = answer.min(distance(points[i], points[(i + 1) % n]));
        }
    }
    println!("{:.10}", answer);
}
