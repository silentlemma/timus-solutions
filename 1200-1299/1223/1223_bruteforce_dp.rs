use std::io::{self, Read};

const FLOORS: usize = 1000;
const EGGS: usize = 10;

fn main() {
    let mut best = vec![vec![0usize; FLOORS + 1]; EGGS + 1];
    for floors in 1..=FLOORS {
        best[1][floors] = floors;
    }
    // Ten eggs suffice for binary search. Try every first floor and
    // minimize the worse of the breaking and surviving outcomes.
    for eggs in 2..=EGGS {
        for floors in 1..=FLOORS {
            best[eggs][floors] = floors;
            for first in 1..=floors {
                let value = 1 + best[eggs - 1][first - 1].max(best[eggs][floors - first]);
                best[eggs][floors] = best[eggs][floors].min(value);
            }
        }
    }
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let mut output = String::new();
    while let Some(eggs) = numbers.next() {
        let floors = numbers.next().unwrap();
        if eggs == 0 && floors == 0 {
            break;
        }
        output += &format!("{}\n", best[eggs.min(EGGS)][floors]);
    }
    print!("{}", output);
}
