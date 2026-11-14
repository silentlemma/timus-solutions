use std::io::{self, BufWriter, Read, Write};

const MAX_ROUTE: usize = 2000;

#[derive(Clone, Copy, Default)]
struct Bus {
    front: u16,
    back: u16,
    next: u16,
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<u16>().unwrap());
    let count = usize::from(numbers.next().unwrap());
    let mut first = [0u16; MAX_ROUTE + 1];
    let mut buses = vec![Bus::default(); count + 1];
    for (id, bus) in buses.iter_mut().enumerate().skip(1) {
        let front = numbers.next().unwrap();
        let back = numbers.next().unwrap();
        *bus = Bus {
            front,
            back,
            next: first[usize::from(front)],
        };
        first[usize::from(front)] = id as u16;
    }
    let (target, left, right) = (
        numbers.next().unwrap(),
        numbers.next().unwrap(),
        numbers.next().unwrap(),
    );
    let target = usize::from(target);
    let mut previous = [0u16; MAX_ROUTE + 1];
    let mut seen = [false; MAX_ROUTE + 1];
    let mut queue = vec![left];
    if right != left {
        queue.push(right);
    }
    seen[usize::from(left)] = true;
    seen[usize::from(right)] = true;

    // A swap makes the back route available using one more exchange.
    let mut head = 0;
    while head < queue.len() && !seen[target] {
        let mut id = first[usize::from(queue[head])];
        head += 1;
        while id != 0 {
            let bus = buses[usize::from(id)];
            let route = usize::from(bus.back);
            if !seen[route] {
                seen[route] = true;
                previous[route] = id;
                queue.push(bus.back);
            }
            id = bus.next;
        }
    }
    if !seen[target] {
        println!("IMPOSSIBLE");
        return Ok(());
    }
    let mut path = Vec::new();
    let mut id = previous[target];
    while id != 0 {
        path.push(id);
        id = previous[usize::from(buses[usize::from(id)].front)];
    }
    let mut output = BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", path.len())?;
    for bus in path.iter().rev() {
        writeln!(output, "{bus}")?;
    }
    output.flush()
}
