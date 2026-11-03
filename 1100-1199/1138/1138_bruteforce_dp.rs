use std::io::{self, Read};

const PERCENT: usize = 100;

fn main() {
    let mut input = String::new();
    io::stdin().read_to_string(&mut input).unwrap();
    let mut numbers = input
        .split_ascii_whitespace()
        .map(|word| word.parse::<usize>().unwrap());
    let (n, start) = (numbers.next().unwrap(), numbers.next().unwrap());
    if start > n {
        println!("0");
        return;
    }
    let mut jobs = vec![0; n + 1];
    jobs[start] = 1;
    let mut answer = 1;
    // Increasing salaries form a DAG. Divisibility tests whole percentages
    // exactly; no floating-point values or gcd successor formula are needed.
    for salary in start..=n {
        if jobs[salary] == 0 {
            continue;
        }
        answer = answer.max(jobs[salary]);
        for following in salary + 1..=n {
            if PERCENT * following % salary == 0 {
                jobs[following] = jobs[following].max(jobs[salary] + 1);
            }
        }
    }
    println!("{}", answer);
}
