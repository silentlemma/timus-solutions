use std::io::{self, Read};

const PLAYERS: usize = 3;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input.split_ascii_whitespace().map(|t| t.parse::<u32>().unwrap());
    let own: Vec<Vec<u32>> = (0..PLAYERS)
        .map(|_| {
            let n = it.next().unwrap() as usize;
            (0..n).map(|_| it.next().unwrap()).collect()
        })
        .collect();
    // walk the three sorted lists together, always moving past the
    // smallest current number
    let mut at = [0usize; PLAYERS];
    let mut common = 0;
    while (0..PLAYERS).all(|p| at[p] < own[p].len()) {
        let low = (0..PLAYERS).map(|p| own[p][at[p]]).min().unwrap();
        let high = (0..PLAYERS).map(|p| own[p][at[p]]).max().unwrap();
        if low == high {
            common += 1;
        }
        for p in 0..PLAYERS {
            if own[p][at[p]] == low {
                at[p] += 1;
            }
        }
    }
    println!("{}", common);
}
