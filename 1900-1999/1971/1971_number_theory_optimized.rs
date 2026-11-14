use std::collections::HashMap;
use std::io::{self, BufRead, BufWriter, Write};

const MAX_FACTOR: usize = 100;
const LOW_FPS: u32 = 10;
const HIGH_FPS: u32 = 60;
const MIN_AREA: u32 = 320 * 200;
const MAX_POWER: u32 = 1_000_000_000;
const CAP: u32 = MAX_POWER / (LOW_FPS * MIN_AREA) + 1;
const EXACT_LIMIT: usize = 10;
const ALPHABET_BASE: u64 = 27;

fn name(bytes: &[u8]) -> u64 {
    bytes
        .iter()
        .fold(0, |key, &c| key * ALPHABET_BASE + u64::from(c - b'a' + 1))
}

fn number(bytes: &[u8]) -> u32 {
    const DECIMAL: u32 = 10;
    bytes
        .iter()
        .fold(0, |value, &c| value * DECIMAL + u32::from(c - b'0'))
}

fn fields(line: &[u8]) -> impl Iterator<Item = &[u8]> {
    line.split(u8::is_ascii_whitespace)
        .filter(|word| !word.is_empty())
}

fn read_line(input: &mut impl BufRead, line: &mut Vec<u8>) -> io::Result<()> {
    loop {
        line.clear();
        if input.read_until(b'\n', line)? == 0 || fields(line).next().is_some() {
            return Ok(());
        }
    }
}

struct Effects {
    counts: [u32; MAX_FACTOR + 1],
    active: usize,
    product: u32,
}

impl Effects {
    fn add(&mut self, factor: u8) {
        self.active += 1;
        self.counts[usize::from(factor)] += 1;
        self.product = (self.product * u32::from(factor)).min(CAP);
    }

    fn remove(&mut self, factor: u8) {
        self.active -= 1;
        self.counts[usize::from(factor)] -= 1;
        if self.product < CAP {
            self.product /= u32::from(factor);
        } else if self.active <= EXACT_LIMIT {
            // A capped product must be rebuilt from the retained multiplicities.
            self.product = 1;
            for (factor, &count) in self.counts.iter().enumerate() {
                for _ in 0..count {
                    self.product = (self.product * factor as u32).min(CAP);
                    if self.product == CAP {
                        return;
                    }
                }
            }
        }
    }

    fn status(&self, area: u32, power: u32) -> &'static [u8] {
        if self.product > power / (LOW_FPS * area) {
            b"Slideshow\n"
        } else if self.product <= power / (HIGH_FPS * area) {
            b"Perfect\n"
        } else {
            b"So-so\n"
        }
    }
}

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut output = BufWriter::new(io::stdout().lock());
    let mut line = Vec::new();
    read_line(&mut input, &mut line)?;
    let n = number(fields(&line).next().unwrap()) as usize;
    let mut options = HashMap::with_capacity(n);
    let mut effects = Effects {
        counts: [0; MAX_FACTOR + 1],
        active: 0,
        product: 1,
    };
    for _ in 0..n {
        read_line(&mut input, &mut line)?;
        let mut values = fields(&line);
        let key = name(values.next().unwrap());
        let factor = number(values.next().unwrap()) as u8;
        options.insert(key, factor);
        effects.add(factor);
    }
    read_line(&mut input, &mut line)?;
    let (mut area, power) = {
        let mut values = fields(&line).map(number);
        let area = values.next().unwrap() * values.next().unwrap();
        (area, values.next().unwrap())
    };
    read_line(&mut input, &mut line)?;
    let changes = number(fields(&line).next().unwrap());
    output.write_all(effects.status(area, power))?;
    for _ in 0..changes {
        read_line(&mut input, &mut line)?;
        let mut values = fields(&line);
        let command = values.next().unwrap();
        let first = values.next().unwrap();
        if command == b"Resolution" {
            area = number(first) * number(values.next().unwrap());
        } else {
            let factor = options[&name(first)];
            if command == b"On" {
                effects.add(factor);
            } else {
                effects.remove(factor);
            }
        }
        output.write_all(effects.status(area, power))?;
    }
    output.flush()
}
