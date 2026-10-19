use std::io::{self, Read};

const NONE: i64 = i64::MIN; // an unreachable state

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_whitespace().map(|t| t.parse().unwrap()).collect();
    let (x, n) = (v[0], v[1]);
    let (a, b) = (&v[2..2 + n], &v[2 + n..2 + 2 * n]);
    // utility above x is earned whatever the order; with b capped at x a task
    // done at repaired volume r (debt x - r) earns max(0, min(x, r) - (x - b))
    let extra: i64 = b.iter().map(|&w| w.saturating_sub(x) as i64).sum();
    let need: Vec<i64> = b.iter().map(|&w| (x - w.min(x)) as i64).collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&i| a[i]);
    // some tasks are given up: they go first and only repair. The rest go by a
    // descending, so task i (ascending a) sees the given up ones before it and
    // every task from it on. best[s]: s = repair of given up tasks so far, capped
    let mut suffix = vec![0; n + 1];
    for k in (0..n).rev() {
        suffix[k] = suffix[k + 1] + a[order[k]];
    }
    let mut best = vec![NONE; x + 1];
    best[0] = 0;
    let mut from = vec![vec![(0usize, false); x + 1]; n]; // previous state, given up
    for (k, &i) in order.iter().enumerate() {
        let mut nxt = vec![NONE; x + 1];
        for s in 0..=x {
            if best[s] == NONE {
                continue;
            }
            let gain = best[s] + x.min(s + suffix[k]) as i64 - need[i];
            if gain > nxt[s] {
                nxt[s] = gain;
                from[k][s] = (s, false);
            }
            let t = x.min(s + a[i]);
            if best[s] > nxt[t] {
                nxt[t] = best[s];
                from[k][t] = (s, true);
            }
        }
        best = nxt;
    }
    let mut s = (0..=x).max_by_key(|&v| (best[v], std::cmp::Reverse(v))).unwrap();
    println!("{}", best[s] + extra);
    let (mut given_up, mut kept) = (Vec::new(), Vec::new()); // kept comes out by a descending
    for k in (0..n).rev() {
        let (prev, up) = from[k][s];
        if up {
            given_up.push(order[k] + 1);
        } else {
            kept.push(order[k] + 1);
        }
        s = prev;
    }
    given_up.extend(kept);
    let text: Vec<String> = given_up.iter().map(|i| i.to_string()).collect();
    println!("{}", text.join(" "));
}
