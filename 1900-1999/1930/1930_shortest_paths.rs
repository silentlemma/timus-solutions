use std::collections::VecDeque;
use std::io::{self, Read};

fn minimum_changes(adjacency: &[Vec<usize>], start: usize, target: usize) -> i32 {
    let state_count = 2 * adjacency.len();
    let mut distance = vec![state_count as i32; state_count];
    let mut settled = vec![false; state_count];
    let first = 2 * start;
    distance[first] = 0;
    distance[first + 1] = 0;
    let mut queue = VecDeque::from(vec![first, first + 1]);
    while let Some(state) = queue.pop_front() {
        if settled[state] {
            continue;
        }
        settled[state] = true;
        let (city, gear) = (state / 2, state & 1);
        if city == target {
            return distance[state];
        }
        for &next_state in &adjacency[city] {
            let cost = i32::from((next_state & 1) != gear);
            let candidate = distance[state] + cost;
            if candidate < distance[next_state] {
                distance[next_state] = candidate;
                if cost == 0 {
                    queue.push_front(next_state);
                } else {
                    queue.push_back(next_state);
                }
            }
        }
    }
    -1
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut values = text
        .split_whitespace()
        .map(|token| token.parse::<usize>().unwrap());
    let count = values.next().unwrap();
    let roads = values.next().unwrap();
    let mut adjacency = vec![Vec::new(); count];
    for _ in 0..roads {
        let lower = values.next().unwrap() - 1;
        let upper = values.next().unwrap() - 1;
        adjacency[lower].push(2 * upper);
        adjacency[upper].push(2 * lower + 1);
    }
    let start = values.next().unwrap() - 1;
    let target = values.next().unwrap() - 1;
    println!("{}", minimum_changes(&adjacency, start, target));
}
