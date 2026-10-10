use std::f64::consts::PI;
use std::io::{self, Read};

fn cross(o: (i64, i64), a: (i64, i64), b: (i64, i64)) -> i64 {
    (a.0 - o.0) * (b.1 - o.1) - (a.1 - o.1) * (b.0 - o.0)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let gap = it.next().unwrap() as f64;
    let mut pts: Vec<(i64, i64)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    pts.sort();
    // the shortest wall is the convex hull pushed out by L: its straight
    // parts add up to the hull perimeter, and its arcs turn once around a
    // full circle of radius L in total
    let mut hull = Vec::new();
    for _ in 0..2 {
        let mut part: Vec<(i64, i64)> = Vec::new();
        for &p in &pts {
            while part.len() >= 2 && cross(part[part.len() - 2], part[part.len() - 1], p) <= 0 {
                part.pop();
            }
            part.push(p);
        }
        part.pop();
        hull.extend(part);
        pts.reverse();
    }
    let mut length = 2.0 * PI * gap;
    for k in 0..hull.len() {
        let (a, b) = (hull[k], hull[(k + 1) % hull.len()]);
        length += ((a.0 - b.0) as f64).hypot((a.1 - b.1) as f64);
    }
    println!("{}", length.round() as i64);
}
