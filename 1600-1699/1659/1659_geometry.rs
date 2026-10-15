use std::io::{self, Read};

const CORNERS: usize = 3;
const INNER: f64 = 0.5; // inner points go this share of the way from the centre to a vertex
const OUTER: f64 = 1.0 + INNER; // outer points go this far the opposite way

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<f64> = text.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let gx = (0..CORNERS).map(|i| v[2 * i]).sum::<f64>() / CORNERS as f64;
    let gy = (0..CORNERS).map(|i| v[2 * i + 1]).sum::<f64>() / CORNERS as f64;
    let mut out = String::new();
    for k in [INNER, -OUTER] {
        for i in 0..CORNERS {
            let (x, y) = (v[2 * i], v[2 * i + 1]);
            out.push_str(&format!("{:.10} {:.10}\n", gx + (x - gx) * k, gy + (y - gy) * k));
        }
    }
    print!("{}", out);
}
