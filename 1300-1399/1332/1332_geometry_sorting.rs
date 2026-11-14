use std::f64::consts::TAU;
use std::io::{self, Read, Write};

const EPS: f64 = 1e-12;

fn most_cities(points: &[(i32, i32)], reach: i32) -> usize {
    if reach < 0 || points.is_empty() {
        return 0;
    }
    if reach == 0 {
        return 1;
    }
    let diameter = 2 * reach;
    let limit = diameter * diameter;
    let mut events = Vec::with_capacity(2 * (points.len() - 1));
    let mut best = 1;
    for &(x, y) in points {
        events.clear();
        let mut active = 1;
        for &(a, b) in points {
            let (dx, dy) = (a - x, b - y);
            let squared = dx * dx + dy * dy;
            if squared == 0 || squared > limit {
                continue;
            }
            let direction = f64::from(dy).atan2(f64::from(dx));
            let half_width = (f64::from(squared).sqrt() / f64::from(diameter)).acos();
            let start = (direction - half_width - EPS).rem_euclid(TAU);
            let end = (direction + half_width + EPS).rem_euclid(TAU);
            active += usize::from(start > end);
            events.push((start, false));
            events.push((end, true));
        }
        // Start events precede end events at the same angle.
        events.sort_unstable_by(|a, b| a.0.partial_cmp(&b.0).unwrap().then(a.1.cmp(&b.1)));
        best = best.max(active);
        for &(_, end) in &events {
            if end {
                active -= 1;
            } else {
                active += 1;
                best = best.max(active);
            }
        }
        if best == points.len() {
            break;
        }
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_ascii_whitespace()
        .map(|token| token.parse::<i32>().unwrap());
    let count = values.next().unwrap();
    let points: Vec<_> = (0..count)
        .map(|_| (values.next().unwrap(), values.next().unwrap()))
        .collect();
    let reach = values.next().unwrap() - values.next().unwrap();
    writeln!(io::stdout().lock(), "{}", most_cities(&points, reach)).unwrap();
}
