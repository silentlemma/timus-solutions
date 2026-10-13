use std::f64::consts::PI;
use std::io::{self, Read};

const CORNERS: usize = 3;
const WIDE: f64 = 2.0 * PI / 3.0; // 120 degrees

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let p: Vec<(f64, f64)> = v.chunks(2).map(|c| (c[0], c[1])).collect();
    let mut angle = [0.0; CORNERS];
    let mut side = [0.0; CORNERS];
    for i in 0..CORNERS {
        let (a, b, c) = (p[i], p[(i + 1) % CORNERS], p[(i + 2) % CORNERS]);
        let (ux, uy, wx, wy) = (b.0 - a.0, b.1 - a.1, c.0 - a.0, c.1 - a.1);
        angle[i] = (ux * wy - uy * wx).abs().atan2(ux * wx + uy * wy);
        side[i] = (c.0 - b.0).hypot(c.1 - b.1);
    }
    for i in 0..CORNERS {
        if angle[i] >= WIDE {
            // a corner of at least 120 degrees is the best place itself
            println!("{:.8} {:.8}", p[i].0, p[i].1);
            return;
        }
    }
    // otherwise the Fermat point: every side is seen at 120 degrees, and its
    // barycentric weights are a / sin(A + 60 degrees) and so on
    let (mut total, mut fx, mut fy) = (0.0, 0.0, 0.0);
    for i in 0..CORNERS {
        let w = side[i] / (angle[i] + PI / CORNERS as f64).sin();
        total += w;
        fx += w * p[i].0;
        fy += w * p[i].1;
    }
    println!("{:.8} {:.8}", fx / total, fy / total);
}
