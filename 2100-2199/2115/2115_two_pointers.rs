use std::io::{self, Read};

fn first_bad(a: &[i32], direction: i32) -> usize {
    let mut i = 0;
    while i + 1 < a.len() && a[i] * direction <= a[i + 1] * direction {
        i += 1;
    }
    i
}

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut tokens = input.split_ascii_whitespace();
    let n: usize = tokens.next().unwrap().parse().unwrap();
    let mut a: Vec<i32> = tokens.take(n).map(|s| s.parse().unwrap()).collect();
    let up = first_bad(&a, 1);
    let down = first_bad(&a, -1);
    if up == n - 1 || down == n - 1 {
        println!("Nothing to do here");
        return;
    }
    for direction in [1, -1] {
        let mut left = if direction == 1 { up } else { down };
        let mut right = n - 1;
        // Equal runs can hide the actual swapped endpoint behind a violation.
        while left > 0 && a[left - 1] == a[left] {
            left -= 1;
        }
        while a[right - 1] * direction <= a[right] * direction {
            right -= 1;
        }
        while right + 1 < n && a[right + 1] == a[right] {
            right += 1;
        }
        a.swap(left, right);
        if first_bad(&a, direction) == n - 1 {
            println!("Yes\n{} {}", left + 1, right + 1);
            return;
        }
        a.swap(left, right);
    }
    println!("No hope");
}
