use std::collections::{HashSet, VecDeque};
use std::io::{self, Read};

const LOCAL_LIMIT: usize = 5;

fn wins(own: &[i32], opponent: &[i32]) -> bool {
    let mut first: VecDeque<i32> = own.iter().copied().collect();
    let mut second: VecDeque<i32> = opponent.iter().copied().collect();
    let mut seen = HashSet::new();
    while !first.is_empty() && !second.is_empty() {
        let state = (
            first.iter().copied().collect::<Vec<_>>(),
            second.iter().copied().collect::<Vec<_>>(),
        );
        if !seen.insert(state) {
            return false;
        }
        let x = first.pop_front().unwrap();
        let y = second.pop_front().unwrap();
        if x > y {
            first.extend([y, x]);
        } else if y > x {
            second.extend([x, y]);
        }
    }
    !first.is_empty()
}

fn next_permutation(values: &mut [i32]) -> bool {
    let pivot = (0..values.len() - 1)
        .rev()
        .find(|&index| values[index] < values[index + 1]);
    let Some(pivot) = pivot else {
        return false;
    };
    let mut successor = values.len() - 1;
    while values[successor] <= values[pivot] {
        successor -= 1;
    }
    values.swap(pivot, successor);
    values[pivot + 1..].reverse();
    true
}

fn construct(opponent: &[i32]) -> Option<Vec<i32>> {
    let size = opponent.len().min(LOCAL_LIMIT);
    let local = &opponent[..size];
    let mut candidate = local.to_vec();
    candidate.sort_unstable();
    loop {
        if wins(&candidate, local) {
            let mut answer = opponent.to_vec();
            answer[..size].copy_from_slice(&candidate);
            return Some(answer);
        }
        if !next_permutation(&mut candidate) {
            return None;
        }
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size = words.next().unwrap().parse::<usize>().unwrap();
    let opponent: Vec<i32> = (0..size)
        .map(|_| words.next().unwrap().parse().unwrap())
        .collect();
    match construct(&opponent) {
        None => println!("NO"),
        Some(answer) => {
            println!("YES");
            println!(
                "{}",
                answer
                    .iter()
                    .map(ToString::to_string)
                    .collect::<Vec<_>>()
                    .join(" ")
            );
        }
    }
}
