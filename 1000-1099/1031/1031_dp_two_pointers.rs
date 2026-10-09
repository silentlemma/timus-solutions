use std::io::{self, Read};

const KINDS: usize = 3;
// the input: lengths, prices, then N and the two stations, then positions
const QUERY: usize = 2 * KINDS;
const POSITIONS: usize = QUERY + 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (length, price) = (&v[..KINDS], &v[KINDS..QUERY]);
    let header = &v[QUERY..POSITIONS];
    let (n, mut a, mut b) = (header[0] as usize, header[1] as usize, header[2] as usize);
    let mut x = vec![0i64; 2];
    x.extend_from_slice(&v[POSITIONS..POSITIONS + n - 1]);
    if a > b {
        std::mem::swap(&mut a, &mut b);
    }
    // cost[i]: the cheapest way from a to i; it never decreases along the
    // line, so for every kind of ticket the farthest start in reach is best
    let mut cost = vec![0i64; n + 1];
    let mut from = [a; KINDS];
    for i in a + 1..=b {
        let mut best = i64::MAX;
        for k in 0..KINDS {
            while x[i] - x[from[k]] > length[k] {
                from[k] += 1;
            }
            if from[k] < i {
                best = best.min(cost[from[k]] + price[k]);
            }
        }
        cost[i] = best;
    }
    println!("{}", cost[b]);
}
