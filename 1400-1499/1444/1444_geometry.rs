use std::io::{self, Read, Write};

fn half(v: (i64, i64)) -> u8 {
    if v.1 > 0 || (v.1 == 0 && v.0 > 0) {
        0
    } else {
        1
    }
}

fn cross(a: (i64, i64), b: (i64, i64)) -> i64 {
    a.0 * b.1 - a.1 * b.0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let raw: Vec<(i64, i64)> = (0..n)
        .map(|_| (it.next().unwrap(), it.next().unwrap()))
        .collect();
    let p: Vec<(i64, i64)> = raw
        .iter()
        .map(|&(x, y)| (x - raw[0].0, y - raw[0].1))
        .collect();
    let mut order: Vec<usize> = (1..n).collect();
    // by angle around the first pumpkin, nearer first on the same ray
    order.sort_by(|&i, &j| {
        let (a, b) = (p[i], p[j]);
        half(a)
            .cmp(&half(b))
            .then_with(|| 0.cmp(&cross(a, b)))
            .then_with(|| (a.0.abs() + a.1.abs()).cmp(&(b.0.abs() + b.1.abs())))
    });
    // cut the circle after a turn of at least half a circle, if there is one:
    // then every step turns by less than that and the walk never meets itself
    let m = order.len();
    let mut start = 0;
    for k in 0..m {
        let (a, b) = (p[order[(k + m - 1) % m]], p[order[k]]);
        let c = cross(a, b);
        if c < 0 || (c == 0 && a.0 * b.0 + a.1 * b.1 < 0) {
            start = k;
        }
    }
    let mut out = format!("{}\n1\n", n);
    for k in 0..m {
        out.push_str(&(order[(start + k) % m] + 1).to_string());
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
