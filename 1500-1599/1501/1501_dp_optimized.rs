use std::io::{self, Read};

fn balance(pile: &[u8]) -> Vec<i16> {
    let mut result = Vec::with_capacity(pile.len() + 1);
    result.push(0);
    for &card in pile {
        result.push(result[result.len() - 1] + if card == b'1' { 1 } else { -1 });
    }
    result
}

fn frontier(
    first: &[i16],
    second: &[i16],
    row: &mut [u8],
    a0: usize,
    a1: usize,
    b0: usize,
    b1: usize,
    reverse: bool,
) -> bool {
    let height = if reverse { a0 - a1 } else { a1 - a0 };
    let width = if reverse { b0 - b1 } else { b1 - b0 };
    row[..=width].fill(0);
    row[0] = 1;
    for offset in 0..=height {
        let i = if reverse { a0 - offset } else { a0 + offset };
        let mut any = false;
        for t in 0..=width {
            let j = if reverse { b0 - t } else { b0 + t };
            let sum = first[i] + second[j];
            row[t] =
                u8::from((-1..=1).contains(&sum) && (row[t] != 0 || (t > 0 && row[t - 1] != 0)));
            any |= row[t] != 0;
        }
        if !any {
            return false;
        }
    }
    true
}

struct Solver {
    first: Vec<i16>,
    second: Vec<i16>,
    forward: Vec<u8>,
    backward: Vec<u8>,
    moves: Vec<u8>,
}
impl Solver {
    fn append(&mut self, move_byte: u8, count: usize) {
        self.moves.extend(std::iter::repeat(move_byte).take(count));
    }
    fn recover(&mut self, a0: usize, a1: usize, b0: usize, b1: usize) -> bool {
        if a0 == a1 || b0 == b1 {
            for i in a0..=a1 {
                for j in b0..=b1 {
                    if (self.first[i] + self.second[j]).abs() > 1 {
                        return false;
                    }
                }
            }
            if a0 == a1 {
                self.append(b'2', b1 - b0);
            } else {
                self.append(b'1', a1 - a0);
            }
            return true;
        }
        let middle = (a0 + a1) / 2;
        let single = a1 - a0 == 1;
        let (upper, lower) = if single { (a0, a1) } else { (middle, middle) };
        if !frontier(
            &self.first,
            &self.second,
            &mut self.forward,
            a0,
            upper,
            b0,
            b1,
            false,
        ) || !frontier(
            &self.first,
            &self.second,
            &mut self.backward,
            a1,
            lower,
            b1,
            b0,
            true,
        ) {
            return false;
        }
        let width = b1 - b0;
        let split =
            match (0..=width).find(|&t| self.forward[t] != 0 && self.backward[width - t] != 0) {
                Some(t) => t,
                None => return false,
            };
        // A single first-pile card joins two one-row paths across an edge.
        if single {
            self.append(b'2', split);
            self.append(b'1', 1);
            self.append(b'2', width - split);
            return true;
        }
        // Child calls overwrite shared buffers; this frame only keeps the split.
        self.recover(a0, middle, b0, b0 + split) && self.recover(middle, a1, b0 + split, b1)
    }
}
fn main() {
    let mut raw = String::new();
    io::stdin().read_to_string(&mut raw).unwrap();
    let mut tokens = raw.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let first = balance(tokens.next().unwrap().as_bytes());
    let second = balance(tokens.next().unwrap().as_bytes());
    let mut solver = Solver {
        first,
        second,
        forward: vec![0; n + 1],
        backward: vec![0; n + 1],
        moves: Vec::with_capacity(2 * n),
    };
    if solver.recover(0, n, 0, n) {
        println!("{}", String::from_utf8(solver.moves).unwrap());
    } else {
        println!("Impossible");
    }
}
