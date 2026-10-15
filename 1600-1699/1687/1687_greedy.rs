use std::io::{self, Read};

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut it = text.split_ascii_whitespace().map(|w| w.parse::<usize>().unwrap());
    let (n, k) = (it.next().unwrap(), it.next().unwrap());
    let boxes: Vec<Vec<usize>> = (0..k)
        .map(|_| {
            let size = it.next().unwrap();
            (0..size).map(|_| it.next().unwrap()).collect()
        })
        .collect();
    let m = it.next().unwrap();
    let mut wanted = vec![false; n + 1];
    for _ in 0..m {
        wanted[it.next().unwrap()] = true;
    }
    let useful: Vec<usize> = (0..k).filter(|&i| boxes[i].iter().any(|&c| wanted[c])).collect();
    let mut coverable = vec![false; n + 1];
    for &i in &useful {
        for &c in &boxes[i] {
            coverable[c] = coverable[c] || wanted[c];
        }
    }
    let coverable_count = coverable.iter().filter(|&&x| x).count();
    // no set of boxes is worth more than all coverable coins, nor holds more
    // than all useful boxes; one box per coverable coin reaches every coin,
    // so the answer is min(useful, coverable): those boxes, then any others
    let mut chosen = vec![false; k];
    let mut covered = vec![false; n + 1];
    let mut count = 0;
    for coin in 1..=n {
        if !coverable[coin] || covered[coin] {
            continue;
        }
        if let Some(&i) = useful.iter().find(|&&i| boxes[i].contains(&coin)) {
            chosen[i] = true;
            count += 1;
            for &c in &boxes[i] {
                covered[c] = true;
            }
        }
    }
    for &i in &useful {
        if count < coverable_count && !chosen[i] {
            chosen[i] = true;
            count += 1;
        }
    }
    let picked: Vec<String> = (0..k).filter(|&i| chosen[i]).map(|i| (i + 1).to_string()).collect();
    println!("{}", count);
    println!("{}", picked.join(" "));
}
