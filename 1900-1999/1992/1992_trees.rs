use std::io::{self, Read, Write};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let count: usize = tokens.next().unwrap().parse().unwrap();
    let _programs: usize = tokens.next().unwrap().parse().unwrap();
    let mut value = vec![0_u32; count + 2];
    let mut previous = vec![0_u32; count + 2];
    let mut learned = vec![0_u32; count + 2];
    let mut redo = vec![0_u32; count + 2];
    let mut used = 0;
    let mut entities = 1;
    let mut output = String::new();
    for _ in 0..count {
        let command = tokens.next().unwrap();
        let entity: usize = tokens.next().unwrap().parse().unwrap();
        match command {
            "learn" => {
                used += 1;
                value[used] = tokens.next().unwrap().parse().unwrap();
                previous[used] = learned[entity];
                learned[entity] = used as u32;
                redo[entity] = 0;
            }
            "rollback" => {
                let head = learned[entity] as usize;
                used += 1;
                value[used] = value[head];
                previous[used] = redo[entity];
                learned[entity] = previous[head];
                redo[entity] = used as u32;
            }
            "relearn" => {
                let head = redo[entity] as usize;
                used += 1;
                value[used] = value[head];
                previous[used] = learned[entity];
                redo[entity] = previous[head];
                learned[entity] = used as u32;
            }
            "clone" => {
                entities += 1;
                learned[entities] = learned[entity];
                redo[entities] = redo[entity];
            }
            _ => {
                let head = learned[entity] as usize;
                if head == 0 {
                    output.push_str("basic\n");
                } else {
                    output.push_str(&value[head].to_string());
                    output.push('\n');
                }
            }
        }
    }
    io::stdout().write_all(output.as_bytes()).unwrap();
}
