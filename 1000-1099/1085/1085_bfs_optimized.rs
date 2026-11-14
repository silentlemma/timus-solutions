use std::io::{self, Read};

const MAX_STOPS: usize = 100;
const FARE: usize = 4;

#[derive(Clone, Copy, Default)]
struct Group {
    present: bool,
    paying: usize,
    budget: usize,
}

fn search(start: usize, neighbors: &[u128], group: Group, total: &mut [usize]) -> u128 {
    let mut front = 1u128 << start;
    let mut reached = 0;
    let mut fare = 0;
    while front != 0 && (group.paying == 0 || fare <= group.budget) {
        reached |= front;
        let mut next = 0;
        while front != 0 {
            let stop = front.trailing_zeros() as usize;
            front &= front - 1;
            total[stop] += fare * group.paying;
            next |= neighbors[stop];
        }
        front = next & !reached;
        fare += FARE;
    }
    reached
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let mut number = || tokens.next().unwrap().parse::<usize>().unwrap();
    let (stops, routes) = (number(), number());
    let mut neighbors = [0u128; MAX_STOPS];
    for _ in 0..routes {
        let mut route = 0u128;
        for _ in 0..number() {
            route |= 1 << (number() - 1);
        }
        let mut remaining = route;
        while remaining != 0 {
            let stop = remaining.trailing_zeros() as usize;
            remaining &= remaining - 1;
            neighbors[stop] |= route;
        }
    }
    let mut groups = [Group::default(); MAX_STOPS];
    for _ in 0..number() {
        let (money, start, pass) = (number(), number(), number());
        let group = &mut groups[start - 1];
        group.present = true;
        if pass == 0 {
            group.budget = if group.paying == 0 {
                money
            } else {
                money.min(group.budget)
            };
            group.paying += 1;
        }
    }
    let mut valid = (1u128 << stops) - 1;
    let mut total = [0; MAX_STOPS];
    for (start, &group) in groups[..stops].iter().enumerate() {
        if group.present {
            valid &= search(start, &neighbors, group, &mut total);
            if valid == 0 {
                break;
            }
        }
    }
    let best = (0..stops)
        .filter(|&stop| valid & (1 << stop) != 0)
        .min_by_key(|&stop| (total[stop], stop));
    match best {
        Some(stop) => println!("{} {}", stop + 1, total[stop]),
        None => println!("0"),
    }
}
