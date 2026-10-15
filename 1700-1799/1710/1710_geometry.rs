use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut words = text.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (ax, ay, bx, by, cx, cy) = (next(), next(), next(), next(), next(), next());
    // C' on the ray AC with |BC'| = |BC| is the other root t of
    // t^2 - 2 t (AB . u) + |AB|^2 - |BC|^2 = 0, u the unit vector along AC:
    // t' = 2 (AB . AC) / |AC| - |AC|, so C' = A + (C - A) (2 dot - |AC|^2) / |AC|^2
    let dot = (bx - ax) * (cx - ax) + (by - ay) * (cy - ay);
    let side = (cx - ax) * (cx - ax) + (cy - ay) * (cy - ay);
    if 2 * dot <= side || dot == side {
        println!("YES");
        return;
    }
    let k = (2 * dot - side) as f64 / side as f64;
    println!("NO");
    println!("{:.10} {:.10}", ax as f64, ay as f64);
    println!("{:.10} {:.10}", bx as f64, by as f64);
    println!("{:.10} {:.10}", ax as f64 + (cx - ax) as f64 * k, ay as f64 + (cy - ay) as f64 * k);
}
