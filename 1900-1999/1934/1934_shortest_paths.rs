use std::fmt::Write as FormatWrite;
use std::io::{self, Read};

const PERCENT_SCALE: usize = 100;
const PROBABILITY_DIGITS: usize = 12;

fn safest_shortest_path(
    adjacency: &[Vec<usize>],
    start: usize,
    target: usize,
) -> (Vec<usize>, f64) {
    let count = adjacency.len();
    let mut costs = [0.0; PERCENT_SCALE];
    for (probability, cost) in costs.iter_mut().enumerate() {
        *cost = -(-(probability as f64) / PERCENT_SCALE as f64).ln_1p();
    }
    let mut distance = vec![usize::MAX; count];
    let mut parent = vec![usize::MAX; count];
    let mut best = vec![f64::INFINITY; count];
    let mut queue = Vec::with_capacity(count);
    distance[start] = 0;
    best[start] = 0.0;
    queue.push(start);
    let mut head = 0;
    while head < queue.len() {
        let city = queue[head];
        head += 1;
        if city == target {
            break;
        }
        for &edge in &adjacency[city] {
            let neighbor = edge / PERCENT_SCALE;
            let probability = edge % PERCENT_SCALE;
            if distance[neighbor] == usize::MAX {
                distance[neighbor] = distance[city] + 1;
                queue.push(neighbor);
            }
            if distance[neighbor] == distance[city] + 1 {
                let candidate = best[city] + costs[probability];
                if candidate < best[neighbor] {
                    best[neighbor] = candidate;
                    parent[neighbor] = city;
                }
            }
        }
    }
    let mut path = Vec::new();
    let mut city = target;
    while city != usize::MAX {
        path.push(city);
        city = parent[city];
    }
    path.reverse();
    (path, -(-best[target]).exp_m1())
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input
        .split_whitespace()
        .map(|token| token.parse::<usize>().unwrap());
    let count = values.next().unwrap();
    let roads = values.next().unwrap();
    let start = values.next().unwrap() - 1;
    let target = values.next().unwrap() - 1;
    let mut adjacency = vec![Vec::new(); count];
    for _ in 0..roads {
        let first = values.next().unwrap() - 1;
        let second = values.next().unwrap() - 1;
        let probability = values.next().unwrap();
        adjacency[first].push(PERCENT_SCALE * second + probability);
        adjacency[second].push(PERCENT_SCALE * first + probability);
    }
    let (path, risk) = safest_shortest_path(&adjacency, start, target);
    let mut output = format!("{} {:.*}\n", path.len(), PROBABILITY_DIGITS, risk);
    for (index, city) in path.iter().enumerate() {
        if index != 0 {
            output.push(' ');
        }
        write!(output, "{}", city + 1).unwrap();
    }
    println!("{}", output);
}
