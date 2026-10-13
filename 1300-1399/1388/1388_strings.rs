use std::collections::HashMap;
use std::io::{self, Read};

const SHORT: usize = 3; // any three points on both sides match

fn gcd(a: i64, b: i64) -> i64 {
    let (mut a, mut b) = (a.abs(), b.abs());
    while b != 0 {
        let t = a % b;
        a = b;
        b = t;
    }
    a
}

/// The distinct directions as reduced p / q with q > 0, by increasing p / q.
fn directions(trees: &[(i64, i64)]) -> Vec<(i64, i64)> {
    let mut d: Vec<(i64, i64)> = trees
        .iter()
        .map(|&(x, y)| {
            let (x, y) = if y < 0 { (-x, -y) } else { (x, y) };
            let g = gcd(x, y);
            (x / g, y / g)
        })
        .collect();
    d.sort_by(|a, b| (a.0 * b.1).cmp(&(b.0 * a.1)));
    d.dedup();
    d
}

/// Cross-ratio of every four consecutive directions, as small integer ids.
fn ratios(d: &[(i64, i64)], ids: &mut HashMap<(i64, i64), usize>) -> Vec<usize> {
    d.windows(SHORT + 1)
        .map(|w| {
            let ((p1, q1), (p2, q2), (p3, q3), (p4, q4)) = (w[0], w[1], w[2], w[SHORT]);
            // (c - a)(d - b) / ((c - b)(d - a)); the denominators q cancel
            let num = (p3 * q1 - p1 * q3) * (p4 * q2 - p2 * q4);
            let den = (p3 * q2 - p2 * q3) * (p4 * q1 - p1 * q4);
            let g = gcd(num, den);
            let next = ids.len();
            *ids.entry((num / g, den / g)).or_insert(next)
        })
        .collect()
}

/// Longest common substring of two sequences, by a suffix automaton of a.
fn longest_common(a: &[usize], b: &[usize], symbols: usize) -> usize {
    let mut link: Vec<i64> = vec![-1];
    let mut len: Vec<usize> = vec![0];
    let mut head: Vec<i64> = vec![-1];
    let (mut edge_symbol, mut edge_next): (Vec<usize>, Vec<i64>) = (Vec::new(), Vec::new());
    // trans[state * symbols + symbol]: the next state; each state lists its symbols
    let mut trans: HashMap<usize, usize> = HashMap::new();
    let mut last = 0usize;
    for &ch in a {
        let cur = len.len();
        len.push(len[last] + 1);
        link.push(0);
        head.push(-1);
        let mut p = last as i64;
        while p != -1 && !trans.contains_key(&(p as usize * symbols + ch)) {
            trans.insert(p as usize * symbols + ch, cur);
            edge_symbol.push(ch);
            edge_next.push(head[p as usize]);
            head[p as usize] = edge_symbol.len() as i64 - 1;
            p = link[p as usize];
        }
        if p != -1 {
            let pu = p as usize;
            let q = trans[&(pu * symbols + ch)];
            if len[pu] + 1 == len[q] {
                link[cur] = q as i64;
            } else {
                let clone = len.len();
                len.push(len[pu] + 1);
                link.push(link[q]);
                head.push(-1);
                let mut e = head[q];
                while e != -1 {
                    let symbol = edge_symbol[e as usize];
                    let target = trans[&(q * symbols + symbol)];
                    trans.insert(clone * symbols + symbol, target);
                    edge_symbol.push(symbol);
                    edge_next.push(head[clone]);
                    head[clone] = edge_symbol.len() as i64 - 1;
                    e = edge_next[e as usize];
                }
                while p != -1 {
                    let key = p as usize * symbols + ch;
                    match trans.get_mut(&key) {
                        Some(t) if *t == q => *t = clone,
                        _ => break,
                    }
                    p = link[p as usize];
                }
                link[q] = clone as i64;
                link[cur] = clone as i64;
            }
        }
        last = cur;
    }
    let (mut best, mut state, mut run) = (0usize, 0usize, 0usize);
    for &ch in b {
        while state != 0 && !trans.contains_key(&(state * symbols + ch)) {
            state = link[state] as usize;
            run = len[state];
        }
        if let Some(&t) = trans.get(&(state * symbols + ch)) {
            state = t;
            run += 1;
        }
        best = best.max(run);
    }
    best
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let nums: Vec<i64> = input
        .split_ascii_whitespace()
        .map(|t| t.parse().unwrap())
        .collect();
    let (mut upper, mut lower) = (Vec::new(), Vec::new());
    for pair in nums.chunks(2) {
        if pair.len() < 2 || (pair[0] == 0 && pair[1] == 0) {
            break;
        }
        if pair[1] > 0 {
            upper.push((pair[0], pair[1]));
        } else {
            lower.push((pair[0], pair[1]));
        }
    }
    let (up, low) = (directions(&upper), directions(&lower));
    let mut answer = up.len().min(low.len()).min(SHORT);
    if up.len() > SHORT && low.len() > SHORT {
        let mut ids = HashMap::new();
        let ra = ratios(&up, &mut ids);
        let rb = ratios(&low, &mut ids);
        let common = longest_common(&ra, &rb, ids.len());
        if common > 0 {
            answer = common + SHORT;
        }
    }
    println!("{}", answer);
}
