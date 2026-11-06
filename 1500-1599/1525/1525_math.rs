use std::io::{self, BufRead, Read};

const AXES: usize = 3;
const BUFFER_SIZE: usize = 4096;

fn main() -> io::Result<()> {
    let mut input = io::stdin().lock();
    let mut header = String::new();
    input.read_line(&mut header)?;
    let mut numbers = header
        .split_ascii_whitespace()
        .map(|s| s.parse::<i32>().unwrap());
    let sizes: [i32; AXES] = std::array::from_fn(|_| numbers.next().unwrap());
    let mut position = [0; AXES];
    let mut low = [0; AXES];
    let mut high = [0; AXES];
    let mut buffer = [0; BUFFER_SIZE];
    loop {
        let count = input.read(&mut buffer)?;
        if count == 0 {
            break;
        }
        for &ch in &buffer[..count] {
            let (axis, step) = match ch {
                b'l' => (0, -1),
                b'r' => (0, 1),
                b'd' => (1, -1),
                b'u' => (1, 1),
                b'b' => (2, -1),
                b'f' => (2, 1),
                _ => continue,
            };
            position[axis] += step;
            low[axis] = low[axis].min(position[axis]);
            high[axis] = high[axis].max(position[axis]);
        }
    }
    let total: i64 = (0..AXES)
        .map(|axis| i64::from((sizes[axis] - (high[axis] - low[axis])).max(1)))
        .product();
    println!("{total}");
    Ok(())
}
