use std::io::{self, Read, Write};

const CORNERS: usize = 4;
const TETRAHEDRON: f64 = 6.0; // a corner with legs a, b, c cuts off abc/6

fn volume(side: i64, h: &[i64]) -> String {
    // the surface is a plane, so the levels at opposite corners add up to
    // the same sum; a sensor reads max(0, level), and 0 hides the level
    let dry: Vec<usize> = (0..CORNERS).filter(|&i| h[i] == 0).collect();
    let mut diagonal = [0i64; 2];
    let mut hidden = [false; 2];
    for (i, &v) in h.iter().enumerate() {
        diagonal[i % 2] += v;
        hidden[i % 2] |= v == 0;
    }
    let total: i64 = h.iter().sum();
    let area = side as f64 * side as f64;
    if dry.len() == CORNERS {
        return "0.000000".to_string();
    }
    if dry.is_empty() {
        if diagonal[0] != diagonal[1] {
            return "error".to_string();
        }
        return format!("{:.6}", area * total as f64 / CORNERS as f64);
    }
    if dry.len() == 1 {
        let at = dry[0];
        let (left, far) = (h[(at + 1) % CORNERS], h[(at + 2) % CORNERS]);
        let right = h[(at + CORNERS - 1) % CORNERS];
        let x = left + right - far;
        if x > 0 {
            return "error".to_string();
        }
        // the plane dips below the bottom at the dry corner in a tetrahedron
        // with legs -x up and -x/(left - x), -x/(right - x) along the edges,
        // so that much negative water is added back
        let dip = -(x as f64);
        let level = (total + x) as f64 / CORNERS as f64
            + dip * dip * dip / (TETRAHEDRON * (left - x) as f64 * (right - x) as f64);
        return format!("{:.6}", area * level);
    }
    // two or more hidden levels: they only have to be at most 0 and keep
    // the two diagonal sums equal, and when that is possible they can move
    if hidden[0] && hidden[1] {
        return "ambiguous".to_string();
    }
    let low = if hidden[0] { 0 } else { 1 };
    if diagonal[1 - low] > diagonal[low] { "error" } else { "ambiguous" }.to_string()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let t = match it.next() {
        Some(v) => v,
        None => return,
    };
    let mut out = String::new();
    for _ in 0..t {
        let side = it.next().unwrap();
        let h: Vec<i64> = (0..CORNERS).map(|_| it.next().unwrap()).collect();
        out.push_str(&volume(side, &h));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
