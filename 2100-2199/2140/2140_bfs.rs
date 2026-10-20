use std::fmt::Write as _;
use std::io::{self, Read, Write};
use std::str::SplitWhitespace;

const PADDING: usize = 2;
const DIRECTION_COUNT: usize = 4;
const MOVE_COUNT: usize = 4;
const WALK: usize = 0;
const JUMP: usize = 1;
const DROP: usize = 2;
const CLIMB: usize = 3;
const UNVISITED: i32 = -1;
const MOVE_NAMES: [&str; MOVE_COUNT] = ["walk", "jump", "drop", "climb"];
const DIRECTION_NAMES: [&str; DIRECTION_COUNT] = ["north", "east", "south", "west"];

fn read_number(tokens: &mut SplitWhitespace<'_>) -> usize {
    tokens.next().unwrap().parse().unwrap()
}

fn read_position(tokens: &mut SplitWhitespace<'_>, width: usize, plane: usize) -> usize {
    let x = read_number(tokens);
    let y = read_number(tokens);
    let z = read_number(tokens);
    z * plane + (x + PADDING - 1) * width + y + PADDING - 1
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let length = read_number(&mut tokens);
    let breadth = read_number(&mut tokens);
    let height = read_number(&mut tokens);
    let width = breadth + 2 * PADDING;
    let rows = length + 2 * PADDING;
    let plane = width * rows;
    let volume = (height + 2) * plane;
    let mut air = vec![false; volume];
    for z in 1..=height {
        for x in 1..=length {
            let row = tokens.next().unwrap().as_bytes();
            let base = z * plane + (x + PADDING - 1) * width + PADDING;
            for y in 0..breadth {
                air[base + y] = row[y] == b'.';
            }
        }
    }
    let start = read_position(&mut tokens, width, plane);
    let goal = read_position(&mut tokens, width, plane);
    let mut stand = vec![false; volume];
    for cell in plane..volume {
        stand[cell] = air[cell] && !air[cell - plane];
    }

    let deltas = [-(width as isize), 1, width as isize, -1];
    let mut parent = vec![UNVISITED; volume];
    let mut action = vec![0; volume];
    let mut queue = Vec::with_capacity(length * breadth * height);
    queue.push(start);
    parent[start] = start as i32;
    let mut head = 0;
    while head < queue.len() && parent[goal] == UNVISITED {
        let current = queue[head];
        head += 1;
        for (direction, &delta) in deltas.iter().enumerate() {
            let near = (current as isize + delta) as usize;
            let far = (near as isize + delta) as usize;
            let candidates = [
                (near, WALK, stand[near]),
                (far, JUMP, air[near] && air[near - plane] && stand[far]),
                (near - plane, DROP, air[near] && stand[near - plane]),
                (
                    near + plane,
                    CLIMB,
                    air[current + plane] && stand[near + plane],
                ),
            ];
            for (next, kind, allowed) in candidates {
                if allowed && parent[next] == UNVISITED {
                    parent[next] = current as i32;
                    action[next] = kind * DIRECTION_COUNT + direction;
                    queue.push(next);
                }
            }
        }
    }

    let mut output = String::new();
    if parent[goal] == UNVISITED {
        output.push_str("NO\n");
    } else {
        let mut moves = Vec::new();
        let mut current = goal;
        while current != start {
            moves.push(action[current]);
            current = parent[current] as usize;
        }
        writeln!(output, "YES\n{}", moves.len()).unwrap();
        for &step in moves.iter().rev() {
            writeln!(
                output,
                "{} {}",
                MOVE_NAMES[step / DIRECTION_COUNT],
                DIRECTION_NAMES[step % DIRECTION_COUNT]
            )
            .unwrap();
        }
    }
    io::BufWriter::new(io::stdout())
        .write_all(output.as_bytes())
        .unwrap();
}
