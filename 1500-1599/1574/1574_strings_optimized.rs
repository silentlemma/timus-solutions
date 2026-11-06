use std::io::{self, BufRead};

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let (mut balance, mut lowest, mut count) = (0, 0, 0);
    loop {
        let block = input.fill_buf()?;
        if block.is_empty() {
            break;
        }
        for &byte in block {
            match byte {
                b'(' => balance += 1,
                b')' => balance -= 1,
                _ => continue,
            }
            if balance < lowest {
                lowest = balance;
                count = 1;
            } else if balance == lowest {
                count += 1;
            }
        }
        let consumed = block.len();
        input.consume(consumed);
    }
    println!("{}", if balance == 0 { count } else { 0 });
    Ok(())
}
