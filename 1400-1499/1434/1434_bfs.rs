use std::collections::VecDeque;
use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut it = input
        .split_ascii_whitespace()
        .map(|x| x.parse::<usize>().unwrap());
    let (n, m) = (it.next().unwrap(), it.next().unwrap());
    let mut routes = Vec::with_capacity(n);
    let mut on_stop = vec![Vec::new(); m + 1];
    for r in 0..n {
        let k = it.next().unwrap();
        let stops: Vec<usize> = (0..k).map(|_| it.next().unwrap()).collect();
        for &st in &stops {
            on_stop[st].push(r);
        }
        routes.push(stops);
    }
    let (a, b) = (it.next().unwrap(), it.next().unwrap());
    // one ride along a route reaches any of its stops, both ways; layers of rides
    let mut rides: Vec<i64> = vec![-1; m + 1];
    let mut came_by = vec![usize::MAX; m + 1];
    let mut boarded = vec![usize::MAX; n]; // the stop where a route was first taken
    rides[a] = 0;
    let mut queue = VecDeque::from(vec![a]);
    while let Some(st) = queue.pop_front() {
        if rides[b] >= 0 {
            break;
        }
        for &r in &on_stop[st] {
            if boarded[r] != usize::MAX {
                continue;
            }
            boarded[r] = st;
            for &next in &routes[r] {
                if rides[next] < 0 {
                    rides[next] = rides[st] + 1;
                    came_by[next] = r;
                    queue.push_back(next);
                }
            }
        }
    }
    if rides[b] < 0 {
        println!("-1");
        return;
    }
    let mut path = vec![b];
    while *path.last().unwrap() != a {
        path.push(boarded[came_by[*path.last().unwrap()]]);
    }
    path.reverse();
    let line: Vec<String> = path.iter().map(|x| x.to_string()).collect();
    println!("{}\n{}", rides[b], line.join(" "));
}
