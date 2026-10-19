use std::io::{self, Read};

fn safe_removals(values: &[u64], budget: u64) -> (usize, usize) {
    let mut values = values.to_vec();
    values.sort_unstable();
    let mut removed = 0;
    let mut spells = 0;
    let mut active = 0;
    let mut start = 0;
    while start < values.len() {
        let mut end = start + 1;
        while end < values.len() && values[end] == values[start] {
            end += 1;
        }
        let count = end - start;
        let threshold = values[start];
        if count as u64 * threshold > budget {
            break;
        }
        if (active + count) as u64 * threshold > budget {
            spells += 1;
            active = 0;
        }
        active += count;
        removed += count;
        start = end;
    }
    (removed, spells + usize::from(active > 0))
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let budget = tokens.next().unwrap().parse::<u64>().unwrap();
    let values: Vec<u64> = (0..count)
        .map(|_| tokens.next().unwrap().parse::<u64>().unwrap())
        .collect();
    let (removed, spells) = safe_removals(&values, budget);
    println!("{} {}", removed, spells);
}
