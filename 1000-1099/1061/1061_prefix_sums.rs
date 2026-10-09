use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace();
    let n: usize = it.next().unwrap().parse().unwrap();
    let k: usize = it.next().unwrap().parse().unwrap();
    let states: Vec<u8> = it.flat_map(|t| t.bytes()).take(n).collect();
    // value[i] and locks[i]: the sum of values and the number of locked
    // buffers among the first i buffers
    let mut value = vec![0u64; n + 1];
    let mut locks = vec![0usize; n + 1];
    for (i, &c) in states.iter().enumerate() {
        let locked = c == b'*';
        locks[i + 1] = locks[i] + usize::from(locked);
        value[i + 1] = value[i] + if locked { 0 } else { u64::from(c - b'0') };
    }
    // the windows [l, l + k - 1] without locks; the first cheapest wins
    let mut best: Option<(u64, usize)> = None;
    for l in 1..=n.saturating_sub(k) + 1 {
        let r = l + k - 1;
        if r > n || locks[r] != locks[l - 1] {
            continue;
        }
        let v = value[r] - value[l - 1];
        if best.map_or(true, |(b, _)| v < b) {
            best = Some((v, l));
        }
    }
    println!("{}", best.map_or(0, |(_, l)| l));
}
