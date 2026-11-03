use std::io::{self, Read};

const MANY: u8 = 2;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let (weight, n) = (numbers.next().unwrap(), numbers.next().unwrap());
    let cards: Vec<usize> = numbers.take(n).collect();
    let total: usize = cards.iter().sum();
    let select_missing = total - weight < weight;
    let target = weight.min(total - weight);
    let mut ways = vec![0u8; target + 1];
    let mut last = vec![0u8; target + 1];
    ways[0] = 1;
    // Complementing subsets preserves uniqueness. Descending sums avoid
    // reusing cards, and a first-reach parent is never replaced later.
    for (i, &card) in cards.iter().enumerate() {
        if card <= target {
            for sum in (card..=target).rev() {
                if ways[sum] == 0 && ways[sum - card] != 0 {
                    last[sum] = (i + 1) as u8;
                }
                ways[sum] = MANY.min(ways[sum] + ways[sum - card]);
            }
        }
        if ways[target] == MANY {
            println!("-1");
            return;
        }
    }
    if ways[target] == 0 {
        println!("0");
        return;
    }
    let mut chosen = vec![false; n];
    let mut sum = target;
    while sum > 0 {
        let i = last[sum] as usize - 1;
        chosen[i] = true;
        sum -= cards[i];
    }
    let answer: Vec<String> = (0..n)
        .filter(|&i| chosen[i] == select_missing)
        .map(|i| (i + 1).to_string())
        .collect();
    println!("{}", answer.join(" "));
}
