use std::io::{self, Read, Write};

const BASE: i64 = 1_000_000_000;
const DIGITS: usize = 9;

fn twice_minus(output: &mut Vec<u32>, current: &[u32], subtract: &[u32]) {
    output.clear();
    let mut carry = 0;
    for (i, &limb) in current.iter().enumerate() {
        let lower = i64::from(subtract.get(i).copied().unwrap_or(0));
        let mut value = carry + 2 * i64::from(limb) - lower;
        carry = 0;
        if value < 0 {
            value += BASE;
            carry = -1;
        } else if value >= BASE {
            value -= BASE;
            carry = 1;
        }
        output.push(value as u32);
    }
    if carry > 0 {
        output.push(carry as u32);
    }
    while output.len() > 1 && output.last() == Some(&0) {
        output.pop();
    }
}

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let k: usize = tokens.next().unwrap().parse().unwrap();

    // History index j stores the count for length j - 1.
    let needed = n - k;
    let slots = needed.min(k + 2);
    let mut history = vec![Vec::new(); slots];
    for entry in history.iter_mut().take(2) {
        entry.push(1);
    }
    let mut current = vec![1];
    let mut next = Vec::new();
    for length in 1..=n {
        let subtract: &[u32] = if length > k {
            &history[(length - k - 1) % slots]
        } else {
            &[]
        };
        twice_minus(&mut next, &current, subtract);
        std::mem::swap(&mut next, &mut current);
        if length + 1 < needed {
            history[(length + 1) % slots].clone_from(&current);
        }
    }
    let mut output = io::BufWriter::new(io::stdout().lock());
    let mut digits = current.iter().rev();
    write!(output, "{}", digits.next().unwrap())?;
    for digit in digits {
        write!(output, "{digit:0DIGITS$}")?;
    }
    writeln!(output)?;
    output.flush()
}
