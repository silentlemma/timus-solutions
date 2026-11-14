use std::io::{self, BufWriter, Read, Write};

const SMALLEST_CYCLE: usize = 3;

fn pairs(size: usize) -> usize {
    size * (size - 1) / 2
}

fn cycles(n: usize, mut target: usize) -> Option<Vec<usize>> {
    let mut minimum = vec![n as u8 + 1; target + 1];
    let mut last = vec![0u8; target + 1];
    minimum[0] = 0;
    // Minimize the vertices in cycles; every leftover vertex becomes a singleton.
    for size in SMALLEST_CYCLE..=n {
        let weight = pairs(size);
        for total in weight..=target {
            let count = minimum[total - weight] + size as u8;
            if count < minimum[total] {
                minimum[total] = count;
                last[total] = size as u8;
            }
        }
    }
    if usize::from(minimum[target]) > n {
        return None;
    }
    let mut sizes = Vec::new();
    while target > 0 {
        let size = usize::from(last[target]);
        sizes.push(size);
        target -= pairs(size);
    }
    Some(sizes)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let n = numbers.next().unwrap();
    let k = numbers.next().unwrap();
    let mut output = BufWriter::new(io::stdout().lock());
    let Some(sizes) = pairs(n).checked_sub(k).and_then(|target| cycles(n, target)) else {
        writeln!(output, "-1").unwrap();
        return;
    };
    let (mut first, mut previous) = (1, 0);
    for size in sizes {
        if previous != 0 {
            writeln!(output, "{} {}", previous, first).unwrap();
        }
        for vertex in first..first + size - 1 {
            writeln!(output, "{} {}", vertex, vertex + 1).unwrap();
        }
        writeln!(output, "{} {}", first + size - 1, first).unwrap();
        previous = first;
        first += size;
    }
    for vertex in first..=n {
        if previous != 0 {
            writeln!(output, "{} {}", previous, vertex).unwrap();
        }
        previous = vertex;
    }
}
