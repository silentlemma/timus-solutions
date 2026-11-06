use std::io::{self, Read, Write};

const MAX_COORD: usize = 10;
const SIDE: usize = MAX_COORD + 2;
const CELLS: usize = SIDE * SIDE;
const DIRECTIONS: [(u8, isize); 4] = [
    (b'R', SIDE as isize),
    (b'T', 1),
    (b'L', -(SIDE as isize)),
    (b'B', -1),
];

fn coordinates(output: &mut impl Write, pixel: usize) -> io::Result<()> {
    writeln!(output, "{} {}", pixel / SIDE, pixel % SIDE)
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let (header, data) = input.split_once('\n').unwrap();
    let mut header = header
        .split_ascii_whitespace()
        .map(|s| s.parse::<usize>().unwrap());
    let first = header.next().unwrap();
    let mut output = io::BufWriter::new(io::stdout().lock());
    let mut queue = [0u8; MAX_COORD * MAX_COORD];
    let mut marked = [false; CELLS];
    let mut end = 1;

    if let Some(y) = header.next() {
        let start = first * SIDE + y;
        queue[0] = start as u8;
        marked[start] = true;
        for (head, row) in data.split_ascii_whitespace().enumerate() {
            let pixel = isize::from(queue[head]);
            for code in row.bytes() {
                if let Some((_, step)) = DIRECTIONS.iter().find(|&&(letter, _)| letter == code) {
                    let next = (pixel + step) as usize;
                    queue[end] = next as u8;
                    end += 1;
                    marked[next] = true;
                }
            }
        }
        writeln!(output, "{}", end)?;
        // The flat bitmap is already in coordinate order.
        for (pixel, &black) in marked.iter().enumerate() {
            if black {
                coordinates(&mut output, pixel)?;
            }
        }
    } else {
        let count = first;
        let mut tokens = data
            .split_ascii_whitespace()
            .map(|s| s.parse::<usize>().unwrap());
        let mut start = CELLS;
        for _ in 0..count {
            let pixel = tokens.next().unwrap() * SIDE + tokens.next().unwrap();
            marked[pixel] = true;
            start = start.min(pixel);
        }
        queue[0] = start as u8;
        marked[start] = false;
        coordinates(&mut output, start)?;
        for head in 0..count {
            for (letter, step) in DIRECTIONS {
                let next = (isize::from(queue[head]) + step) as usize;
                if marked[next] {
                    marked[next] = false;
                    queue[end] = next as u8;
                    end += 1;
                    output.write_all(&[letter])?;
                }
            }
            output.write_all(if head + 1 == count { b".\n" } else { b",\n" })?;
        }
    }
    output.flush()
}
