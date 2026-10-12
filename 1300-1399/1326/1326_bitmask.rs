use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|t| t.parse::<usize>().unwrap());
    let n = it.next().unwrap();
    // every offer as a price and its caps as a mask over 1..n
    let mut offers: Vec<(usize, usize)> = (0..n).map(|i| (it.next().unwrap(), 1 << i)).collect();
    let m = it.next().unwrap();
    for _ in 0..m {
        let price = it.next().unwrap();
        let size = it.next().unwrap();
        let mask = (0..size).fold(0, |mask, _| mask | 1 << (it.next().unwrap() - 1));
        offers.push((price, mask));
    }
    let count = it.next().unwrap_or(0);
    // the wanted caps get the bits 0, 1, ... of a smaller mask
    let mut bit = vec![0usize; n];
    let mut wanted = 0;
    for _ in 0..count {
        let cap = it.next().unwrap() - 1;
        if bit[cap] == 0 {
            bit[cap] = 1 << wanted;
            wanted += 1;
        }
    }
    let full = (1usize << wanted) - 1;
    // offers that hold each wanted cap, as a price and the bits they leave
    let mut by_low: Vec<Vec<(usize, usize)>> = vec![Vec::new(); wanted];
    for &(price, caps) in &offers {
        let mask = (0..n)
            .filter(|&i| caps >> i & 1 == 1)
            .fold(0, |mask, i| mask | bit[i]);
        for (i, list) in by_low.iter_mut().enumerate() {
            if mask >> i & 1 == 1 {
                list.push((price, full & !mask));
            }
        }
    }
    // cheapest[s]: the least money that buys every cap of the set s; some
    // offer must hold its lowest cap
    let mut cheapest = vec![0usize; full + 1];
    for s in 1..=full {
        cheapest[s] = by_low[s.trailing_zeros() as usize]
            .iter()
            .map(|&(price, keep)| price + cheapest[s & keep])
            .min()
            .unwrap();
    }
    println!("{}", cheapest[full]);
}
