use std::io::{self, Read};

const MAX_N: i64 = 10000;

// the number of comparisons after which the search over n elements reaches
// index target, when every other element sends it towards the target
fn steps(n: i64, target: i64) -> i64 {
    let (mut p, mut q) = (0, n - 1);
    let mut count = 0;
    while p <= q {
        count += 1;
        let i = (p + q) / 2;
        if i == target {
            return count;
        }
        if target < i {
            q = i - 1;
        } else {
            p = i + 1;
        }
    }
    0
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (target, l) = (v[0], v[1]);
    // any array whose elements before the target are smaller and after it are
    // larger leads the search there, so only n decides the number of steps
    let mut runs: Vec<(i64, i64)> = Vec::new();
    for n in target + 1..=MAX_N {
        if steps(n, target) != l {
            continue;
        }
        match runs.last_mut() {
            Some(last) if last.1 == n - 1 => last.1 = n,
            _ => runs.push((n, n)),
        }
    }
    let mut out = format!("{}\n", runs.len());
    for (a, b) in runs {
        out.push_str(&format!("{} {}\n", a, b));
    }
    print!("{}", out);
}
