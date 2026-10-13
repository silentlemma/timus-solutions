use std::f64::consts::PI;
use std::io::{self, Read};

const TURN: f64 = 2.0 * PI;

/// Signed area of the unit disk at the origin inside the triangle (origin, a, b).
fn cut(ax: f64, ay: f64, bx: f64, by: f64) -> f64 {
    let (dx, dy) = (bx - ax, by - ay);
    let (qa, qb, qc) = (
        dx * dx + dy * dy,
        ax * dx + ay * dy,
        ax * ax + ay * ay - 1.0,
    );
    let mut marks = vec![0.0, 1.0];
    let disc = qb * qb - qa * qc;
    if disc > 0.0 {
        let root = disc.sqrt();
        for t in [(-qb - root) / qa, (-qb + root) / qa] {
            if t > 0.0 && t < 1.0 {
                marks.push(t);
            }
        }
    }
    marks.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut area = 0.0;
    for w in marks.windows(2) {
        let (s, t) = (w[0], w[1]);
        let (px, py, qx, qy) = (ax + dx * s, ay + dy * s, ax + dx * t, ay + dy * t);
        let (mx, my) = ((px + qx) / 2.0, (py + qy) / 2.0);
        let cross = px * qy - py * qx;
        // a piece inside the disk adds its triangle, one outside adds its sector
        area += if mx * mx + my * my < 1.0 {
            cross / 2.0
        } else {
            cross.atan2(px * qx + py * qy) / 2.0
        };
    }
    area
}

/// Water that one umbrella moves off or onto the field.
fn change(x: f64, y: f64, width: f64, length: f64) -> f64 {
    let corners = [
        (-x, -y),
        (length - x, -y),
        (length - x, width - y),
        (-x, width - y),
    ];
    let mut covered = 0.0;
    for i in 0..corners.len() {
        let (a, b) = (corners[(i + corners.len() - 1) % corners.len()], corners[i]);
        covered += cut(a.0, a.1, b.0, b.1);
    }
    // the rim splits into arcs at the field's border lines
    let mut angles = vec![0.0, TURN];
    for d in [-x, length - x] {
        if d.abs() <= 1.0 {
            angles.push(d.acos());
            angles.push(TURN - d.acos());
        }
    }
    for d in [-y, width - y] {
        if d.abs() <= 1.0 {
            angles.push((d.asin() + TURN) % TURN);
            angles.push(PI - d.asin());
        }
    }
    angles.sort_by(|a, b| a.partial_cmp(b).unwrap());
    let mut inside = 0.0;
    for w in angles.windows(2) {
        let m = (w[0] + w[1]) / 2.0;
        let (px, py) = (x + m.cos(), y + m.sin());
        if px >= 0.0 && px <= length && py >= 0.0 && py <= width {
            inside += w[1] - w[0];
        }
    }
    // rain caught over the whole disk leaves from the rim evenly by angle
    PI * inside / TURN - covered
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_whitespace();
    let width: f64 = it.next().unwrap().parse().unwrap();
    let length: f64 = it.next().unwrap().parse().unwrap();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut total = width * length;
    for _ in 0..n {
        let x: f64 = it.next().unwrap().parse().unwrap();
        let y: f64 = it.next().unwrap().parse().unwrap();
        total += change(x, y, width, length);
    }
    println!("{:.3}", total);
}
