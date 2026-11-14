use std::io::{self, Read, Write};

const CAPACITY: usize = 4096;
const MAX_VALUE: i64 = 1_000_000_000;
const HASH_MULTIPLIER: u32 = 2_654_435_761;
const HASH_FOLD: u32 = 16;
const SLOT_SHIFT: u32 = u32::BITS - CAPACITY.trailing_zeros();

struct Positions {
    values: [u32; CAPACITY],
    indices: [u16; CAPACITY],
}

impl Positions {
    fn slot(&self, value: u32) -> usize {
        let hash = value ^ (value >> HASH_FOLD);
        let mut slot = (hash.wrapping_mul(HASH_MULTIPLIER) >> SLOT_SHIFT) as usize;
        while self.indices[slot] != 0 && self.values[slot] != value {
            slot = (slot + 1) & (CAPACITY - 1);
        }
        slot
    }

    fn find(&self, value: i64) -> u16 {
        if (0..=MAX_VALUE).contains(&value) {
            self.indices[self.slot(value as u32)]
        } else {
            0
        }
    }

    fn insert(&mut self, value: u32, index: u16) -> bool {
        let slot = self.slot(value);
        if self.indices[slot] != 0 {
            return false;
        }
        self.values[slot] = value;
        self.indices[slot] = index;
        true
    }
}

fn main() {
    let mut input = String::new();
    io::stdin().lock().read_to_string(&mut input).unwrap();
    let mut fields = input.split_ascii_whitespace();
    let count = fields.next().unwrap().parse::<u16>().unwrap();
    let mut positions = Positions {
        values: [0; CAPACITY],
        indices: [0; CAPACITY],
    };
    let mut values = Vec::with_capacity(count as usize);
    for index in 1..=count {
        let value = fields.next().unwrap().parse::<u32>().unwrap();
        if positions.insert(value, index) {
            values.push(i64::from(value));
        }
    }
    values.sort_unstable();
    let maximum = *values.last().unwrap();
    let (mut best, mut first, mut step) = (1i64, values[0], 0i64);
    for (index, &start) in values.iter().enumerate() {
        if values.len() - index <= best as usize {
            break;
        }
        for &second in &values[index + 1..] {
            let delta = second - start;
            // The (best + 1)-st term must exist to improve the record.
            let required = start + best * delta;
            if required > maximum {
                break;
            }
            if (best > 1 && positions.find(required) == 0) || positions.find(start - delta) != 0 {
                continue;
            }
            let mut length = 2;
            let mut next = second + delta;
            while positions.find(next) != 0 {
                length += 1;
                next += delta;
            }
            if length > best {
                (best, first, step) = (length, start, delta);
            }
        }
    }
    let mut output = io::BufWriter::new(io::stdout().lock());
    writeln!(output, "{}", best).unwrap();
    for offset in 0..best {
        if offset != 0 {
            write!(output, " ").unwrap();
        }
        write!(output, "{}", positions.find(first + offset * step)).unwrap();
    }
    writeln!(output).unwrap();
}
