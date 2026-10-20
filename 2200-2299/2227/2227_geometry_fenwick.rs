use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn sum(tree: &[i64], mut end: usize) -> i64 {
    let mut result = 0;
    while end > 0 {
        result += tree[end];
        end &= end - 1;
    }
    result
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let q: usize = tokens.next().unwrap().parse().unwrap();
    let mut x = vec![0_i64; n];
    let mut y = vec![0_i64; n];
    for i in 0..n {
        x[i] = tokens.next().unwrap().parse().unwrap();
        y[i] = tokens.next().unwrap().parse().unwrap();
    }
    let cross = |a: usize, b: usize| x[a] * y[b] - y[a] * x[b];
    let mut prefix = vec![0_i64; n + 1];
    let mut removed = vec![0_i64; n + 1];
    for i in 0..n {
        prefix[i + 1] = prefix[i] + cross(i, (i + 1) % n);
    }
    let mut total = prefix[n];
    let mut output = String::new();
    for _ in 0..q {
        let kind = tokens.next().unwrap();
        let mut left = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let mut right = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        if left > right {
            std::mem::swap(&mut left, &mut right);
        }
        let mut part = prefix[right] - prefix[left] + cross(right, left);
        part -= sum(&removed, right) - sum(&removed, left);
        let other = total - part;
        let mut answer = part.max(other);
        if kind == "c" {
            answer = part.min(other);
            // Charge the discarded area to the first edge of its original arc.
            let mut i = if part < other { left } else { right } + 1;
            while i <= n {
                removed[i] += answer;
                i += i & i.wrapping_neg();
            }
            total -= answer;
        }
        let suffix = if answer % 2 == 0 { ".0" } else { ".5" };
        writeln!(output, "{}{}", answer / 2, suffix).unwrap();
    }
    print!("{}", output);
}
