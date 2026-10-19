use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn insert_ear(
    successor: &mut [usize],
    mut first: usize,
    mut second: usize,
    mut outer_first: usize,
    mut outer_second: usize,
) {
    if successor[first] != second {
        std::mem::swap(&mut first, &mut second);
        std::mem::swap(&mut outer_first, &mut outer_second);
    }
    successor[first] = outer_first;
    successor[outer_first] = outer_second;
    successor[outer_second] = second;
}

fn construct_cycle(size: usize, length: usize) -> Option<Vec<usize>> {
    if length % 2 != 0 || length > size * size - size % 2 {
        return None;
    }
    let mut successor = vec![0; size * size];
    let initial = [0, 1, size + 1, size];
    for (index, &vertex) in initial.iter().enumerate() {
        successor[vertex] = initial[(index + 1) % initial.len()];
    }
    let mut used = initial.len();
    let width = size - size % 2;
    let mut column = 2;
    while column < width && used < length {
        insert_ear(
            &mut successor,
            column - 1,
            size + column - 1,
            column,
            size + column,
        );
        used += 2;
        column += 1;
    }
    let mut row = 2;
    while row < size && used < length {
        let mut column = 0;
        while column < width && used < length {
            let upper = (row - 1) * size + column;
            let lower = row * size + column;
            insert_ear(&mut successor, upper, upper + 1, lower, lower + 1);
            used += 2;
            column += 2;
        }
        row += 1;
    }
    if size % 2 != 0 {
        let mut row = 0;
        while row < size - 1 && used < length {
            let left = row * size + width - 1;
            insert_ear(&mut successor, left, left + size, left + 1, left + size + 1);
            used += 2;
            row += 2;
        }
    }
    let mut result = Vec::with_capacity(length);
    let mut current = 0;
    for _ in 0..length {
        result.push(current);
        current = successor[current];
    }
    Some(result)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let size = tokens.next().unwrap().parse::<usize>().unwrap();
    let length = tokens.next().unwrap().parse::<usize>().unwrap();
    let mut output = String::new();
    if let Some(cycle) = construct_cycle(size, length) {
        output.push_str("Overwhelming power of magic\n");
        for vertex in cycle {
            writeln!(output, "{} {}", vertex / size + 1, vertex % size + 1).unwrap();
        }
    } else {
        output.push_str("Unsuitable device\n");
    }
    print!("{}", output);
}
