use std::f64::consts::PI;
use std::io::{self, Read};

const PERCENT: f64 = 100.0;

fn cross(ax: f64, ay: f64, bx: f64, by: f64) -> f64 {
    ax * by - ay * bx
}

// signed area, positive for a counterclockwise triangle
fn triangle(a: (f64, f64), b: (f64, f64), c: (f64, f64)) -> f64 {
    cross(b.0 - a.0, b.1 - a.1, c.0 - a.0, c.1 - a.1) / 2.0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|w| w.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (big, small, near, x, y) = (next(), next(), next(), next(), next());
    let center = (x, y);
    let d = x.hypot(y);
    let (ux, uy) = (x / d, y / d);
    // the outer common tangents touch both buildings at n * radius from
    // each center, n making cos = -k with the direction to the new one
    let k = (near - small) / d;
    let s = (1.0 - k * k).sqrt();
    let mut touch = [(0.0, 0.0); 2];
    let mut end = [(0.0, 0.0); 2];
    for (i, side) in [-1.0, 1.0].iter().enumerate() {
        let nx = -k * ux - side * s * uy;
        let ny = -k * uy + side * s * ux;
        let (tx, ty) = (x + near * nx, y + near * ny);
        // the line runs away from the old building through the tangent
        // point, and leaves the city where |T + t D| = R
        let (dx, dy) = (x + (near - small) * nx, y + (near - small) * ny);
        let a = dx * dx + dy * dy;
        let b = tx * dx + ty * dy;
        let c = tx * tx + ty * ty - big * big;
        let t = (-b + (b * b - a * c).sqrt()) / a;
        touch[i] = (tx, ty);
        end[i] = (tx + t * dx, ty + t * dy);
    }
    // go around the hidden part counterclockwise: the arc of the new
    // building that faces the old one, the first tangent out to the city
    // border, along the border, the second tangent back
    let mut area = k.acos() * near * near;
    area += triangle(center, touch[0], end[0]);
    area += triangle(center, end[1], touch[1]);
    let (e1, e2) = (end[0], end[1]);
    let mut turn = cross(e1.0, e1.1, e2.0, e2.1).atan2(e1.0 * e2.0 + e1.1 * e2.1);
    if turn < 0.0 {
        turn += 2.0 * PI;
    }
    // the border arc seen from the new center: a triangle plus the piece
    // of the city cut off by the chord
    area += triangle(center, e1, e2);
    area += turn * big * big / 2.0 - triangle((0.0, 0.0), e1, e2);
    println!("{:.10}", PERCENT * area / (PI * big * big));
}
