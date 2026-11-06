use std::io::{self, Read};

const FRESH: u8 = 0;
const WALKING: u8 = 1;
const DONE: u8 = 2;

fn main() -> io::Result<()> {
    let (successor, incoming) = {
        let mut input = String::new();
        io::stdin().read_to_string(&mut input)?;
        let mut tokens = input.split_ascii_whitespace();
        let size: usize = tokens.next().unwrap().parse().unwrap();
        let mut successor = Vec::with_capacity(size + 1);
        successor.push(0);
        let mut incoming = vec![0u8; size + 1];
        for token in tokens.take(size) {
            let next: u32 = token.parse().unwrap();
            successor.push(next);
            let count = &mut incoming[next as usize];
            // Only zero, one, and more than one incoming edge matter.
            *count = (*count + 1).min(2);
        }
        (successor, incoming)
    };
    let size = successor.len() - 1;
    let mut state = vec![FRESH; size + 1];
    let (mut cycles, mut cycle_nodes, mut isolated_cycles) = (0, 0, 0);
    for start in 1..=size {
        let mut node = start;
        while state[node] == FRESH {
            state[node] = WALKING;
            node = successor[node] as usize;
        }
        if state[node] == WALKING {
            cycles += 1;
            let cycle_start = node;
            let mut isolated = true;
            loop {
                cycle_nodes += 1;
                isolated &= incoming[node] == 1;
                node = successor[node] as usize;
                if node == cycle_start {
                    break;
                }
            }
            isolated_cycles += usize::from(isolated);
        }
        // Follow the same arrows to clear this walk without storing its path.
        node = start;
        while state[node] == WALKING {
            state[node] = DONE;
            node = successor[node] as usize;
        }
    }
    let starts = incoming[1..].iter().filter(|&&count| count == 0).count();
    println!(
        "{} {}",
        starts + isolated_cycles,
        size - cycle_nodes + cycles
    );
    Ok(())
}
