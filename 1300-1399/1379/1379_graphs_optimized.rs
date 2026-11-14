use std::io::{self, Read};

const TRUCK: usize = 3_000_000;
const CUP: usize = 100;
const ORDER: usize = 10_000_000;
const DAY: usize = 24 * 60;
const MAX_VERTICES: usize = 500;
const VERTEX_BITS: usize = 9;
const TIME_BITS: usize = 11;
const LOAD_SHIFT: usize = VERTEX_BITS + TIME_BITS;
const VERTEX_MASK: usize = (1 << VERTEX_BITS) - 1;
const TIME_MASK: usize = (1 << TIME_BITS) - 1;
const NONE: usize = usize::MAX;

fn number(bytes: &mut &[u8]) -> usize {
    let mut value = 0;
    while let [c, rest @ ..] = *bytes {
        if !c.is_ascii_whitespace() {
            break;
        }
        *bytes = rest;
    }
    while let [c, rest @ ..] = *bytes {
        if !c.is_ascii_digit() {
            break;
        }
        value = value * 10 + usize::from(*c - b'0');
        *bytes = rest;
    }
    value
}

fn can_deliver(graph: &[Vec<usize>], load: usize) -> bool {
    let threshold = load << LOAD_SHIFT;
    let mut distance = [DAY + 1; MAX_VERTICES];
    let mut next = [NONE; MAX_VERTICES];
    let mut previous = [NONE; MAX_VERTICES];
    let mut heads = [NONE; DAY + 1];
    distance[0] = 0;
    heads[0] = 0;
    for minute in 0..=DAY {
        while heads[minute] != NONE {
            let v = heads[minute];
            heads[minute] = next[v];
            if next[v] != NONE {
                previous[next[v]] = NONE;
            }
            if v == graph.len() - 1 {
                return true;
            }
            for &edge in &graph[v] {
                if edge < threshold {
                    break;
                }
                let to = edge & VERTEX_MASK;
                let arrival = minute + ((edge >> VERTEX_BITS) & TIME_MASK);
                let old = distance[to];
                if arrival >= old {
                    continue;
                }
                if old <= DAY {
                    let (before, after) = (previous[to], next[to]);
                    if before == NONE {
                        heads[old] = after;
                    } else {
                        next[before] = after;
                    }
                    if after != NONE {
                        previous[after] = before;
                    }
                }
                distance[to] = arrival;
                previous[to] = NONE;
                next[to] = heads[arrival];
                if next[to] != NONE {
                    previous[next[to]] = to;
                }
                heads[arrival] = to;
            }
        }
    }
    false
}

fn main() {
    let mut input = Vec::new();
    io::stdin().read_to_end(&mut input).unwrap();
    let mut bytes = input.as_slice();
    let (n, m) = (number(&mut bytes), number(&mut bytes));
    if n == 1 {
        println!("{ORDER}");
        return;
    }
    let mut graph = vec![Vec::new(); n];
    let mut limits = Vec::with_capacity(m);
    for _ in 0..m {
        let (a, b) = (number(&mut bytes) - 1, number(&mut bytes) - 1);
        let (minutes, weight) = (number(&mut bytes), number(&mut bytes));
        if weight >= TRUCK + CUP {
            let load = (weight - TRUCK) / CUP;
            let edge = (load << LOAD_SHIFT) | (minutes << VERTEX_BITS);
            graph[a].push(edge | b);
            graph[b].push(edge | a);
            limits.push(load);
        }
    }
    drop(input);
    if graph[0].is_empty() || graph[n - 1].is_empty() {
        println!("0");
        return;
    }
    for edges in &mut graph {
        edges.sort_unstable_by(|a, b| b.cmp(a));
    }
    let upper = graph[0][0].min(graph[n - 1][0]) >> LOAD_SHIFT;
    limits.retain(|&load| load <= upper);
    limits.sort_unstable();
    limits.dedup();
    let count = limits.partition_point(|&load| can_deliver(&graph, load));
    let answer = if count == 0 { 0 } else { limits[count - 1] };
    println!("{answer}");
}
