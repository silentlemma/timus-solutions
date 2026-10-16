use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let suits: Vec<Vec<u8>> = input
        .lines()
        .filter(|line| !line.trim().is_empty())
        .map(|line| {
            line.split_ascii_whitespace()
                .map(|card| *card.as_bytes().last().unwrap())
                .collect()
        })
        .collect();
    let (count, depth) = (suits.len(), suits[0].len());
    let mut moves = 0;
    for level in 0..depth - 1 {
        // once the cards above level j sit in one-suit runs, the run ending at
        // level j of pile i must go onto the card one rank lower in its suit,
        // which lies at level j + 1 of pile target[i]
        let target: Vec<usize> = (0..count)
            .map(|i| (0..count).find(|&k| suits[k][level + 1] == suits[i][level]).unwrap())
            .collect();
        // every pile with a change of suit here needs one move, and each cycle
        // of such piles needs one more, to a new pile and back
        let mut seen = vec![false; count];
        for i in 0..count {
            if target[i] == i || seen[i] {
                continue;
            }
            moves += 1;
            let mut k = i;
            while !seen[k] {
                seen[k] = true;
                moves += 1;
                k = target[k];
            }
        }
    }
    println!("{}", moves);
}
