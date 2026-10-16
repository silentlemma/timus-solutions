use std::f64::consts::PI;
use std::io::{self, Read};

// a wrong set must move by 1e-5 to become right, so one turn misses by more
// than 1e-5 / n, while right sets given to 1e-10 miss by far less
const EPS: f64 = 1e-8;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let mut pts: Vec<(f64, f64)> = (0..n)
        .map(|_| {
            let x: f64 = words.next().unwrap().parse().unwrap();
            let y: f64 = words.next().unwrap().parse().unwrap();
            (x, y)
        })
        .collect();
    let cx = pts.iter().map(|p| p.0).sum::<f64>() / n as f64;
    let cy = pts.iter().map(|p| p.1).sum::<f64>() / n as f64;
    for p in pts.iter_mut() {
        p.0 -= cx;
        p.1 -= cy;
    }
    // the vertices of a regular polygon in order turn into each other by a
    // rotation of 2 pi / n about the centre, one way or the other
    let mut ok = false;
    if pts[0].0.hypot(pts[0].1) > EPS {
        for way in [-1.0, 1.0] {
            let (s, c) = (way * 2.0 * PI / n as f64).sin_cos();
            let all = (0..n).all(|i| {
                let (x, y) = pts[i];
                let (nx, ny) = pts[(i + 1) % n];
                (nx - (x * c - y * s)).hypot(ny - (x * s + y * c)) <= EPS
            });
            if all {
                ok = true;
            }
        }
    }
    println!("{}", if ok { "YES" } else { "NO" });
}
