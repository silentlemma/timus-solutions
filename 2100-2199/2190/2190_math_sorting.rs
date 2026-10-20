use std::io::{self, Read};

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        a
    } else {
        gcd(b, a % b)
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = it.next().unwrap() as usize;
    let s: Vec<i64> = (0..n).map(|_| it.next().unwrap()).collect();
    let mut q: Vec<i64> = (0..n).map(|_| it.next().unwrap()).collect();
    let g = q.iter().fold(0, |acc, &v| gcd(acc, v));
    for v in q.iter_mut() {
        *v /= g;
    }
    // The heaps become k * q for an integer k >= 1, and the cost
    // sum |s - k q| = sum q |s / q - k| is convex in k with its real minimum
    // at the median of the ratios s / q weighted by q.
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by(|&i, &j| (s[i] * q[j]).cmp(&(s[j] * q[i])));
    let total: i64 = q.iter().sum();
    let mut weight = 0i64;
    let mut median = order[n - 1];
    for &i in &order {
        weight += q[i];
        if 2 * weight >= total {
            median = i;
            break;
        }
    }
    let low = s[median] / q[median];
    let cost = |k: i64| -> i64 { s.iter().zip(&q).map(|(&a, &b)| (a - k * b).abs()).sum() };
    let mut best = cost(low + 1);
    if low >= 1 {
        best = best.min(cost(low));
    }
    println!("{}", best);
}
