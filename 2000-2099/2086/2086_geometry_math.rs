use std::cmp::Ordering;
use std::io::{self, Read};

const QUAD: i64 = 4; // the discriminant of a t^2 + b t + c is b^2 - 4 a c

// compares sign * sqrt(disc) with the integer k exactly
fn sign_sqrt_vs(sign: i64, disc: i64, k: i64) -> Ordering {
    if sign > 0 {
        if k < 0 {
            Ordering::Greater
        } else {
            disc.cmp(&(k * k))
        }
    } else if k > 0 {
        Ordering::Less
    } else {
        (k * k).cmp(&disc)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    // tuple fields are read from left to right
    let (x, y, z) = (next(), next(), next());
    let (vx, vy, ex, ey) = (next(), next(), next(), next());
    // Stewart: the point at fraction t of the way from Denis to the hall is at
    // squared distance (1 - t) X^2 + t Y^2 - t (1 - t) Z^2 from Vanya; Eugene is
    // at d^2, so t solves z2 t^2 + b t + c = 0 with integer coefficients
    let d2 = (ex - vx) * (ex - vx) + (ey - vy) * (ey - vy);
    let z2 = z * z;
    let (b, c) = (y * y - x * x - z2, x * x - d2);
    let disc = b * b - QUAD * z2 * c;
    let mut found = Vec::new(); // t, and whether Eugene is at Denis's place
    if disc >= 0 {
        for s in [1i64, -1] {
            if s < 0 && disc == 0 {
                break;
            }
            // t = (-b + s sqrt(disc)) / (2 z2) must lie in [0, 1]
            if sign_sqrt_vs(s, disc, b) == Ordering::Less
                || sign_sqrt_vs(s, disc, 2 * z2 + b) == Ordering::Greater
            {
                continue;
            }
            let t = (-b as f64 + s as f64 * (disc as f64).sqrt()) / (2 * z2) as f64;
            found.push((t, c == 0 && sign_sqrt_vs(s, disc, b) == Ordering::Equal));
        }
    }
    // a model triangle: Vanya at 0, Denis on the x axis, the hall above it
    let (fx, fy) = (x as f64, y as f64);
    let cos_v = (x * x + y * y - z2) as f64 / (2.0 * fx * fy);
    let (hx, hy) = (fy * cos_v, fy * (1.0 - cos_v * cos_v).max(0.0).sqrt());
    let (ux, uy) = ((ex - vx) as f64, (ey - vy) as f64);
    let mut points = Vec::new();
    for &(t, at_denis) in &found {
        let (px, py) = (fx + t * (hx - fx), t * hy);
        for mirror in [1.0, -1.0] {
            if mirror < 0.0 && at_denis {
                break;
            }
            // rotate (and maybe reflect) the model so that its point lands on Eugene
            let (qx, qy) = (px, mirror * py);
            let norm = qx * qx + qy * qy;
            let (cos_r, sin_r) = ((qx * ux + qy * uy) / norm, (qx * uy - qy * ux) / norm);
            points.push((vx as f64 + cos_r * fx, vy as f64 + sin_r * fx));
        }
    }
    let mut out = format!("{}\n", points.len());
    for (px, py) in points {
        out.push_str(&format!("{:.12} {:.12}\n", px, py));
    }
    print!("{}", out);
}
