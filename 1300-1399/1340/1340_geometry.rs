use std::f64::consts::PI;
use std::io::{self, Read};

const TURN: f64 = 2.0 * PI;
const EPS: f64 = 1e-9;

// an arc angle in [0, 2 pi), with angles a hair below a full turn taken
// as no turn at all
fn ahead(angle: f64) -> f64 {
    let a = angle.rem_euclid(TURN);
    if a > TURN - EPS {
        0.0
    } else {
        a
    }
}

// the points where the circles around a and b of radii ra and rb meet
fn circle_cross(a: (f64, f64), ra: f64, b: (f64, f64), rb: f64) -> Vec<(f64, f64)> {
    let d = (b.0 - a.0).hypot(b.1 - a.1);
    if d == 0.0 || d > ra + rb + EPS || d < (ra - rb).abs() - EPS {
        return Vec::new();
    }
    let along = (ra * ra - rb * rb + d * d) / (2.0 * d);
    let side = (ra * ra - along * along).max(0.0).sqrt();
    let (ux, uy) = ((b.0 - a.0) / d, (b.1 - a.1) / d);
    let (mx, my) = (a.0 + ux * along, a.1 + uy * along);
    vec![
        (mx - uy * side, my + ux * side),
        (mx + uy * side, my - ux * side),
    ]
}

fn shortest(x: f64, y: f64, heading: f64, r: f64, kx: f64, ky: f64) -> f64 {
    if r == 0.0 {
        return (kx - x).hypot(ky - y);
    }
    let mut best = f64::INFINITY;
    // sign 1 turns left (counter-clockwise), sign -1 turns right
    for sign in [1.0, -1.0] {
        let (cx, cy) = (x - sign * r * heading.sin(), y + sign * r * heading.cos());
        // where the cockroach is on the circle
        let start = (y - cy).atan2(x - cx);

        // an arc, then straight along the tangent to the crumb
        let d = (kx - cx).hypot(ky - cy);
        if d >= r - EPS {
            let run = (d * d - r * r).max(0.0).sqrt();
            let leave = (ky - cy).atan2(kx - cx) - sign * (r / d).min(1.0).acos();
            best = best.min(r * ahead(sign * (leave - start)) + run);
        }
        // an arc, then an arc the other way around a circle 2r further out
        // that passes through the crumb
        for (ox, oy) in circle_cross((cx, cy), 2.0 * r, (kx, ky), r) {
            let sw = (oy - cy).atan2(ox - cx);
            let first = ahead(sign * (sw - start));
            let back = sw + PI; // the switch point seen from the new center
            let end = (ky - oy).atan2(kx - ox);
            best = best.min(r * (first + ahead(-sign * (end - back))));
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
    println!("{:.4}", shortest(x, y, a.to_radians(), r.abs(), kx, ky));
}
