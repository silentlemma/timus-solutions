use std::io::{self, Read};

const SNAPSHOT_AGE: f64 = 60.0;

type Point = (i64, i64);

fn rotate_polygon(points: &mut Vec<Point>) {
    let start = (0..points.len())
        .min_by_key(|&i| (points[i].1, points[i].0))
        .unwrap();
    points.rotate_left(start);
    points.push(points[0]);
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let m: usize = tokens.next().unwrap().parse().unwrap();
    let mut airport = Vec::with_capacity(n + 1);
    let mut cloud = Vec::with_capacity(m + 1);
    for _ in 0..n {
        airport.push((
            tokens.next().unwrap().parse::<i64>().unwrap(),
            tokens.next().unwrap().parse::<i64>().unwrap(),
        ));
    }
    for _ in 0..m {
        cloud.push((
            -tokens.next().unwrap().parse::<i64>().unwrap(),
            -tokens.next().unwrap().parse::<i64>().unwrap(),
        ));
    }
    rotate_polygon(&mut airport);
    rotate_polygon(&mut cloud);
    let (mut x, mut y) = (airport[0].0 + cloud[0].0, airport[0].1 + cloud[0].1);
    let (mut i, mut j) = (0, 0);
    let mut distance = f64::INFINITY;
    while i < n || j < m {
        let (ax, ay) = if i < n {
            (
                airport[i + 1].0 - airport[i].0,
                airport[i + 1].1 - airport[i].1,
            )
        } else {
            (0, 0)
        };
        let (bx, by) = if j < m {
            (cloud[j + 1].0 - cloud[j].0, cloud[j + 1].1 - cloud[j].1)
        } else {
            (0, 0)
        };
        let turn = ax * by - ay * bx;
        let take_airport = i < n && (j == m || turn >= 0);
        let take_cloud = j < m && (i == n || turn <= 0);
        let dx = if take_airport { ax } else { 0 } + if take_cloud { bx } else { 0 };
        let dy = if take_airport { ay } else { 0 } + if take_cloud { by } else { 0 };
        let candidate = (x * dy - y * dx) as f64 / (dx as f64).hypot(dy as f64);
        distance = distance.min(candidate);
        x += dx;
        y += dy;
        i += usize::from(take_airport);
        j += usize::from(take_cloud);
    }
    println!("{:.10}", (distance - SNAPSHOT_AGE).max(0.0));
}
