use std::io::{self, Read};

const MAX_COORDINATE: i32 = 10000;
const COLUMN_COUNT: usize = (2 * MAX_COORDINATE + 1) as usize;
const GRAVITY: i32 = 10;
const HALF_GRAVITY: i32 = GRAVITY / 2;
const OUTPUT_PRECISION: usize = 9;

struct Point {
    x: i32,
    y: i32,
    wait: i32,
    best: f64,
}

fn main() {
    let mut data = String::new();
    io::stdin().read_to_string(&mut data).unwrap();
    let mut input = data
        .split_whitespace()
        .map(|token| token.parse::<i32>().unwrap());
    let n = input.next().unwrap() as usize;
    let start_x = input.next().unwrap();
    let start_y = input.next().unwrap();
    let mut points = Vec::with_capacity(n + 1);
    for _ in 0..n {
        points.push(Point {
            x: input.next().unwrap(),
            y: input.next().unwrap(),
            wait: input.next().unwrap(),
            best: 0.0,
        });
    }
    points.push(Point {
        x: start_x,
        y: start_y,
        wait: 0,
        best: 0.0,
    });
    points.sort_unstable_by_key(|point| point.y);
    let mut columns = vec![Vec::new(); COLUMN_COUNT];
    for (i, point) in points.iter().take(n).enumerate() {
        columns[(point.x + MAX_COORDINATE) as usize].push(i);
    }
    let mut fall = vec![0.0; start_y as usize + 1];
    for (drop, duration) in fall.iter_mut().enumerate() {
        *duration = (drop as f64 / HALF_GRAVITY as f64).sqrt();
    }
    for i in 0..points.len() {
        let point = &points[i];
        let mut best = fall[point.y as usize];
        let radius = (((point.y - 1) / HALF_GRAVITY) as f64).sqrt() as i32;
        let left = (point.x - radius).max(-MAX_COORDINATE);
        let right = (point.x + radius).min(MAX_COORDINATE);
        for x in left..=right {
            let dx = x - point.x;
            let drop = (HALF_GRAVITY * dx * dx).max(1);
            let height = point.y - drop;
            let column = &columns[(x + MAX_COORDINATE) as usize];
            let mut lo = 0;
            let mut hi = column.len();
            while lo < hi {
                let mid = (lo + hi) / 2;
                if points[column[mid]].y <= height {
                    lo = mid + 1;
                } else {
                    hi = mid;
                }
            }
            // A higher reachable cloud dominates all lower clouds in its column.
            if lo > 0 {
                let target = &points[column[lo - 1]];
                let candidate = fall[(point.y - target.y) as usize] + target.best;
                best = best.max(candidate);
            }
        }
        points[i].best = points[i].wait as f64 + best;
    }
    println!(
        "{:.precision$}",
        points[n].best,
        precision = OUTPUT_PRECISION
    );
}
