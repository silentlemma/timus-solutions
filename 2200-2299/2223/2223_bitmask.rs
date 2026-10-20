use std::io::{self, Read};

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let x = tokens.next().unwrap().as_bytes();
    let y = tokens.next().unwrap().as_bytes();
    let size = x.len().max(y.len());
    let x_padding = size - x.len();
    let y_padding = size - y.len();

    let mut propagating = 0;
    let mut longest = 0;
    for i in 0..size {
        let a = if i < x_padding {
            b'0'
        } else {
            x[i - x_padding]
        };
        let b = if i < y_padding {
            b'0'
        } else {
            y[i - y_padding]
        };
        if a != b {
            propagating += 1;
        } else {
            // A common one starts a carry through the differing bits above it.
            if a == b'1' {
                longest = longest.max(propagating + 1);
            }
            propagating = 0;
        }
    }
    // Include the initial call and the final call with a zero second argument.
    println!("{}", longest + 2);
}
