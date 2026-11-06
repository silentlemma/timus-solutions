use std::io::{self, BufRead, Read};

const ALPHABET: usize = 26;

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut counts = [0u32; ALPHABET];
    let mut started = false;
    loop {
        let bytes = input.fill_buf()?;
        if bytes.is_empty() {
            break;
        }
        let mut consumed = 0;
        let mut finished = false;
        for &ch in bytes {
            consumed += 1;
            if ch.is_ascii_lowercase() {
                started = true;
                counts[usize::from(ch - b'a')] += 1;
            } else if started {
                finished = true;
                break;
            }
        }
        input.consume(consumed);
        if finished {
            break;
        }
    }
    let mut tail = String::new();
    input.read_to_string(&mut tail)?;
    let limit: usize = tail.trim().parse().unwrap();
    counts.sort_unstable();
    let boundary = counts[ALPHABET - limit];
    let size: u32 = counts[ALPHABET - limit..].iter().sum();
    let mut ways = 1u32;
    if boundary != 0 {
        let first = counts.partition_point(|&count| count < boundary);
        let end = counts.partition_point(|&count| count <= boundary);
        let tied = end - first;
        let selected = end - (ALPHABET - limit);
        for i in 1..=selected {
            ways = ways * (tied - i + 1) as u32 / i as u32;
        }
    }
    println!("{size} {ways}");
    Ok(())
}
