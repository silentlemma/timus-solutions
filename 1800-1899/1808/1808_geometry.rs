use std::io::{self, Read};

const EPS: f64 = 1e-9;

fn cross(a: (f64, f64), b: (f64, f64)) -> f64 {
    a.0 * b.1 - a.1 * b.0
}

// where the refracted line of sight enters the planet and where it would
// leave it again
fn chord(r: f64, eta: f64, x: f64, y: f64, dx: f64, dy: f64) -> ((f64, f64), (f64, f64)) {
    // the first crossing of the line of sight with the circle
    let (a, half_b, c) = (dx * dx + dy * dy, x * dx + y * dy, x * x + y * y - r * r);
    let t = (-half_b - (half_b * half_b - a * c).max(0.0).sqrt()) / a;
    let (ex, ey) = (x + dx * t, y + dy * t);
    let length = dx.hypot(dy);
    let (ux, uy) = (dx / length, dy / length);
    // split the direction into the inward normal and the tangent; Snell's
    // law shrinks the tangent part by eta
    let (nx, ny) = (-ex / r, -ey / r);
    let along = ux * nx + uy * ny;
    let (tx, ty) = ((ux - along * nx) / eta, (uy - along * ny) / eta);
    let inward = (1.0 - tx * tx - ty * ty).max(0.0).sqrt();
    let (vx, vy) = (inward * nx + tx, inward * ny + ty);
    // the chord from the entry point along v has length -2 (e . v)
    let span = -2.0 * (ex * vx + ey * vy);
    ((ex, ey), (ex + vx * span, ey + vy * span))
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<f64> = input.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let [r, eta, ax, ay, adx, ady, bx, by, bdx, bdy] = v[..] else {
        return;
    };
    let (p1, q1) = chord(r, eta, ax, ay, adx, ady);
    let (p2, q2) = chord(r, eta, bx, by, bdx, bdy);
    let d1 = (q1.0 - p1.0, q1.1 - p1.1);
    let d2 = (q2.0 - p2.0, q2.1 - p2.1);
    let w = (p2.0 - p1.0, p2.1 - p1.1);
    let den = cross(d1, d2);
    let seen = if den.abs() < EPS {
        // parallel chords meet only if they lie on one line
        cross(w, d1).abs() < EPS * d1.0.hypot(d1.1).max(1.0)
    } else {
        let (s, t) = (cross(w, d2) / den, cross(w, d1) / den);
        EPS < s && s < 1.0 - EPS && EPS < t && t < 1.0 - EPS
    };
    println!("{}", if seen { "Yes" } else { "No" });
}
