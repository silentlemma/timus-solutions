use std::io::{self, BufRead, BufWriter, Write};

const MAX_VERTICES: usize = 100;
const INFINITY: u16 = 32767;

fn number(input: &mut impl BufRead) -> Option<usize> {
    let mut value = 0;
    let mut started = false;
    loop {
        let buffer = input.fill_buf().unwrap();
        if buffer.is_empty() {
            return if started { Some(value) } else { None };
        }
        let mut consumed = 0;
        for &byte in buffer {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = value * 10 + usize::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return Some(value);
            } else if byte == b'-' {
                return None;
            }
        }
        input.consume(consumed);
    }
}

fn solve(n: usize, input: &mut impl BufRead, output: &mut impl Write) -> io::Result<()> {
    let roads = number(input).unwrap();
    let mut direct = [[INFINITY; MAX_VERTICES]; MAX_VERTICES];
    let mut next = [[0u8; MAX_VERTICES]; MAX_VERTICES];
    for i in 0..n {
        direct[i][i] = 0;
        for j in 0..n {
            next[i][j] = j as u8;
        }
    }
    for _ in 0..roads {
        let a = number(input).unwrap() - 1;
        let b = number(input).unwrap() - 1;
        let length = number(input).unwrap() as u16;
        direct[a][b] = direct[a][b].min(length);
        direct[b][a] = direct[a][b];
    }

    let mut distance = direct;
    let mut best = u32::from(INFINITY);
    let mut cycle = [0; MAX_VERTICES];
    let mut count = 0;
    for k in 0..n {
        for i in 0..k {
            let left = u32::from(direct[k][i]);
            if left >= best {
                continue;
            }
            for j in i + 1..k {
                let length = left + u32::from(direct[k][j]) + u32::from(distance[i][j]);
                if length < best {
                    best = length;
                    count = 0;
                    let mut v = i;
                    while v != j {
                        cycle[count] = v;
                        count += 1;
                        v = usize::from(next[v][j]);
                    }
                    cycle[count] = j;
                    cycle[count + 1] = k;
                    count += 2;
                }
            }
        }
        for i in 0..n {
            let left = u32::from(distance[k][i]);
            if i == k || left >= best {
                continue;
            }
            for j in i + 1..n {
                let length = left + u32::from(distance[k][j]);
                if length < best && length < u32::from(distance[i][j]) {
                    distance[i][j] = length as u16;
                    distance[j][i] = length as u16;
                    next[i][j] = next[i][k];
                    next[j][i] = next[j][k];
                }
            }
        }
    }
    if count == 0 {
        return writeln!(output, "No solution.");
    }
    for (i, &vertex) in cycle[..count].iter().enumerate() {
        if i > 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{}", vertex + 1)?;
    }
    writeln!(output)
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let mut input = stdin.lock();
    let mut output = BufWriter::new(stdout.lock());
    while let Some(n) = number(&mut input) {
        solve(n, &mut input, &mut output)?;
    }
    output.flush()
}
