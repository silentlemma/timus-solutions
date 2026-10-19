use std::io::{self, Read};

#[derive(Clone, Copy)]
struct Point {
    x: i64,
    y: i64,
}
struct Direction {
    key: f64,
    x: i64,
    y: i64,
    other: usize,
}

fn minimum_distance(points: &[Point]) -> f64 {
    let mut best = f64::INFINITY;
    let mut directions = Vec::with_capacity(points.len());
    for pivot in 0..points.len() - 1 {
        directions.clear();
        let (mut total_x, mut total_y) = (0_i64, 0_i64);
        for (other, p) in points.iter().enumerate() {
            let (mut dx, mut dy) = (p.x - points[pivot].x, p.y - points[pivot].y);
            if dx == 0 && dy == 0 {
                continue;
            }
            if dy < 0 || (dy == 0 && dx < 0) {
                dx = -dx;
                dy = -dy;
            }
            directions.push(Direction {
                key: -(dx as f64) / ((dx.abs() + dy) as f64),
                x: dx,
                y: dy,
                other,
            });
            total_x += dx;
            total_y += dy;
        }
        directions.sort_unstable_by(|a, b| a.key.total_cmp(&b.key));
        for d in &directions {
            if d.other > pivot {
                let numerator = d.x * total_y - d.y * total_x;
                if numerator == 0 {
                    return 0.0;
                }
                let value = (numerator as f64) / ((d.x * d.x + d.y * d.y) as f64).sqrt();
                best = best.min(value);
            }
            total_x -= 2 * d.x;
            total_y -= 2 * d.y;
        }
    }
    if best.is_finite() {
        best
    } else {
        0.0
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let points: Vec<Point> = (0..n)
        .map(|_| Point {
            x: words.next().unwrap().parse().unwrap(),
            y: words.next().unwrap().parse().unwrap(),
        })
        .collect();
    println!("{:.12}", minimum_distance(&points));
}
