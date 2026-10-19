use std::collections::BTreeSet;
use std::io::{self, Read};

const VERTEX_COUNT: usize = 4;
type Point = (i64, i64);

fn boundary_count(points: &[Point; VERTEX_COUNT]) -> usize {
    let mut boundary = BTreeSet::new();
    for shift in 0..VERTEX_COUNT {
        let (a, b);
        if shift % 2 == 0 {
            let first = shift / 2;
            let opposite = (first + 2) % VERTEX_COUNT;
            a = (2 * points[first].0, 2 * points[first].1);
            b = (2 * points[opposite].0, 2 * points[opposite].1);
        } else {
            a = (points[0].0 + points[shift].0, points[0].1 + points[shift].1);
            let remaining: Vec<usize> = (0..VERTEX_COUNT)
                .filter(|&i| i != 0 && i != shift)
                .collect();
            let (p, q) = (points[remaining[0]], points[remaining[1]]);
            b = (p.0 + q.0, p.1 + q.1);
        }
        let (dx, dy) = (b.0 - a.0, b.1 - a.1);
        if dx == 0 && dy == 0 {
            continue;
        }
        let mut valid = true;
        for (i, &p) in points.iter().enumerate() {
            let q = points[(shift + VERTEX_COUNT - i) % VERTEX_COUNT];
            if (p.0 + q.0 - a.0) * dy != (p.1 + q.1 - a.1) * dx
                || (p.0 - q.0) * dx + (p.1 - q.1) * dy != 0
            {
                valid = false;
                break;
            }
        }
        if valid {
            boundary.insert(a);
            boundary.insert(b);
        }
    }
    boundary.len()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let mut points = [(0, 0); VERTEX_COUNT];
    for point in &mut points {
        *point = (
            words.next().unwrap().parse().unwrap(),
            words.next().unwrap().parse().unwrap(),
        );
    }
    println!("{}", boundary_count(&points));
}
