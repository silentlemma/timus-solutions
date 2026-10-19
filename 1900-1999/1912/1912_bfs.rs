use std::collections::VecDeque;
use std::io::{self, Read};

const ORIENTATIONS: usize = 4;

struct Transition {
    player: usize,
    mask: u8,
    change: i32,
    offset: isize,
}

fn minimum_passages(rows: usize, columns: usize, scheme: &[Vec<u8>]) -> Option<i32> {
    let (height, width) = (rows + 2, columns + 2);
    let size = height * width;
    let moves = [(-1_i32, 0_i32), (0, 1), (1, 0), (0, -1)];
    let offsets = [-(width as isize), 1, width as isize, -1];
    let mut outside = vec![false; size];
    let mut masks = vec![0_u8; size];
    let mut starts = Vec::new();
    for position in 0..size {
        let (row, column) = (position / width, position % width);
        outside[position] = row == 0 || row + 1 == height || column == 0 || column + 1 == width;
    }
    for row in 1..=rows {
        for column in 1..=columns {
            let position = row * width + column;
            let (r, c) = (2 * row - 1, 2 * column - 1);
            if scheme[r][c] == b'1' || scheme[r][c] == b'2' {
                starts.push(position);
            }
            let walls = [
                scheme[r - 1][c],
                scheme[r][c + 1],
                scheme[r + 1][c],
                scheme[r][c - 1],
            ];
            for (direction, &wall) in walls.iter().enumerate() {
                if wall == b'.' {
                    masks[position] |= 1 << direction;
                }
            }
        }
    }
    for position in 0..size {
        if !outside[position] {
            continue;
        }
        let (row, column) = ((position / width) as i32, (position % width) as i32);
        for (direction, &(dr, dc)) in moves.iter().enumerate() {
            let (nr, nc) = (row + dr, column + dc);
            if nr < 0 || nr >= height as i32 || nc < 0 || nc >= width as i32 {
                continue;
            }
            let neighbor = nr as usize * width + nc as usize;
            let opposite = (direction + 2) % moves.len();
            if outside[neighbor] || masks[neighbor] & (1 << opposite) != 0 {
                masks[position] |= 1 << direction;
            }
        }
    }
    let relative = [(0_i32, 1_i32), (1, -1), (1, 0), (1, 1)];
    let mut deltas = [0_usize; ORIENTATIONS];
    let mut transitions: Vec<Vec<Transition>> = (0..ORIENTATIONS).map(|_| Vec::new()).collect();
    for orientation in 0..ORIENTATIONS {
        deltas[orientation] =
            (relative[orientation].0 * width as i32 + relative[orientation].1) as usize;
        for player in 0..2 {
            for (direction, &(dr, dc)) in moves.iter().enumerate() {
                let mut positions = [(0, 0), relative[orientation]];
                positions[player].0 += dr;
                positions[player].1 += dc;
                if positions[1] < positions[0] {
                    positions.swap(0, 1);
                }
                let difference = (
                    positions[1].0 - positions[0].0,
                    positions[1].1 - positions[0].1,
                );
                if let Some(next) = relative.iter().position(|&point| point == difference) {
                    let shift = positions[0].0 * width as i32 + positions[0].1;
                    transitions[orientation].push(Transition {
                        player,
                        mask: 1 << direction,
                        change: shift * ORIENTATIONS as i32 + next as i32 - orientation as i32,
                        offset: offsets[direction],
                    });
                }
            }
        }
    }
    starts.sort_unstable();
    let orientation = deltas
        .iter()
        .position(|&delta| delta == starts[1] - starts[0])
        .unwrap();
    let initial = starts[0] * ORIENTATIONS + orientation;
    let mut distance = vec![-1_i32; size * ORIENTATIONS];
    let mut finished = vec![false; distance.len()];
    distance[initial] = 0;
    let mut pending = VecDeque::new();
    pending.push_back(initial);
    while let Some(state) = pending.pop_front() {
        if finished[state] {
            continue;
        }
        finished[state] = true;
        let current = distance[state];
        let (first, orientation) = (state / ORIENTATIONS, state % ORIENTATIONS);
        let second = first + deltas[orientation];
        if outside[first] && outside[second] {
            return Some(current);
        }
        for action in &transitions[orientation] {
            let position = if action.player == 0 { first } else { second };
            if masks[position] & action.mask == 0 {
                continue;
            }
            let neighbor = (position as isize + action.offset) as usize;
            let cost = if outside[position] && outside[neighbor] {
                0
            } else {
                1
            };
            let following = (state as i32 + action.change) as usize;
            let candidate = current + cost;
            if distance[following] == -1 || candidate < distance[following] {
                distance[following] = candidate;
                if cost == 0 {
                    pending.push_front(following);
                } else {
                    pending.push_back(following);
                }
            }
        }
    }
    None
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut lines = input.lines();
    let mut header = lines.next().unwrap().split_whitespace();
    let rows = header.next().unwrap().parse::<usize>().unwrap();
    let columns = header.next().unwrap().parse::<usize>().unwrap();
    let scheme: Vec<Vec<u8>> = (0..2 * rows + 1)
        .map(|_| lines.next().unwrap().as_bytes().to_vec())
        .collect();
    match minimum_passages(rows, columns, &scheme) {
        Some(answer) => println!("{}", answer),
        None => println!("Death"),
    }
}
