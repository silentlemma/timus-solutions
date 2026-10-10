use std::collections::HashMap;
use std::io::{self, Read};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

// directions (y, x) through corners, in lowest terms, with the change of p
// and q there
fn term(
    events: &mut HashMap<(i64, i64), (i64, i64)>,
    from: (i64, i64),
    to: (i64, i64),
    dp: i64,
    dq: i64,
) {
    for (d, sign) in [(from, 1), (to, -1)] {
        let g = gcd(d.0, d.1);
        let e = events.entry((d.0 / g, d.1 / g)).or_insert((0, 0));
        e.0 += sign * dp;
        e.1 += sign * dq;
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    // a rectangle is given by its corners and delay
    const FIELDS: usize = 5;
    let n = v[0] as usize;
    let (c0, length) = (v[1 + FIELDS * n], v[2 + FIELDS * n]);
    let mut events = HashMap::new();
    // walking at angle t, a vertical line x = a is crossed after a/cos t and a
    // horizontal one y = b after b/sin t; a rectangle adds (c - c0) times
    // (exit - entry), a sum of such terms, each valid between two corners
    for r in v[1..1 + FIELDS * n].chunks(FIELDS) {
        let (x1, y1, x2, y2, c) = (r[0], r[1], r[2], r[FIELDS - 2], r[FIELDS - 1]);
        let w = c - c0;
        // out through the right side or the top, in through the left or the bottom
        term(&mut events, (y1, x2), (y2, x2), w * x2, 0);
        term(&mut events, (y2, x2), (y2, x1), 0, w * y2);
        term(&mut events, (y1, x1), (y2, x1), -w * x1, 0);
        term(&mut events, (y1, x2), (y1, x1), 0, -w * y1);
    }
    let mut order: Vec<(i64, i64)> = events.keys().cloned().collect();
    order.sort_by(|a, b| (a.0 * b.1).cmp(&(b.0 * a.1)));
    // below the lowest corner no rectangle is met at all
    let mut best_cost = (c0 * length) as f64;
    let mut best_t = (order[0].0 as f64).atan2(order[0].1 as f64) / 2.0;
    // between corners the time is c0*L + p/cos t + q/sin t: with p, q > 0 it
    // is above c0*L, otherwise monotone or concave, so corners are enough
    let (mut p, mut q) = (0i64, 0i64);
    for d in &order {
        let t = (d.0 as f64).atan2(d.1 as f64);
        let cost = (c0 * length) as f64 + p as f64 / t.cos() + q as f64 / t.sin();
        if cost < best_cost {
            best_cost = cost;
            best_t = t;
        }
        let (dp, dq) = events[d];
        p += dp;
        q += dq;
    }
    let l = length as f64;
    println!(
        "{:.6}\n{:.6} {:.6}",
        best_cost,
        l * best_t.cos(),
        l * best_t.sin()
    );
}
