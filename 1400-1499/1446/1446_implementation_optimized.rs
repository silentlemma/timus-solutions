use std::io::{self, BufRead, Write};

const HOUSE_COUNT: usize = 4;
const HOUSES: [&str; HOUSE_COUNT] = ["Slytherin", "Hufflepuff", "Gryffindor", "Ravenclaw"];

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut header = String::new();
    input.read_line(&mut header).unwrap();
    let n: usize = header.trim().parse().unwrap();
    // the input is read line by line, and each name goes straight into the
    // byte buffer of its house
    let mut lists: Vec<Vec<u8>> = (0..HOUSE_COUNT).map(|_| Vec::new()).collect();
    let mut name = Vec::new();
    let mut house = String::new();
    for _ in 0..n {
        // names keep their inner spaces, so only the line break is dropped
        name.clear();
        input.read_until(b'\n', &mut name).unwrap();
        while matches!(name.last(), Some(b'\n' | b'\r')) {
            name.pop();
        }
        house.clear();
        input.read_line(&mut house).unwrap();
        let h = HOUSES.iter().position(|&s| s == house.trim()).unwrap();
        lists[h].extend_from_slice(&name);
        lists[h].push(b'\n');
    }
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for h in 0..HOUSE_COUNT {
        if h > 0 {
            writeln!(out).unwrap();
        }
        writeln!(out, "{}:", HOUSES[h]).unwrap();
        out.write_all(&lists[h]).unwrap();
    }
}
