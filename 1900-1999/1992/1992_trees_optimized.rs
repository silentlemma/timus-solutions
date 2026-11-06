use std::io::{self, BufRead, Write};

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut output = io::BufWriter::new(io::stdout().lock());
    let mut line = String::new();
    input.read_line(&mut line)?;
    let count: usize = line
        .split_ascii_whitespace()
        .next()
        .unwrap()
        .parse()
        .unwrap();

    // A command creates at most one stack node or one entity.
    // Allocate nodes from the front and entity heads from the back.
    let end = count + 2;
    let mut arena = vec![[0u32; 2]; end];
    let mut used = 0;
    let mut entities = 1;
    for _ in 0..count {
        line.clear();
        input.read_line(&mut line)?;
        let mut tokens = line.split_ascii_whitespace();
        let command = tokens.next().unwrap();
        let entity: usize = tokens.next().unwrap().parse().unwrap();
        let slot = end - entity;
        let [learned, undone] = arena[slot];
        match command {
            "learn" => {
                let program = tokens.next().unwrap().parse().unwrap();
                used += 1;
                arena[used] = [program, learned];
                arena[slot] = [used as u32, 0];
            }
            "rollback" => {
                let [program, previous] = arena[learned as usize];
                used += 1;
                arena[used] = [program, undone];
                arena[slot] = [previous, used as u32];
            }
            "relearn" => {
                let [program, previous] = arena[undone as usize];
                used += 1;
                arena[used] = [program, learned];
                arena[slot] = [used as u32, previous];
            }
            "clone" => {
                entities += 1;
                arena[end - entities] = [learned, undone];
            }
            _ => {
                if learned == 0 {
                    writeln!(output, "basic")?;
                } else {
                    writeln!(output, "{}", arena[learned as usize][0])?;
                }
            }
        }
    }
    output.flush()
}
