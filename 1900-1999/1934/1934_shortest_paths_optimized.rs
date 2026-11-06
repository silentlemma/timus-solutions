use std::io::{self, Read, Write};

const PERCENT_SCALE: usize = 100;
const PROBABILITY_BITS: u32 = 7;
const PROBABILITY_MASK: u32 = (1 << PROBABILITY_BITS) - 1;
const DECIMAL_PLACES: usize = 12;
const NONE: u32 = u32::MAX;

struct Edge {
    packed: u32,
    next: u32,
}

fn main() -> io::Result<()> {
    let (heads, edges, start, target) = {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input)?;
        let mut numbers = input
            .split_ascii_whitespace()
            .map(|token| token.parse::<u32>().unwrap());
        let size = numbers.next().unwrap() as usize;
        let roads = numbers.next().unwrap() as usize;
        let start = numbers.next().unwrap();
        let target = numbers.next().unwrap();
        let mut heads = vec![NONE; size + 1];
        let mut edges = Vec::with_capacity(2 * roads);
        for _ in 0..roads {
            let a = numbers.next().unwrap();
            let b = numbers.next().unwrap();
            let p = numbers.next().unwrap();
            for (from, to) in [(a, b), (b, a)] {
                let head = &mut heads[from as usize];
                let edge = Edge {
                    packed: (to << PROBABILITY_BITS) | p,
                    next: *head,
                };
                *head = edges.len() as u32;
                edges.push(edge);
            }
        }
        (heads, edges, start, target)
    };

    let mut cost = [0.0; PERCENT_SCALE];
    for (probability, value) in cost.iter_mut().enumerate() {
        *value = -(-(probability as f64) / PERCENT_SCALE as f64).ln_1p();
    }
    let mut distance = vec![NONE; heads.len()];
    let mut parent = vec![NONE; heads.len()];
    let mut best = vec![f64::INFINITY; heads.len()];
    let mut queue = Vec::with_capacity(heads.len());
    distance[start as usize] = 0;
    best[start as usize] = 0.0;
    queue.push(start);
    let mut front = 0;
    while front < queue.len() {
        let city = queue[front];
        if city == target {
            break;
        }
        front += 1;
        let next_distance = distance[city as usize] + 1;
        let prefix_cost = best[city as usize];
        let mut index = heads[city as usize];
        while index != NONE {
            let edge = &edges[index as usize];
            let neighbor = edge.packed >> PROBABILITY_BITS;
            let vertex = neighbor as usize;
            if distance[vertex] == NONE {
                distance[vertex] = next_distance;
                queue.push(neighbor);
            }
            if distance[vertex] == next_distance {
                let candidate = prefix_cost + cost[(edge.packed & PROBABILITY_MASK) as usize];
                if candidate < best[vertex] {
                    best[vertex] = candidate;
                    parent[vertex] = city;
                }
            }
            index = edge.next;
        }
    }

    queue.clear();
    let mut city = target;
    while city != NONE {
        queue.push(city);
        city = parent[city as usize];
    }
    let risk = -(-best[target as usize]).exp_m1();
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{} {risk:.DECIMAL_PLACES$}", queue.len())?;
    for (index, city) in queue.iter().rev().enumerate() {
        if index != 0 {
            write!(output, " ")?;
        }
        write!(output, "{city}")?;
    }
    writeln!(output)?;
    output.flush()
}
