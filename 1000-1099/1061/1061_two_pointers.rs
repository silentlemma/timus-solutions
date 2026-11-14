use std::io::{self, BufRead};

const MAX_DIGIT: usize = 9;

fn first_cheapest(input: &mut impl BufRead, count: usize, width: usize) -> usize {
    if width > count {
        return 0;
    }
    let mut window = vec![0u8; width];
    let (mut slot, mut length, mut sum) = (0, 0, 0);
    let (mut position, mut best, mut minimum) = (0, 0, MAX_DIGIT * width + 1);
    while position < count {
        let bytes = input.fill_buf().unwrap();
        if bytes.is_empty() {
            break;
        }
        for &byte in bytes {
            match byte {
                b'*' => (slot, length, sum) = (0, 0, 0),
                b'0'..=b'9' => {
                    if length == width {
                        sum -= usize::from(window[slot]);
                    } else {
                        length += 1;
                    }
                    let digit = byte - b'0';
                    window[slot] = digit;
                    sum += usize::from(digit);
                    slot += 1;
                    if slot == width {
                        slot = 0;
                    }
                    if length == width && sum < minimum {
                        minimum = sum;
                        best = position + 2 - width;
                        if sum == 0 {
                            return best;
                        }
                    }
                }
                _ => continue,
            }
            position += 1;
            if position == count {
                return best;
            }
        }
        let consumed = bytes.len();
        input.consume(consumed);
    }
    best
}

fn main() {
    let stdin = io::stdin();
    let mut input = stdin.lock();
    let mut header = String::new();
    input.read_line(&mut header).unwrap();
    let mut numbers = header.split_ascii_whitespace();
    let count = numbers.next().unwrap().parse().unwrap();
    let width = numbers.next().unwrap().parse().unwrap();
    println!("{}", first_cheapest(&mut input, count, width));
}
