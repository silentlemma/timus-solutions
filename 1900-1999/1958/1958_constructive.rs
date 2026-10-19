use std::fmt::Write;
use std::io::{self, Read};

fn flush(values: &mut [usize], operations: &mut Vec<usize>) {
    let n = values.len();
    while values[n - 1] != n {
        let value = values[n - 1];
        values.swap(n - 1, value - 1);
        operations.push(value);
    }
}

fn sort_operations(permutation: &[usize]) -> Vec<usize> {
    let mut values = permutation.to_vec();
    let n = values.len();
    let mut operations = Vec::with_capacity((n - 1) * (2 * n - 1));
    flush(&mut values, &mut operations);
    let mut unfixed = n - 1;
    while unfixed > 0 {
        while unfixed > 0 && values[unfixed - 1] == unfixed {
            unfixed -= 1;
        }
        if unfixed == 0 {
            break;
        }
        let start = values.iter().position(|&x| x == 1).unwrap();
        for position in start..n - 1 {
            values.swap(position, position + 1);
            operations.push(1);
        }
        flush(&mut values, &mut operations);
    }
    operations
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut words = input.split_whitespace();
    let n: usize = words.next().unwrap().parse().unwrap();
    let values: Vec<usize> = (0..n)
        .map(|_| words.next().unwrap().parse().unwrap())
        .collect();
    let operations = sort_operations(&values);
    let mut output = String::new();
    writeln!(output, "{}", operations.len()).unwrap();
    for value in operations {
        writeln!(output, "{}", value).unwrap();
    }
    print!("{output}");
}
