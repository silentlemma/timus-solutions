use std::io::{self, BufRead, BufWriter, Write};

fn main() -> io::Result<()> {
    let mut input = String::new();
    io::stdin().lock().read_line(&mut input)?;
    let n: i32 = input.trim().parse().unwrap();
    let mut out = BufWriter::new(io::stdout().lock());
    writeln!(out, "{}", n * (n + 2))?;

    let tokens: Vec<String> = (0..=2 * n).map(|i| format!(" {i}")).collect();
    let mut hole = n;
    let mut direction = 1;
    for run in 0..=2 * n {
        let length = (run + 1).min(n).min(2 * n - run + 1);
        // Rising runs slide last and falling runs slide first.
        let slide = if run < n {
            length - 1
        } else if run > n {
            0
        } else {
            -1
        };
        for i in 0..length {
            let distance = if i == slide { 1 } else { 2 };
            hole += distance * direction;
            let skip = usize::from(run == 0);
            out.write_all(&tokens[hole as usize].as_bytes()[skip..])?;
        }
        direction = -direction;
    }
    writeln!(out)?;
    out.flush()
}
