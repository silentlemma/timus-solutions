use std::fmt::Write as FmtWrite;
use std::io::{self, Read};

fn better(left: usize, right: usize, values: &[i64]) -> bool {
    values[left] > values[right] || (values[left] == values[right] && left < right)
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut values: Vec<i64> = (0..n)
        .map(|_| tokens.next().unwrap().parse().unwrap())
        .collect();
    let mut following = vec![usize::MAX; n];
    let mut last = 0;
    let mut count = 1;
    for position in 1..n {
        if values[position] > values[last] {
            following[last] = position;
            last = position;
            count += 1;
        }
    }
    following[last] = n;

    // A prefix maximum uses its earliest position to preserve strict records.
    let mut tree = vec![0; n + 1];
    for (index, entry) in tree.iter_mut().enumerate().skip(1) {
        *entry = index - 1;
    }
    for index in 1..=n {
        let parent = index + (index & index.wrapping_neg());
        if parent <= n && better(tree[index], tree[parent], &values) {
            tree[parent] = tree[index];
        }
    }

    let queries: usize = tokens.next().unwrap().parse().unwrap();
    let mut output = String::new();
    for _ in 0..queries {
        let position = tokens.next().unwrap().parse::<usize>().unwrap() - 1;
        let increase: i64 = tokens.next().unwrap().parse().unwrap();
        if increase == 0 {
            writeln!(output, "{}", count).unwrap();
            continue;
        }
        values[position] += increase;
        if following[position] == usize::MAX {
            let mut previous = 0;
            let mut index = position;
            while index > 0 {
                if better(tree[index], previous, &values) {
                    previous = tree[index];
                }
                index &= index - 1;
            }
            if values[position] > values[previous] {
                following[position] = following[previous];
                following[previous] = position;
                count += 1;
            }
        }
        if following[position] != usize::MAX {
            let mut successor = following[position];
            while successor < n && values[successor] <= values[position] {
                let removed = successor;
                successor = following[removed];
                following[removed] = usize::MAX;
                count -= 1;
            }
            following[position] = successor;
        }

        let mut index = position + 1;
        while index <= n {
            if tree[index] != position {
                if !better(position, tree[index], &values) {
                    break;
                }
                tree[index] = position;
            }
            index += index & index.wrapping_neg();
        }
        writeln!(output, "{}", count).unwrap();
    }
    print!("{}", output);
}
