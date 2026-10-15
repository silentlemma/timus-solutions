use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let words: Vec<&[u8]> = tokens.take(n).map(|w| w.as_bytes()).collect();
    // every suffix of every command, sorted; a substring starting at some
    // position is in another command exactly when it is a prefix of another
    // command's suffix, and the nearest such suffixes in the order share most
    let mut suffixes: Vec<(&[u8], usize)> = Vec::new();
    for (i, w) in words.iter().enumerate() {
        for p in 0..w.len() {
            suffixes.push((&w[p..], i));
        }
    }
    suffixes.sort();
    let total = suffixes.len();
    let adjacent: Vec<usize> = (0..total.saturating_sub(1))
        .map(|k| {
            let (a, b) = (suffixes[k].0, suffixes[k + 1].0);
            a.iter().zip(b).take_while(|(x, y)| x == y).count()
        })
        .collect();
    let mut shared = vec![0usize; total]; // the longest prefix shared with another command
    let mut run = 0;
    for k in 1..total {
        let other = suffixes[k].1 != suffixes[k - 1].1;
        run = if other { adjacent[k - 1] } else { run.min(adjacent[k - 1]) };
        shared[k] = run;
    }
    run = 0;
    for k in (0..total.saturating_sub(1)).rev() {
        let other = suffixes[k].1 != suffixes[k + 1].1;
        run = if other { adjacent[k] } else { run.min(adjacent[k]) };
        shared[k] = shared[k].max(run);
    }
    let mut best: Vec<Option<&[u8]>> = vec![None; n];
    for (k, &(suffix, w)) in suffixes.iter().enumerate() {
        let need = shared[k] + 1;
        if need <= suffix.len() && best[w].map_or(true, |b| need < b.len()) {
            best[w] = Some(&suffix[..need]);
        }
    }
    let lines: Vec<&str> = best.iter().map(|b| std::str::from_utf8(b.unwrap()).unwrap()).collect();
    println!("{}", lines.join("\n"));
}
