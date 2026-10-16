use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_ascii_whitespace().map(|w| w.parse::<i64>().unwrap());
    let mut next = || words.next().unwrap();
    let (n, m, a, b, r, s) = (next(), next() as usize, next(), next(), next(), next());
    // bus i takes the fans after the border P(i-1) up to the border P(i), with
    // P(0) = 0, P(m) = n and a <= P(i) - P(i-1) <= b; a fan in bus f puts
    // P(f) at or above them and P(f-1) below them
    let mut lo = vec![0i64; m + 1];
    let mut hi = vec![n; m + 1];
    hi[0] = 0;
    lo[m] = n;
    for _ in 0..s {
        let (fan, bus) = (next(), next() as usize);
        lo[bus] = lo[bus].max(fan);
        hi[bus - 1] = hi[bus - 1].min(fan - 1);
    }
    // the borders reachable from the left end and from the right end each
    // form a range, and a border is possible when it is in both
    for i in 1..=m {
        lo[i] = lo[i].max(lo[i - 1] + a);
        hi[i] = hi[i].min(hi[i - 1] + b);
    }
    for i in (0..m).rev() {
        lo[i] = lo[i].max(lo[i + 1] - b);
        hi[i] = hi[i].min(hi[i + 1] - a);
    }
    if (0..=m).any(|i| lo[i] > hi[i]) {
        println!("IMPOSSIBLE");
        return;
    }
    // fan r rides in bus k when some P(k-1) below r and P(k) at or above r
    // are possible borders a to b apart
    let buses: Vec<String> = (1..=m)
        .filter(|&k| {
            let (x_lo, x_hi) = (lo[k - 1], hi[k - 1].min(r - 1));
            let (y_lo, y_hi) = (lo[k].max(r), hi[k]);
            x_lo <= x_hi && y_lo <= y_hi && y_hi - x_lo >= a && y_lo - x_hi <= b
        })
        .map(|k| k.to_string())
        .collect();
    println!("{}\n{}", buses.len(), buses.join(" "));
}
