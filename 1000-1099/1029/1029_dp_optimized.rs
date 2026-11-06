use std::io::{self, BufRead, Write};

#[derive(Clone, Copy)]
enum Parent {
    Below,
    Left,
    Right,
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut line = String::new();
    input.read_line(&mut line)?;
    let mut dimensions = line.split_ascii_whitespace().map(|s| s.parse().unwrap());
    let floors: usize = dimensions.next().unwrap();
    let rooms: usize = dimensions.next().unwrap();

    let mut costs = vec![0u64; rooms];
    let mut fees = vec![0u64; rooms];
    let mut parents = vec![Parent::Below; floors * rooms];
    for floor in 0..floors {
        line.clear();
        input.read_line(&mut line)?;
        let mut tokens = line.split_ascii_whitespace();
        let directions = &mut parents[floor * rooms..(floor + 1) * rooms];
        for (cost, fee) in costs.iter_mut().zip(&mut fees) {
            *fee = tokens.next().unwrap().parse().unwrap();
            *cost += *fee;
        }
        for room in 1..rooms {
            let from_left = costs[room - 1] + fees[room];
            if from_left < costs[room] {
                costs[room] = from_left;
                directions[room] = Parent::Left;
            }
        }
        for room in (0..rooms - 1).rev() {
            let from_right = costs[room + 1] + fees[room];
            if from_right < costs[room] {
                costs[room] = from_right;
                directions[room] = Parent::Right;
            }
        }
    }

    let mut room = costs
        .iter()
        .enumerate()
        .min_by_key(|&(_, cost)| cost)
        .unwrap()
        .0;
    let mut floor = floors - 1;
    let mut path = Vec::new();
    loop {
        path.push((room + 1) as u16);
        match parents[floor * rooms + room] {
            Parent::Below if floor == 0 => break,
            Parent::Below => floor -= 1,
            Parent::Left => room -= 1,
            Parent::Right => room += 1,
        }
    }
    let mut output = io::BufWriter::new(io::stdout().lock());
    for (i, room) in path.iter().rev().enumerate() {
        if i != 0 {
            write!(output, " ")?;
        }
        write!(output, "{room}")?;
    }
    writeln!(output)?;
    output.flush()
}
