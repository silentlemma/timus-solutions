use std::io::{self, BufWriter, Read, Write};

const STATION_IDS: usize = 32768;

fn register(station: usize, index: &mut [u16], count: &mut u16) -> u16 {
    if index[station] == 0 {
        *count += 1;
        index[station] = *count;
    }
    index[station]
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut values = input.split_ascii_whitespace();
    let mut number = || values.next().unwrap().parse::<usize>().unwrap();
    let mut index = vec![0; STATION_IDS];
    let mut count = 0;
    let mut edges = Vec::new();
    for _ in 0..number() {
        let length = number();
        let mut last = register(number(), &mut index, &mut count);
        for _ in 1..length {
            let next = register(number(), &mut index, &mut count);
            edges.push((last, next));
            last = next;
        }
    }

    // Store every adjacency list in one contiguous buffer.
    let mut offsets = vec![0; usize::from(count) + 2];
    for &(a, b) in &edges {
        offsets[usize::from(a) + 1] += 1;
        offsets[usize::from(b) + 1] += 1;
    }
    for i in 1..offsets.len() {
        offsets[i] += offsets[i - 1];
    }
    let mut neighbors = vec![0; *offsets.last().unwrap()];
    let mut cursor = offsets.clone();
    for (a, b) in edges {
        neighbors[cursor[usize::from(a)]] = b;
        neighbors[cursor[usize::from(b)]] = a;
        cursor[usize::from(a)] += 1;
        cursor[usize::from(b)] += 1;
    }
    let adjacent = |v: usize| &neighbors[offsets[v]..offsets[v + 1]];

    let length = number();
    let mut recorded = values.map(|value| {
        value
            .parse::<usize>()
            .ok()
            .and_then(|station| index.get(station))
            .copied()
            .unwrap_or_default()
    });
    let start = recorded.next().unwrap();
    if start == 0 {
        return;
    }
    let mut last = start;
    for next in recorded.take(length - 1) {
        if !adjacent(usize::from(last)).contains(&next) {
            return;
        }
        last = next;
    }

    // Use zero for unvisited vertices and number the first layer one.
    let mut layer = vec![0u16; usize::from(count) + 1];
    layer[usize::from(start)] = 1;
    let mut queue = Vec::with_capacity(usize::from(count));
    queue.push(start);
    let mut head = 0;
    while head < queue.len() {
        let v = usize::from(queue[head]);
        head += 1;
        for &to in adjacent(v) {
            let to_index = usize::from(to);
            if layer[to_index] == 0 {
                layer[to_index] = layer[v] + 1;
                queue.push(to);
            }
        }
    }
    if usize::from(layer[usize::from(last)]) != length {
        return;
    }

    // Extend the record only along edges that increase the BFS distance.
    let mut possible = vec![false; layer.len()];
    possible[usize::from(last)] = true;
    for v in queue.into_iter().map(usize::from) {
        if possible[v] {
            for to in adjacent(v).iter().copied().map(usize::from) {
                if layer[to] == layer[v] + 1 {
                    possible[to] = true;
                }
            }
        }
    }

    let mut output = BufWriter::new(io::stdout().lock());
    for (station, v) in index.into_iter().enumerate() {
        if possible[usize::from(v)] {
            writeln!(output, "{}", station).unwrap();
        }
    }
}
