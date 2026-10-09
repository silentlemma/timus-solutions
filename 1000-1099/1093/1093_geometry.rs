use std::io::{self, Read};

const HALF_G: f64 = 5.0;
// coefficients this small count as zero
const TINY: f64 = 1e-12;
// tolerance for times and for being strictly inside the rim
const EPS: f64 = 1e-9;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let [cx, cy, cz, nx, ny, nz, r, sx, sy, sz, vx, vy, vz] = v[..] else {
        return;
    };
    let (dx, dy, dz) = (sx - cx, sy - cy, sz - cz);
    // the dart at time t, if that time has come, is strictly inside the rim
    let inside = |t: f64| {
        if t < -EPS {
            return false;
        }
        let t = t.max(0.0);
        let (px, py, pz) = (dx + vx * t, dy + vy * t, dz + vz * t - HALF_G * t * t);
        px * px + py * py + pz * pz < r * r - EPS
    };
    // the distance to the plane, times |N|, is a t^2 + 2 h t + c; a flight that
    // never crosses the plane, even one lying in it, misses
    let a = -HALF_G * nz;
    let h = (nx * vx + ny * vy + nz * vz) / 2.0;
    let c = nx * dx + ny * dy + nz * dz;
    let hit = if a.abs() < TINY {
        h.abs() >= TINY && inside(-c / (2.0 * h))
    } else {
        let d = h * h - a * c;
        d >= -TINY && {
            let root = d.max(0.0).sqrt();
            inside((-h - root) / a) || inside((-h + root) / a)
        }
    };
    println!("{}", if hit { "HIT" } else { "MISSED" });
}
