use std::io::{self, Read, Write};

const KINDS: usize = 8; // cocktails as masks of three juices; 0 is unused
const INF: u32 = 1 << 30;
const JUICES: &str = "ABP";

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let mut glasses: Vec<Vec<usize>> = vec![Vec::new(); KINDS];
    for i in 1..=n {
        let word = it.next().unwrap();
        let mask = word.chars().fold(0usize, |m, c| m | 1 << JUICES.find(c).unwrap());
        glasses[mask].push(i);
    }
    // equal cocktails stand together; the cocktails present are ordered by a DP over
    // subsets, where best[used][last] counts the pourings, and a juice needs a new pouring
    // when a cocktail contains it and the previous one does not
    let present: usize = (1..KINDS).filter(|&k| !glasses[k].is_empty()).map(|k| 1 << k).sum();
    let mut best = vec![[INF; KINDS]; 1 << KINDS];
    let mut from = vec![[0usize; KINDS]; 1 << KINDS];
    for k in 1..KINDS {
        if present >> k & 1 == 1 {
            best[1 << k][k] = (k as u32).count_ones();
        }
    }
    for used in 0..1 << KINDS {
        for last in 1..KINDS {
            if best[used][last] == INF {
                continue;
            }
            for k in 1..KINDS {
                if present >> k & 1 == 0 || used >> k & 1 == 1 {
                    continue;
                }
                let cost = best[used][last] + ((k & !last) as u32).count_ones();
                let next = used | 1 << k;
                if cost < best[next][k] {
                    best[next][k] = cost;
                    from[next][k] = last;
                }
            }
        }
    }
    let mut last = (1..KINDS).min_by_key(|&k| best[present][k]).unwrap();
    let mut out = format!("{}\n", best[present][last]);
    let mut order = Vec::new();
    let mut used = present;
    while last != 0 {
        order.push(last);
        let prev = from[used][last];
        used ^= 1 << last;
        last = prev;
    }
    let arrangement: Vec<String> =
        order.iter().rev().flat_map(|&k| glasses[k].iter().map(|g| g.to_string())).collect();
    out.push_str(&arrangement.join(" "));
    out.push('\n');
    io::stdout().write_all(out.as_bytes()).unwrap();
}
