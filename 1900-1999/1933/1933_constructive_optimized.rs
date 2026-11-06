use std::io::{self, Read, Write};

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input)?;
    let pairs: usize = input.trim().parse().unwrap();
    let size = 2 * pairs + 1;
    let mut output = io::BufWriter::new(io::stdout().lock());
    for row in 0..size {
        let mut round = if row == 0 { size } else { row };
        for column in 0..size {
            if column != 0 {
                output.write_all(b" ")?;
            }
            let value = if column == row { 0 } else { round };
            write!(output, "{value}")?;
            round = if round == size { 1 } else { round + 1 };
        }
        writeln!(output)?;
    }
    output.flush()
}
