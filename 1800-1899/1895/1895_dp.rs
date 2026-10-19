use std::fmt::Write;
use std::io::{self, Read};

fn solve(window: i32, capacity: usize, deadlines: &[i32]) -> Option<(usize, Vec<(i32, i32)>)> {
    let n = deadlines.len();
    let width = n + 1;
    let state_count = width * width;
    let target = state_count - 1;
    let infinity = deadlines[n - 1] + 1;
    let releases: Vec<_> = deadlines
        .iter()
        .map(|&time| (time - window).max(0))
        .collect();
    let mut initial = vec![infinity; state_count];
    initial[0] = -1;
    let mut layers = vec![initial];
    let mut parents = vec![Vec::new()];
    let mut active = vec![0];
    for busy in 1..=2 * n {
        let mut following = vec![infinity; state_count];
        let mut previous = vec![0; state_count];
        let mut next_active = Vec::new();
        for &state in &active {
            let (first_done, second_done) = (state / width, state % width);
            let earliest = layers[busy - 1][state] + 1;
            for new_first in 0..=capacity.min(n - first_done) {
                let new_second = (capacity - new_first).min(first_done - second_done);
                if new_first + new_second == 0 {
                    continue;
                }
                let (ni, nj) = (first_done + new_first, second_done + new_second);
                let minute = if new_first > 0 {
                    earliest.max(releases[ni - 1])
                } else {
                    earliest
                };
                if new_second > 0 && minute >= deadlines[second_done] {
                    continue;
                }
                if nj < n {
                    let remaining_sides = if nj < ni { 1 } else { 2 };
                    if minute + 1 + remaining_sides > deadlines[nj] {
                        continue;
                    }
                }
                let destination = ni * width + nj;
                if minute < following[destination] {
                    if following[destination] == infinity {
                        next_active.push(destination);
                    }
                    following[destination] = minute;
                    previous[destination] = state;
                }
            }
        }
        layers.push(following);
        parents.push(previous);
        if layers[busy][target] != infinity {
            let mut starts = vec![(0, 0); n];
            let mut state = target;
            for used in (1..=busy).rev() {
                let old_state = parents[used][state];
                let (ni, nj) = (state / width, state % width);
                let (oi, oj) = (old_state / width, old_state % width);
                let minute = layers[used][state];
                for item in &mut starts[oi..ni] {
                    item.0 = minute;
                }
                for item in &mut starts[oj..nj] {
                    item.1 = minute;
                }
                state = old_state;
            }
            return Some((busy, starts));
        }
        if next_active.is_empty() {
            return None;
        }
        active = next_active;
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let window: i32 = tokens.next().unwrap().parse().unwrap();
    let capacity: usize = tokens.next().unwrap().parse().unwrap();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let deadlines: Vec<_> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    if let Some((busy, starts)) = solve(window, capacity, &deadlines) {
        let mut output = format!("{busy}\n");
        for (first, second) in starts {
            writeln!(output, "{first} {second}").unwrap();
        }
        print!("{output}");
    } else {
        println!("-1");
    }
}
