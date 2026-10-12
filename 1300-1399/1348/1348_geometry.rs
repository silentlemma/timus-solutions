use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<f64>().unwrap());
    let mut next = || it.next().unwrap();
    let (ax, ay, bx, by) = (next(), next(), next(), next());
    let (cx, cy, rope) = (next(), next(), next());
    let (dx, dy) = (bx - ax, by - ay);
    // the nearest point of the bed: C projected onto AB, kept inside it
    let length = dx * dx + dy * dy;
    let t = if length == 0.0 {
        0.0
    } else {
        (((cx - ax) * dx + (cy - ay) * dy) / length).clamp(0.0, 1.0)
    };
    let nearest = (ax + t * dx - cx).hypot(ay + t * dy - cy);
    let farthest = (ax - cx).hypot(ay - cy).max((bx - cx).hypot(by - cy));
    println!("{:.2}", (nearest - rope).max(0.0));
    println!("{:.2}", (farthest - rope).max(0.0));
}
