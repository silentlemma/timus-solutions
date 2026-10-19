use std::fmt::Write;
use std::io::{self, Read};

fn fixed_directions(
    values: &[i32],
    first_direction: i32,
    second_direction: i32,
) -> Option<[Vec<i32>; 2]> {
    let size = values.len();
    let direction = [first_direction, second_direction];
    let mut other = [
        if second_direction == 1 {
            0
        } else {
            size as i32 + 1
        },
        if first_direction == 1 {
            0
        } else {
            size as i32 + 1
        },
    ];
    let mut parent = [vec![0_u8; size], vec![0_u8; size]];
    let mut previous = values[0];
    for index in 1..size {
        let value = values[index];
        let mut next = [-1, -1];
        for owner in 0..2 {
            if other[owner] >= 0 && direction[owner] * (value - previous) > 0 {
                next[owner] = other[owner];
                parent[owner][index] = owner as u8;
            }
            if other[1 - owner] >= 0 && direction[owner] * (value - other[1 - owner]) > 0 {
                if next[owner] < 0 || direction[1 - owner] * (previous - next[owner]) < 0 {
                    next[owner] = previous;
                    parent[owner][index] = (1 - owner) as u8;
                }
            }
        }
        if next[0] < 0 && next[1] < 0 {
            return None;
        }
        other = next;
        previous = value;
    }
    let mut owner = if other[0] >= 0 { 0 } else { 1 };
    let mut assignment = vec![0; size];
    let mut counts = [0, 0];
    for index in (0..size).rev() {
        assignment[index] = owner;
        counts[owner] += 1;
        owner = parent[owner][index] as usize;
    }
    if counts[0] == 0 {
        assignment[size - 1] = 0;
    }
    if counts[1] == 0 {
        assignment[size - 1] = 1;
    }
    let mut groups = [Vec::new(), Vec::new()];
    for (index, &value) in values.iter().enumerate() {
        groups[assignment[index]].push(value);
    }
    Some(groups)
}

fn partition(values: &[i32]) -> Option<[Vec<i32>; 2]> {
    for (first, second) in [(1, 1), (-1, -1), (1, -1), (-1, 1)] {
        if let Some(groups) = fixed_directions(values, first, second) {
            return Some(groups);
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let size: usize = words.next().unwrap().parse().unwrap();
    let values: Vec<i32> = words.take(size).map(|w| w.parse().unwrap()).collect();
    if let Some(groups) = partition(&values) {
        let mut output = format!("{} {}\n", groups[0].len(), groups[1].len());
        for group in groups {
            for value in group {
                write!(&mut output, "{} ", value).unwrap();
            }
            output.push('\n');
        }
        print!("{}", output);
    } else {
        println!("Fail");
    }
}
