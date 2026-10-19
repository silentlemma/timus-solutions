use std::io::{self, Read};

const MODULUS: u64 = 1000000007;

fn seating_count(size: usize, requests: &[usize]) -> u64 {
    if size == 2 {
        return 1;
    }
    let mut neighbors = vec![Vec::new(); size];
    for (person, &target) in requests.iter().enumerate() {
        if !neighbors[person].contains(&target) {
            neighbors[person].push(target);
            neighbors[target].push(person);
            if neighbors[person].len() > 2 || neighbors[target].len() > 2 {
                return 0;
            }
        }
    }
    let mut visited = vec![false; size];
    let (mut components, mut paths) = (0, 0);
    for start in 0..size {
        if visited[start] {
            continue;
        }
        let mut stack = vec![start];
        visited[start] = true;
        let (mut vertices, mut degrees) = (0, 0);
        while let Some(person) = stack.pop() {
            vertices += 1;
            degrees += neighbors[person].len();
            for &target in &neighbors[person] {
                if !visited[target] {
                    visited[target] = true;
                    stack.push(target);
                }
            }
        }
        if degrees == 2 * vertices {
            return if vertices == size { 2 } else { 0 };
        }
        components += 1;
        if vertices > 1 {
            paths += 1;
        }
    }
    let mut answer = 1;
    for _ in 0..paths {
        answer = answer * 2 % MODULUS;
    }
    for factor in 2..components {
        answer = answer * factor as u64 % MODULUS;
    }
    answer
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size: usize = words.next().unwrap().parse().unwrap();
    let count: usize = words.next().unwrap().parse().unwrap();
    let requests: Vec<usize> = words
        .take(count)
        .map(|word| word.parse::<usize>().unwrap() - 1)
        .collect();
    println!("{}", seating_count(size, &requests));
}
