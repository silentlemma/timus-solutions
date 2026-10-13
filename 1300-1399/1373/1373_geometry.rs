use std::io::{self, Read};

const STROKE: usize = 4; // numbers per stroke

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let data: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (mut xs, mut ys) = (Vec::new(), Vec::new());
    for s in data.chunks_exact(STROKE) {
        let (ax, ay, bx, by) = (s[0], s[1], s[2], s[STROKE - 1]);
        let (dx, dy) = (bx - ax, by - ay);
        // go (p, q), then turn clockwise and go (q, -p): p + q = dx and
        // q - p = dy give the corner a + ((dx - dy) / 2, (dx + dy) / 2), and
        // doubled coordinates keep the halves whole
        xs.extend_from_slice(&[2 * ax, 2 * bx, 2 * ax + dx - dy]);
        ys.extend_from_slice(&[2 * ay, 2 * by, 2 * ay + dx + dy]);
    }
    let span = |v: &Vec<i64>| match (v.iter().min(), v.iter().max()) {
        (Some(lo), Some(hi)) => (hi - lo) as f64 / 2.0,
        _ => 0.0,
    };
    println!("{:.4} {:.4}", span(&xs), span(&ys));
}
