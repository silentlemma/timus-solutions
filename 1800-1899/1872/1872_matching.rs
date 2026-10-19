use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let v: Vec<usize> = input.split_ascii_whitespace().map(|t| t.parse().unwrap()).collect();
    let n = v[0];
    let area = &v[1..n + 1];
    let low: Vec<usize> = v[n + 1..].iter().step_by(2).copied().collect();
    let high: Vec<usize> = v[n + 2..].iter().step_by(2).copied().collect();
    let mut order: Vec<usize> = (0..n).collect();
    order.sort_by_key(|&k| area[k]);
    let mut by_low: Vec<usize> = (0..n).collect();
    by_low.sort_by_key(|&k| low[k]);
    let sizes: Vec<usize> = order.iter().map(|&k| area[k]).collect();
    // rooms from the smallest up, each to the waiting team whose largest
    // area is the smallest
    let mut waiting = BinaryHeap::new();
    let mut team = vec![0usize; n];
    let mut at = 0;
    for place in 0..n {
        while at < n && low[by_low[at]] <= sizes[place] {
            waiting.push(Reverse((high[by_low[at]], by_low[at])));
            at += 1;
        }
        match waiting.pop() {
            Some(Reverse((top, t))) if top >= sizes[place] => team[place] = t,
            _ => {
                println!("Let's search for another office.");
                return;
            }
        }
    }
    // the team in room place takes rooms first[place] .. last[place] in
    // sorted order; another seating exists exactly when two teams could swap
    let first: Vec<usize> = team.iter().map(|&t| sizes.partition_point(|&s| s < low[t])).collect();
    let last: Vec<usize> = team.iter().map(|&t| sizes.partition_point(|&s| s <= high[t])).collect();
    for q in 1..n {
        // last holds one past the last room
        if (first[q]..q).any(|p| last[p] > q) {
            println!("Ask Shiftman for help.");
            return;
        }
    }
    let mut room = vec![0usize; n];
    for (p, &t) in team.iter().enumerate() {
        room[t] = order[p] + 1;
    }
    let line: Vec<String> = room.iter().map(|r| r.to_string()).collect();
    println!("Perfect!\n{}", line.join(" "));
}
