use std::io::{self, Read, Write};

const DECIMAL_BASE: usize = 10;

struct Input {
    data: Vec<u8>,
    at: usize,
}
impl Input {
    fn integer(&mut self) -> usize {
        while self.data[self.at] <= b' ' {
            self.at += 1;
        }
        let mut value = 0;
        while self.at < self.data.len() && self.data[self.at].is_ascii_digit() {
            value = value * DECIMAL_BASE + (self.data[self.at] - b'0') as usize;
            self.at += 1;
        }
        value
    }
    fn base(&mut self) -> bool {
        while self.data[self.at] <= b' ' {
            self.at += 1;
        }
        let value = self.data[self.at] == b'1';
        self.at += 1;
        value
    }
}

fn main() {
    let mut data = Vec::new();
    io::stdin().read_to_end(&mut data).unwrap();
    let mut input = Input { data, at: 0 };
    let (height, width) = (input.integer(), input.integer());
    let far = (height + width) as i32;
    let mut distances = vec![0; height * width];
    let mut last = vec![-far; width];
    for row in 0..height {
        for column in 0..width {
            if input.base() {
                last[column] = row as i32;
            }
            distances[row * width + column] = row as i32 - last[column];
        }
    }
    let mut following = vec![height as i32 + far; width];
    for row in (0..height).rev() {
        for column in 0..width {
            let at = row * width + column;
            let value = distances[at];
            if value == 0 {
                following[column] = row as i32;
            } else if following[column] - (row as i32) < value {
                distances[at] = following[column] - row as i32;
            }
        }
    }
    let mut costs = vec![0; width];
    let mut intercepts = vec![0; width];
    let mut sites = vec![0; width];
    let mut starts = vec![0; width];
    let stdout = io::stdout();
    let mut out = io::BufWriter::new(stdout.lock());
    for row in 0..height {
        let mut used = 0;
        for q in 0..width {
            let vertical = distances[row * width + q];
            if vertical >= far {
                continue;
            }
            costs[q] = vertical * vertical;
            intercepts[q] = costs[q] + (q * q) as i32;
            let mut first = 0;
            while used > 0 {
                let p = sites[used - 1];
                let numerator: i32 = intercepts[q] - intercepts[p];
                let denominator = 2 * (q - p) as i32;
                first = -(-numerator).div_euclid(denominator);
                if first > starts[used - 1] {
                    break;
                }
                used -= 1;
            }
            if used == 0 {
                first = 0;
            }
            sites[used] = q;
            starts[used] = first;
            used += 1;
        }
        let mut current = 0;
        for x in 0..width {
            while current + 1 < used && starts[current + 1] <= x as i32 {
                current += 1;
            }
            let p = sites[current];
            let delta = x as i32 - p as i32;
            if x != 0 {
                write!(out, " ").unwrap();
            }
            write!(out, "{}", delta * delta + costs[p]).unwrap();
        }
        writeln!(out).unwrap();
    }
}
