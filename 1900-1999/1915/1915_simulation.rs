use std::io::{self, Read, Write};

fn popped_coins(operations: &[i32]) -> Vec<i32> {
    let mut remaining = operations
        .iter()
        .filter(|&&operation| operation == -1)
        .count();
    let mut answer = Vec::with_capacity(remaining);
    if remaining == 0 {
        return answer;
    }
    let capacity = remaining;
    let mut coins = vec![0; capacity];
    let mut bottom = 0;
    let mut size = 0;
    for &operation in operations {
        if remaining == 0 {
            break;
        }
        if operation > 0 {
            if size == remaining {
                bottom = (bottom + 1) % capacity;
                size -= 1;
            }
            coins[(bottom + size) % capacity] = operation;
            size += 1;
        } else if operation == -1 {
            remaining -= 1;
            size -= 1;
            answer.push(coins[(bottom + size) % capacity]);
        } else {
            let extra = size.min(remaining - size);
            let new_bottom = (bottom + capacity - extra) % capacity;
            let mut source = (bottom + size - extra) % capacity;
            let mut destination = new_bottom;
            for _ in 0..extra {
                coins[destination] = coins[source];
                source += 1;
                destination += 1;
                if source == capacity {
                    source = 0;
                }
                if destination == capacity {
                    destination = 0;
                }
            }
            bottom = new_bottom;
            size += extra;
        }
    }
    answer
}

fn main() {
    let mut text = String::new();
    io::stdin().read_to_string(&mut text).unwrap();
    let mut tokens = text.split_whitespace();
    let count = tokens.next().unwrap().parse::<usize>().unwrap();
    let operations: Vec<i32> = (0..count)
        .map(|_| tokens.next().unwrap().parse::<i32>().unwrap())
        .collect();
    let stdout = io::stdout();
    let mut output = io::BufWriter::new(stdout.lock());
    for coin in popped_coins(&operations) {
        writeln!(output, "{}", coin).unwrap();
    }
}
