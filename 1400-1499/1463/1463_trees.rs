use std::io::{self, BufRead, BufWriter, Write};

#[derive(Clone, Copy, Default)]
struct City {
    arm: u32,
    joy: u16,
    degree: u16,
    neighbor: u16,
    weight: u16,
    child: u16,
}

impl City {
    fn add(&mut self, neighbor: u16, weight: u16) {
        self.degree += 1;
        self.neighbor ^= neighbor;
        self.weight ^= weight;
    }
}

fn number(input: &mut impl BufRead) -> usize {
    let mut value = 0;
    let mut started = false;
    loop {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            return value;
        }
        let mut consumed = 0;
        for &byte in bytes {
            consumed += 1;
            if byte.is_ascii_digit() {
                value = value * 10 + usize::from(byte - b'0');
                started = true;
            } else if started {
                input.consume(consumed);
                return value;
            }
        }
        input.consume(consumed);
    }
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let (count, flights) = (number(&mut input), number(&mut input));
    let mut cities = vec![City::default(); count + 1];
    let mut center = 1u16;
    let mut best = 0;
    for (index, city) in cities.iter_mut().enumerate().skip(1) {
        city.joy = number(&mut input) as u16;
        if u32::from(city.joy) > best {
            center = index as u16;
            best = u32::from(city.joy);
        }
    }
    for _ in 0..flights {
        let a = number(&mut input) as u16;
        let b = number(&mut input) as u16;
        let weight = number(&mut input) as u16;
        cities[usize::from(a)].add(b, weight);
        cities[usize::from(b)].add(a, weight);
    }

    let mut leaves = Vec::with_capacity(count);
    leaves.extend(
        (1..=count)
            .filter(|&v| cities[v].degree == 1)
            .map(|v| v as u16),
    );
    let (mut cursor, mut left, mut right) = (0, 0, 0);
    while cursor < leaves.len() {
        let v = leaves[cursor];
        cursor += 1;
        let leaf = cities[usize::from(v)];
        if leaf.degree == 0 {
            continue;
        }
        // The XOR fields of a leaf contain its one remaining edge.
        let parent = &mut cities[usize::from(leaf.neighbor)];
        parent.degree -= 1;
        parent.neighbor ^= v;
        parent.weight ^= leaf.weight;
        if parent.degree == 1 {
            leaves.push(leaf.neighbor);
        }
        let arm = leaf.arm + u32::from(leaf.joy) + u32::from(leaf.weight);
        let total = u32::from(parent.joy) + parent.arm + arm;
        if total > best {
            best = total;
            (center, left, right) = (leaf.neighbor, v, parent.child);
        }
        if arm > parent.arm {
            (parent.arm, parent.child) = (arm, v);
        }
    }

    let mut route = leaves;
    route.clear();
    while left != 0 {
        route.push(left);
        left = cities[usize::from(left)].child;
    }
    route.reverse();
    route.push(center);
    while right != 0 {
        route.push(right);
        right = cities[usize::from(right)].child;
    }
    let stdout = io::stdout();
    let mut output = BufWriter::new(stdout.lock());
    writeln!(output, "{best}\n{}", route.len())?;
    for (i, city) in route.iter().enumerate() {
        if i != 0 {
            output.write_all(b" ")?;
        }
        write!(output, "{city}")?;
    }
    writeln!(output)?;
    output.flush()
}
