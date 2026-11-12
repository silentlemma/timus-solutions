use std::io::{self, Read, Write};

const MAX_PEOPLE: usize = 100;
const INPUT_SIZE: usize = 512;
const OUTPUT_SIZE: usize = 1024;
const DECIMAL_DIGITS: usize = 3;

struct Input<R: Read> {
    stream: R,
    bytes: [u8; INPUT_SIZE],
    position: usize,
    length: usize,
}

impl<R: Read> Input<R> {
    fn next(&mut self) -> u8 {
        if self.position == self.length {
            self.length = self.stream.read(&mut self.bytes).unwrap();
            self.position = 0;
            if self.length == 0 {
                return 0;
            }
        }
        let c = self.bytes[self.position];
        self.position += 1;
        c
    }
    fn number(&mut self) -> usize {
        let mut c = self.next();
        while c != 0 && c <= b' ' {
            c = self.next();
        }
        let mut value = 0;
        while c.is_ascii_digit() {
            value = value * 10 + (c - b'0') as usize;
            c = self.next();
        }
        value
    }
}

fn number(output: &mut [u8; OUTPUT_SIZE], used: &mut usize, mut value: usize) {
    let mut digits = [0_u8; DECIMAL_DIGITS];
    let mut count = 0;
    loop {
        digits[count] = b'0' + (value % 10) as u8;
        count += 1;
        value /= 10;
        if value == 0 {
            break;
        }
    }
    for &digit in digits[..count].iter().rev() {
        output[*used] = digit;
        *used += 1;
    }
}

fn main() {
    let stdin = io::stdin();
    let mut input = Input {
        stream: stdin.lock(),
        bytes: [0; INPUT_SIZE],
        position: 0,
        length: 0,
    };
    let n = input.number();
    let mut knows = [0_u128; MAX_PEOPLE];
    for row in &mut knows[..n] {
        loop {
            let friend = input.number();
            if friend == 0 {
                break;
            }
            *row |= 1_u128 << (friend - 1);
        }
    }
    let mut edges = [0_u128; MAX_PEOPLE];
    for a in 0..n {
        for b in a + 1..n {
            if knows[a] >> b & 1 == 0 || knows[b] >> a & 1 == 0 {
                edges[a] |= 1_u128 << b;
                edges[b] |= 1_u128 << a;
            }
        }
    }
    let mut remaining = (1_u128 << n) - 1;
    let mut colors = [0_u128; 2];
    let mut side = [0_u8; MAX_PEOPLE];
    let mut parts = [[0_u128; 2]; MAX_PEOPLE];
    let mut sizes = [[0_u8; 2]; MAX_PEOPLE];
    let mut components = 0;
    for seed in 0..n {
        if remaining >> seed & 1 == 0 {
            continue;
        }
        remaining &= !(1_u128 << seed);
        colors[0] |= 1_u128 << seed;
        side[seed] = 0;
        let mut queue = [0_u8; MAX_PEOPLE];
        queue[0] = seed as u8;
        let (mut head, mut tail) = (0, 1);
        while head < tail {
            let person = queue[head] as usize;
            head += 1;
            let group = side[person] as usize;
            parts[components][group] |= 1_u128 << person;
            sizes[components][group] += 1;
            if edges[person] & colors[group] != 0 {
                io::stdout().write_all(b"No solution\n").unwrap();
                return;
            }
            let mut pending = edges[person] & remaining;
            while pending != 0 {
                let neighbor = pending.trailing_zeros() as usize;
                let mask = 1_u128 << neighbor;
                pending &= !mask;
                remaining &= !mask;
                side[neighbor] = (1 - group) as u8;
                colors[1 - group] |= mask;
                queue[tail] = neighbor as u8;
                tail += 1;
            }
        }
        components += 1;
    }
    // One128-bit reachability row per component is enough to recover every orientation.
    let mut history = [0_u128; MAX_PEOPLE + 1];
    history[0] = 1;
    for component in 0..components {
        history[component + 1] = (history[component] << sizes[component][0])
            | (history[component] << sizes[component][1]);
    }
    let mut size = n / 2;
    while size > 0 && history[components] >> size & 1 == 0 {
        size -= 1;
    }
    if size == 0 {
        io::stdout().write_all(b"No solution\n").unwrap();
        return;
    }
    let mut teams = [0_u128; 2];
    for component in (0..components).rev() {
        let a = sizes[component][0] as usize;
        let pick = usize::from(size < a || history[component] >> (size - a) & 1 == 0);
        teams[0] |= parts[component][pick];
        teams[1] |= parts[component][1 - pick];
        size -= sizes[component][pick] as usize;
    }
    let mut output = [0_u8; OUTPUT_SIZE];
    let mut used = 0;
    for team in teams {
        number(&mut output, &mut used, team.count_ones() as usize);
        for person in 0..n {
            if team >> person & 1 != 0 {
                output[used] = b' ';
                used += 1;
                number(&mut output, &mut used, person + 1);
            }
        }
        output[used] = b'\n';
        used += 1;
    }
    io::stdout().write_all(&output[..used]).unwrap();
}
