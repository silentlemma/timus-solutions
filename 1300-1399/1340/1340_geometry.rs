use std::f64::consts::PI;
use std::io::{self, Read};

const TURN: f64 = 2.0 * PI;
const FULL_TURN_DEGREES: f64 = 360.0;
const ROUND_OFF: f64 = 1e-15;

// an arc angle in [0, 2 pi)
fn ahead(angle: f64) -> f64 {
    angle.rem_euclid(TURN)
}

// the second-circle centers, using power = d squared minus r squared
// to test whether the circles meet
fn circle_cross(r: f64, cy: f64, kx: f64, ky: f64, power: f64) -> Vec<(f64, f64)> {
    if power < 0.0 || power > 8.0 * r * r {
        return Vec::new();
    }
    let d = kx.hypot(ky - cy);
    let along = (4.0 * r * r + power) / (2.0 * d);
    let side = (power * (8.0 * r * r - power)).max(0.0).sqrt() / (2.0 * d);
    let (ux, uy) = (kx / d, (ky - cy) / d);
    let (mx, my) = (ux * along, cy + uy * along);
    vec![
        (mx - uy * side, my + ux * side),
        (mx + uy * side, my - ux * side),
    ]
}

fn shortest(x: f64, y: f64, heading: f64, r: f64, kx: f64, ky: f64) -> f64 {
    let (dx, dy) = (kx - x, ky - y);
    if r * r == 0.0 || (dx == 0.0 && dy == 0.0) {
        return dx.hypot(dy);
    }
    let heading = heading.rem_euclid(FULL_TURN_DEGREES);
    let quadrant = (heading / 90.0 + 0.5).floor() as i32;
    let heading = (heading - quadrant as f64 * 90.0) * PI / 180.0;
    let mut kx = dx * heading.cos() + dy * heading.sin();
    let mut ky = -dx * heading.sin() + dy * heading.cos();
    for _ in 0..quadrant % 4 {
        let old = kx;
        kx = ky;
        ky = -old;
    }
    let mut best = f64::INFINITY;
    // sign 1 turns left (counter-clockwise), sign -1 turns right
    for sign in [1.0, -1.0] {
        let cy = sign * r;
        let mut power = dx * dx + dy * dy - 2.0 * cy * ky;
        if power < 0.0 && power >= -ROUND_OFF * (dx * dx + dy * dy) {
            power = 0.0;
        }

        // an arc, then straight along the tangent to the crumb
        if power >= 0.0 {
            let run = power.sqrt();
            let leave = kx.atan2(r - sign * ky) - run.atan2(r);
            best = best.min(r * ahead(leave) + run);
        }
        // an arc, then an arc the other way around a circle 2r further out
        // that passes through the crumb
        for (ox, oy) in circle_cross(r, cy, kx, ky, power) {
            let first = ahead(ox.atan2(r - sign * oy));
            let (vx, vy) = (-ox, cy - oy); // the switch radius, doubled
            let (ex, ey) = (kx - ox, ky - oy);
            let last = (-sign * (vx * ey - vy * ex)).atan2(vx * ex + vy * ey);
            best = best.min(r * (first + ahead(last)));
        }
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (x, y, a, r) = (next(), next(), next(), next());
    let (kx, ky) = (next(), next());
    println!("{:.4}", shortest(x, y, a, r.abs(), kx, ky));
}
