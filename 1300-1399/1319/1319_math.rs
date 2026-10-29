use std::io::{self, BufWriter, Read, Write};

// no table: each number is computed from the length of its diagonal,
// counted from the start above the main diagonal and from the end below it
fn main() {
    const OUTPUT_BUFFER_SIZE: usize = 1024;
    let mut n = 0;
    // n is parsed by hand from the bytes of the input
    for byte in io::stdin().lock().bytes() {
        match byte.unwrap() {
            c @ b'0'..=b'9' => n = n * 10 + i32::from(c - b'0'),
            _ if n != 0 => break,
            _ => {}
        }
    }
    let stdout = io::stdout();
    let mut output = BufWriter::with_capacity(OUTPUT_BUFFER_SIZE, stdout.lock());
    for row in 0..n {
        for col in 0..n {
            // the diagonal of this cell has n - |col - row| cells
            let length = n - (col - row).abs();
            let value = if col >= row {
                length * (length - 1) / 2 + row + 1
            } else {
                n * n - length * (length + 1) / 2 + col + 1
            };
            if col > 0 {
                write!(output, " ").unwrap();
            }
            write!(output, "{}", value).unwrap();
        }
        writeln!(output).unwrap();
    }
}
