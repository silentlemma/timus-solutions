use std::io::{self, Read};

const SMALL_SENDER: i64 = 5;
const BASE: i64 = 6;
const BOARD_SIZE: i64 = 7;
const POWER_OF_TWO: i64 = 8;
const POWER_OF_THREE: i64 = 9;
const SECOND_PRIME: i64 = 3;

fn solve(sender: i64, target: i64) -> (i64, Vec<i64>) {
    if target <= sender {
        return (sender - target, vec![sender, target]);
    }
    if target % sender == 0 {
        return (0, vec![sender, target]);
    }

    // One paid step joins a multiple of sender to a divisor of target.
    let mut divisor = 1;
    while divisor <= target / divisor {
        if target % divisor == 0 {
            for receiver in [divisor, target / divisor] {
                for before in [receiver - 1, receiver + 1] {
                    if before >= sender && before % sender == 0 {
                        return (1, vec![sender, before, receiver, target]);
                    }
                }
            }
        }
        divisor += 1;
    }

    if sender <= SMALL_SENDER {
        let mut before = target / sender * sender;
        if target - before > before + sender - target {
            before += sender;
        }
        return (2, vec![sender, before, target]);
    }

    let mut remainder = target;
    for prime in [2, SECOND_PRIME] {
        while remainder % prime == 0 {
            remainder /= prime;
        }
    }
    if remainder > 1 {
        let before = if remainder % BASE == 1 {
            remainder - 1
        } else {
            remainder + 1
        };
        return (2, vec![sender, BASE, before, remainder, target]);
    }
    if target % BASE == 0 {
        return (2, vec![sender, BASE, target]);
    }
    if target % POWER_OF_TWO == 0 {
        return (2, vec![sender, POWER_OF_TWO, target]);
    }
    if sender == BOARD_SIZE {
        return (2, vec![sender, POWER_OF_THREE, target]);
    }
    (2, vec![sender, SMALL_SENDER, 10, POWER_OF_THREE, target])
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input.split_whitespace().map(|word| word.parse().unwrap());
    let (cost, mut path) = solve(numbers.next().unwrap(), numbers.next().unwrap());
    path.dedup();
    println!("{}", cost);
    println!("{}", path.len());
    let route: Vec<String> = path.iter().map(|employee| employee.to_string()).collect();
    println!("{}", route.join(" "));
}
