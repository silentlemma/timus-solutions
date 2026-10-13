use std::io::{self, Read};

/// When the walk from start is at each node it reaches: the first moment
/// (or -1 if never) and the period, 0 for a node passed only once.
fn visits(step: &[usize], start: usize) -> (Vec<i64>, Vec<i64>) {
    let n = step.len() - 1;
    let (mut first, mut period) = (vec![-1i64; n + 1], vec![0i64; n + 1]);
    let mut order = Vec::new();
    let mut v = start;
    while first[v] < 0 {
        first[v] = order.len() as i64;
        order.push(v);
        v = step[v];
    }
    let (loop_start, len) = (first[v], order.len() as i64 - first[v]);
    for &u in &order {
        if first[u] >= loop_start {
            period[u] = len;
        }
    }
    (first, period)
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

/// x with a x = 1 (mod m), for a and m coprime.
fn inverse(a: i64, m: i64) -> i64 {
    let (mut g, mut x, mut x1, mut a1) = (m, 0i64, 1i64, a % m);
    while a1 != 0 {
        let q = g / a1;
        let t = g - q * a1;
        g = a1;
        a1 = t;
        let t = x - q * x1;
        x = x1;
        x1 = t;
    }
    (x % m + m) % m
}

/// The least moment in both sets r + k L (k >= 0), or -1.
fn first_common(mut ra: i64, mut la: i64, mut rb: i64, mut lb: i64) -> i64 {
    if la == 0 && lb == 0 {
        return if ra == rb { ra } else { -1 };
    }
    if la == 0 {
        std::mem::swap(&mut ra, &mut rb);
        std::mem::swap(&mut la, &mut lb);
    }
    if lb == 0 {
        // one moment rb against the moments ra, ra + la, ...
        return if rb >= ra && (rb - ra) % la == 0 {
            rb
        } else {
            -1
        };
    }
    let g = gcd(la, lb);
    if (rb - ra) % g != 0 {
        return -1;
    }
    let m = lb / g;
    let k = if m > 1 {
        let diff = ((rb - ra) / g % m + m) % m;
        diff * inverse(la / g % m, m) % m
    } else {
        0
    };
    let (mut t, whole) = (ra + la * k, la / g * lb);
    if t < rb {
        t += (rb - t + whole - 1) / whole * whole;
    }
    t
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    let (mut left, mut right) = (vec![0usize; n + 1], vec![0usize; n + 1]);
    for v in 1..=n {
        let mut x = it.next().unwrap();
        left[v] = x;
        let mut last = 0;
        while x != 0 {
            last = x;
            x = it.next().unwrap();
        }
        right[v] = last;
    }
    let (a, b) = (it.next().unwrap(), it.next().unwrap());
    // A always takes the leftmost road and B the rightmost
    let (first_a, period_a) = visits(&left, a);
    let (first_b, period_b) = visits(&right, b);
    let mut best = -1i64;
    for v in 1..=n {
        if first_a[v] < 0 || first_b[v] < 0 {
            continue;
        }
        let t = first_common(first_a[v], period_a[v], first_b[v], period_b[v]);
        if t >= 0 && (best < 0 || t < best) {
            best = t;
        }
    }
    println!("{}", best);
}
