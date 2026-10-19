use std::io::{self, Read, Write};

// cut the values 1 .. n greedily into runs of consecutive values whose
// positions alternately rise and fall, the first one as asked
fn blocks(pos: &[usize], n: usize, mut rising: bool) -> Vec<(usize, usize)> {
    let mut cuts = Vec::new();
    let mut v = 1;
    while v <= n {
        let mut w = v;
        while w < n && (pos[w + 1] > pos[w]) == rising {
            w += 1;
        }
        cuts.push((v, w));
        v = w + 1;
        rising = !rising;
    }
    cuts
}

// the least k with 2^k >= count
fn passes(count: usize) -> usize {
    let mut k = 0;
    while (1 << k) < count {
        k += 1;
    }
    k
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    if v.is_empty() {
        return;
    }
    let n = v[0];
    let mut cars = v[1..=n].to_vec();
    let mut pos = vec![0; n + 1];
    for (i, &c) in cars.iter().enumerate() {
        pos[c] = i;
    }
    // one pass keeps a chosen set of cars in order and appends the others
    // reversed; over k passes cars end up ordered by their codes of choices
    // in reflected Gray order, reversed once per one in the code
    let rising = blocks(&pos, n, true);
    let falling = blocks(&pos, n, false);
    let (runs, first) = if passes(rising.len()) <= passes(falling.len() + 1) {
        (rising, 0)
    } else {
        (falling, 1)
    };
    let k = passes(runs.len() + first);
    let mut code = vec![0usize; n + 1];
    for (i, &(lo, hi)) in runs.iter().enumerate() {
        let rank = i + first;
        for c in lo..=hi {
            code[c] = rank ^ (rank >> 1);
        }
    }
    let mut out = format!("{}\n", k);
    for bit in 0..k {
        let mut next: Vec<usize> =
            cars.iter().copied().filter(|&c| code[c] >> bit & 1 == 0).collect();
        next.extend(cars.iter().rev().copied().filter(|&c| code[c] >> bit & 1 == 1));
        cars = next;
        let line: Vec<String> = cars.iter().map(|c| c.to_string()).collect();
        out.push_str(&line.join(" "));
        out.push('\n');
    }
    io::stdout().write_all(out.as_bytes()).unwrap();
}
