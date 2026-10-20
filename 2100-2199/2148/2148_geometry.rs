use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let mut next = || it.next().unwrap();
    let (cx, cy, r) = (next(), next(), next());
    let (ax, ay, bx, by) = (next(), next(), next(), next());
    // The players are equally far from the centre, so the mirror point lies on
    // the bisector of the angle between them, in the direction w = A + B - 2C.
    let (wx, wy) = (ax + bx - 2 * cx, ay + by - 2 * cy);
    // Both shots stay outside the tank exactly when each player is strictly
    // beyond the tangent line at that point: (A - C) . w > r |w|.
    let dot = (ax - cx) * wx + (ay - cy) * wy;
    let norm = wx * wx + wy * wy;
    if dot <= 0 || dot * dot <= r * r * norm {
        println!("No way");
        return;
    }
    let scale = r as f64 / (norm as f64).sqrt();
    println!("{:.9} {:.9}", cx as f64 + wx as f64 * scale, cy as f64 + wy as f64 * scale);
}
