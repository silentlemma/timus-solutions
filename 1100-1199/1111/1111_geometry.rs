use std::io::{self, Read};

// squared distances carry these denominators: a point scaled by 2, a square
// by its projections
const POINT_DEN: i64 = 4;
const SQUARE_DEN: i64 = 8;

// squared distance from P to the square with diagonal (x1, y1)-(x2, y2), as a
// numerator and a denominator
fn distance(x1: i64, y1: i64, x2: i64, y2: i64, px: i64, py: i64) -> (i128, i128) {
    // doubled coordinates of P relative to the centre, and the diagonal
    let (qx, qy) = (2 * px - x1 - x2, 2 * py - y1 - y2);
    let (dx, dy) = (x2 - x1, y2 - y1);
    let h = dx * dx + dy * dy;
    if h == 0 {
        return ((qx * qx + qy * qy) as i128, POINT_DEN as i128);
    }
    // projections on the two side directions, the diagonal turned by +-45
    // degrees; inside the square both stay within h
    let s1 = (qx * (dx - dy) + qy * (dy + dx)).abs();
    let s2 = (qx * (dx + dy) + qy * (dy - dx)).abs();
    let (a, b) = ((s1 - h).max(0), (s2 - h).max(0));
    ((a * a + b * b) as i128, (SQUARE_DEN * h) as i128)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tok = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<i64>().unwrap());
    let mut next = || tok.next().unwrap();
    let n = next() as usize;
    let squares: Vec<(i64, i64, i64, i64)> =
        (0..n).map(|_| (next(), next(), next(), next())).collect();
    let (px, py) = (next(), next());
    let dist: Vec<(i128, i128)> = squares
        .iter()
        .map(|&(x1, y1, x2, y2)| distance(x1, y1, x2, y2, px, py))
        .collect();
    // the cross products reach about 10^28, hence 128 bits; the sort is stable
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&i, &j| (dist[i].0 * dist[j].1).cmp(&(dist[j].0 * dist[i].1)));
    let out: Vec<String> = order.iter().map(|i| (i + 1).to_string()).collect();
    println!("{}", out.join(" "));
}
