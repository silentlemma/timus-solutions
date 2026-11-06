use std::io::{self, Read};

const DECIMAL: usize = 10;

fn next_number(bytes: &mut impl Iterator<Item = u8>) -> usize {
    let mut value = 0;
    let mut started = false;
    for byte in bytes {
        if byte.is_ascii_digit() {
            value = value * DECIMAL + usize::from(byte - b'0');
            started = true;
        } else if started {
            break;
        }
    }
    value
}

fn root(sets: &mut [usize], mut city: usize) -> usize {
    while sets[city] != city {
        sets[city] = sets[sets[city]];
        city = sets[city];
    }
    city
}

fn depth(
    city: usize,
    parent: usize,
    roads: &[Vec<(usize, usize)>],
    visited: &mut [bool],
    diameter: &mut usize,
) -> usize {
    visited[city] = true;
    let mut deepest = 0;
    for &(neighbor, length) in &roads[city] {
        if neighbor != parent {
            let branch = length + depth(neighbor, city, roads, visited, diameter);
            *diameter = (*diameter).max(deepest + branch);
            deepest = deepest.max(branch);
        }
    }
    deepest
}

fn main() {
    let stdin = io::stdin();
    let mut bytes = stdin.lock().bytes().map_while(Result::ok);
    let cities = next_number(&mut bytes);
    let count = next_number(&mut bytes);
    let target = next_number(&mut bytes);
    let mut sets: Vec<_> = (0..=cities).collect();
    let mut roads = vec![Vec::new(); cities + 1];
    for _ in 0..count {
        let left = next_number(&mut bytes);
        let right = next_number(&mut bytes);
        let length = next_number(&mut bytes);
        let (a, b) = (root(&mut sets, left), root(&mut sets, right));
        if a == b {
            println!("YES");
            return;
        }
        sets[a] = b;
        roads[left].push((right, length));
        roads[right].push((left, length));
    }
    let mut visited = vec![false; cities + 1];
    let mut diameter = 0;
    for city in 1..=cities {
        if !visited[city] {
            depth(city, 0, &roads, &mut visited, &mut diameter);
        }
    }
    println!("{}", if diameter >= target { "YES" } else { "NO" });
}
