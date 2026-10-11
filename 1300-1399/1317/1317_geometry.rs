use std::io::{self, Read};

const EPS: f64 = 1e-9;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (n, h) = (next() as usize, next());
    let mut poly: Vec<(f64, f64)> = (0..n).map(|_| (next(), next())).collect();
    let (d, lx, ly) = (next(), next(), next());
    let area: f64 = (0..n)
        .map(|i| poly[i].0 * poly[(i + 1) % n].1 - poly[(i + 1) % n].0 * poly[i].1)
        .sum();
    if area < 0.0 {
        poly.reverse();
    }
    // each side as an outward normal and an offset: inside the lot
    // nx x + ny y <= c on every side
    let sides: Vec<(f64, f64, f64)> = (0..n)
        .map(|i| {
            let (a, b) = (poly[i], poly[(i + 1) % n]);
            let (nx, ny) = (b.1 - a.1, a.0 - b.0);
            (nx, ny, nx * a.0 + ny * a.1)
        })
        .collect();
    let k = next() as usize;
    let mut shot = 0;
    for _ in 0..k {
        let (px, py) = (next(), next());
        let r = (px - lx).hypot(py - ly);
        let inside = sides
            .iter()
            .all(|&(nx, ny, c)| nx * px + ny * py <= c + EPS * nx.hypot(ny) * (r + 1.0));
        if inside {
            shot += 1; // over the lot the laser always reaches it in time
            continue;
        }
        // the beam leaves the lot at horizontal distance a and must clear
        // the fence there, so it meets the stone no lower than h r / a
        let (ux, uy) = ((px - lx) / r, (py - ly) / r);
        let a = sides
            .iter()
            .filter(|&&(nx, ny, _)| nx * ux + ny * uy > 0.0)
            .map(|&(nx, ny, c)| (c - nx * lx - ny * ly) / (nx * ux + ny * uy))
            .fold(f64::INFINITY, f64::min);
        if r * r * (a * a + h * h) <= d * d * a * a * (1.0 + EPS) {
            shot += 1;
        }
    }
    println!("{}", shot);
}
