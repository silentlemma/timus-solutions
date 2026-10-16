use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut piles: Vec<i64> = input.split_ascii_whitespace().map(|w| w.parse().unwrap()).collect();
    let mut asked = 0;
    loop {
        asked += 1;
        // the closest two piles differ least among neighbours in sorted order
        piles.sort();
        let gap = piles.windows(2).map(|w| w[1] - w[0]).min().unwrap();
        if gap == 0 {
            break;
        }
        piles.push(gap);
    }
    println!("{}", asked);
}
