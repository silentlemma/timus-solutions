use std::io::{self, Read};

const CITIES: usize = 3;
const EPS: f64 = 1e-9; // a tie at the edge gives the same cost either way

fn solve(x: &[f64], y: &[f64], w: &[f64]) -> f64 {
    let cost = |mx: f64, my: f64| -> f64 {
        (0..CITIES).map(|i| w[i] * (x[i] - mx).hypot(y[i] - my)).sum()
    };
    // a city is the best place when the pull of the others, the weighted
    // unit vectors towards them, is no stronger than the weight standing on
    // that very spot
    for v in 0..CITIES {
        let (mut here, mut px, mut py) = (0.0, 0.0, 0.0);
        for i in 0..CITIES {
            let d = (x[i] - x[v]).hypot(y[i] - y[v]);
            if d == 0.0 {
                here += w[i];
            } else {
                px += w[i] * (x[i] - x[v]) / d;
                py += w[i] * (y[i] - y[v]) / d;
            }
        }
        if f64::hypot(px, py) <= here + EPS {
            return cost(x[v], y[v]);
        }
    }
    // otherwise the best point is inside: by Ptolemy's inequality
    // w2 |MB| + w3 |MC| >= w1 |MQ| for the point Q beyond BC with
    // |BQ| : |CQ| : |BC| = w3 : w2 : w1, so the answer is w1 |AQ|
    let base = (x[2] - x[1]).hypot(y[2] - y[1]);
    let (from_b, from_c) = (base * w[2] / w[0], base * w[1] / w[0]);
    let along = (from_b * from_b - from_c * from_c + base * base) / (2.0 * base);
    let height = (from_b * from_b - along * along).max(0.0).sqrt();
    let (ex, ey) = ((x[2] - x[1]) / base, (y[2] - y[1]) / base);
    let (mut nx, mut ny) = (-ey, ex);
    // Q lies on the other side of BC from A
    if (x[0] - x[1]) * nx + (y[0] - y[1]) * ny > 0.0 {
        nx = -nx;
        ny = -ny;
    }
    let (qx, qy) = (x[1] + along * ex + height * nx, y[1] + along * ey + height * ny);
    w[0] * (x[0] - qx).hypot(y[0] - qy)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|v| v.parse::<f64>().unwrap());
    let t = it.next().unwrap() as usize;
    let mut out = String::new();
    for _ in 0..t {
        let (mut x, mut y) = ([0.0; CITIES], [0.0; CITIES]);
        for i in 0..CITIES {
            x[i] = it.next().unwrap();
            y[i] = it.next().unwrap();
        }
        let w: Vec<f64> = (0..CITIES).map(|_| it.next().unwrap()).collect();
        out.push_str(&format!("{:.10}\n", solve(&x, &y, &w)));
    }
    print!("{}", out);
}
