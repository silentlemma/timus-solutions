use std::io::{self, Read};

const PERCENT: i64 = 100;
const OUTPUT_SCALE: i64 = 100000000;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<i64>().unwrap());
    let n = match it.next() {
        Some(v) => v as usize,
        None => return,
    };
    let limit = it.next().unwrap();
    let mut own = vec![0i64; n + 1];
    let mut children = vec![Vec::new(); n + 1];
    for i in 2..=n {
        let parent = it.next().unwrap() as usize;
        own[i] = it.next().unwrap();
        children[parent].push(i);
    }
    let mut order = vec![1usize];
    let mut i = 0;
    while i < order.len() {
        let v = order[i];
        order.extend_from_slice(&children[v]);
        i += 1;
    }
    let mut ready = vec![0i64; n + 1];
    let mut times = Vec::new();
    // x = 100 num/den: a noble with c vassals waits for ceil(num c/den) of
    // them, so the wait is that order statistic of their ready days
    let mut ready_by = |num: i64, den: i64| -> bool {
        for &v in order.iter().rev() {
            let c = children[v].len() as i64;
            let need = (num * c + den - 1) / den;
            let mut wait = 0;
            if need > 0 {
                times.clear();
                times.extend(children[v].iter().map(|&w| ready[w]));
                let (_, nth, _) = times.select_nth_unstable((need - 1) as usize);
                wait = *nth;
            }
            ready[v] = wait + own[v];
        }
        ready[1] <= limit
    };
    // the answer is a largest fraction m/c over the vassal counts c
    let mut seen = vec![false; n + 1];
    let mut fractions = Vec::new();
    for v in 1..=n {
        let c = children[v].len();
        if c > 0 && !seen[c] {
            seen[c] = true;
            fractions.extend((0..=c as i64).map(|m| (m, c as i64)));
        }
    }
    if fractions.is_empty() {
        fractions.push((1, 1));
    }
    fractions.sort_by(|a, b| (a.0 * b.1).cmp(&(b.0 * a.1)));
    let (mut lo, mut hi) = (0, fractions.len() - 1);
    while lo < hi {
        let mid = (lo + hi + 1) / 2;
        if ready_by(fractions[mid].0, fractions[mid].1) {
            lo = mid;
        } else {
            hi = mid - 1;
        }
    }
    let (num, den) = fractions[lo];
    let answer = (PERCENT * num * OUTPUT_SCALE + den / 2) / den;
    println!("{}.{:08}", answer / OUTPUT_SCALE, answer % OUTPUT_SCALE);
}
