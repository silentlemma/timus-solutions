use std::cmp::Reverse;
use std::collections::BinaryHeap;
use std::io::{self, Read};

fn read_number(tokens: &mut std::str::SplitWhitespace<'_>) -> usize {
    tokens.next().unwrap().parse().unwrap()
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let height = read_number(&mut tokens);
    let width = read_number(&mut tokens);
    let stride = width + 2;
    let size = (height + 2) * stride;
    let row = read_number(&mut tokens);
    let column = read_number(&mut tokens);
    let start = row * stride + column;
    let row = read_number(&mut tokens);
    let column = read_number(&mut tokens);
    let mut drone = row * stride + column;

    let mut cost = vec![0_i64; size];
    for row in 1..=height {
        for column in 1..=width {
            cost[row * stride + column] = read_number(&mut tokens) as i64;
        }
    }
    let mut successor = vec![0; size];
    for row in 1..=height {
        let wind = tokens.next().unwrap().as_bytes();
        for column in 1..=width {
            let cell = row * stride + column;
            successor[cell] = match wind[column - 1] {
                b'U' => cell - stride,
                b'D' => cell + stride,
                b'L' => cell - 1,
                b'R' => cell + 1,
                _ => unreachable!(),
            };
        }
    }

    let infinity = i64::MAX / 2;
    let mut distance = vec![infinity; size];
    let mut heap = BinaryHeap::new();
    distance[start] = 0;
    heap.push(Reverse((0_i64, start)));
    while let Some(Reverse((time, cell))) = heap.pop() {
        if time != distance[cell] {
            continue;
        }
        for next in [cell - stride, cell + stride, cell - 1, cell + 1] {
            if cost[next] == 0 {
                continue;
            }
            let arrival = time + cost[next];
            if arrival < distance[next] {
                distance[next] = arrival;
                heap.push(Reverse((arrival, next)));
            }
        }
    }

    let mut first = vec![None; size];
    let mut path = Vec::new();
    while cost[drone] != 0 && first[drone].is_none() {
        first[drone] = Some(path.len());
        path.push(drone);
        drone = successor[drone];
    }
    let cycle_start = first[drone].unwrap_or(path.len());
    let period = (path.len() - cycle_start) as i64;
    let mut answer = infinity;
    for (time, &cell) in path.iter().enumerate() {
        let arrival = distance[cell];
        let mut catch_time = time as i64;
        if arrival > catch_time {
            if time < cycle_start {
                continue;
            }
            // Each cycle cell is revisited once per period.
            catch_time += ((arrival - catch_time + period - 1) / period) * period;
        }
        answer = answer.min(catch_time);
    }
    println!("{}", if answer == infinity { -1 } else { answer });
}
