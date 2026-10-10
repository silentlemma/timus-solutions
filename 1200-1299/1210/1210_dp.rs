use std::io::{self, Read};

const INF: i64 = 1 << 40;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    // the "*" lines between blocks carry no information
    let mut it = input
        .split_ascii_whitespace()
        .filter(|&t| t != "*")
        .map(|t| t.parse::<i64>().unwrap());
    let levels = it.next().unwrap();
    // the cheapest cost of reaching each planet of the current level
    let mut cost = vec![0i64];
    for _ in 0..levels {
        let k = it.next().unwrap() as usize;
        let mut nxt = vec![INF; k];
        for best in nxt.iter_mut() {
            loop {
                let src = it.next().unwrap() as usize;
                if src == 0 {
                    break;
                }
                let price = it.next().unwrap();
                if cost[src - 1] < INF {
                    *best = (*best).min(cost[src - 1] + price);
                }
            }
        }
        cost = nxt;
    }
    println!("{}", cost.iter().min().unwrap());
}
