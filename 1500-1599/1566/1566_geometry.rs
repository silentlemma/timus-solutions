use std::io::{self, Read};

const EPS: f64 = 1e-9; // touching counts as fitting
const SIDES: usize = 3;

/// The third vertex of a triangle on the segment from (0, 0) to (base, 0)
/// whose other sides are left (from the origin) and right.
fn apex(base: f64, left: f64, right: f64) -> (f64, f64) {
    let x = (base * base + left * left - right * right) / (2.0 * base);
    (x, (left * left - x * x).max(0.0).sqrt())
}

/// Can the card lie with its side card[0] on the envelope's side env[0], in
/// either of its two mirror images?
fn fits_on(env: [f64; SIDES], card: [f64; SIDES]) -> bool {
    let (m, length) = (env[0], card[0]);
    if length > m + EPS {
        return false;
    }
    let (wx, height) = apex(m, env[1], env[2]);
    for (left, right) in [(card[1], card[2]), (card[2], card[1])] {
        let (u, h) = apex(length, left, right);
        if h > height + EPS {
            continue;
        }
        // the card slides along the side by t in [0, m - length]; its apex
        // (t + u, h) must stay between the envelope's two other sides
        let lo = (h * wx / height - u).max(0.0);
        let hi = (m - length).min(m - h * (m - wx) / height - u);
        if lo <= hi + EPS {
            return true;
        }
    }
    false
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let v: Vec<i64> = text
        .split_ascii_whitespace()
        .map(|w| w.parse().unwrap())
        .collect();
    let (mut e, mut c) = (v[..SIDES].to_vec(), v[SIDES..].to_vec());
    e.sort_unstable();
    c.sort_unstable();
    let fits = if e[0] + e[1] == e[2] {
        // a flat envelope holds only a flat card that is no longer
        c[0] + c[1] == c[2] && c[2] <= e[2]
    } else {
        // a triangle fits in another one exactly when it fits with one of its
        // sides lying on a side of the other
        (0..SIDES).any(|i| {
            (0..SIDES).any(|j| {
                let env = [0, 1, 2].map(|k| e[(i + k) % SIDES] as f64);
                let card = [0, 1, 2].map(|k| c[(j + k) % SIDES] as f64);
                fits_on(env, card)
            })
        })
    };
    println!("{}", if fits { "YES" } else { "NO" });
}
