
use std::collections::HashSet;

mod common;
use common::split_num;

fn main() {

    let mut result: HashSet<usize> = HashSet::new();

    for a in (2..100) {
        let b_start = if a > 9 { 123 } else { 1234 };
        let b_end = 10000;
        for b in (b_start..b_end) {
            let c = a * b;
            let mut nums: Vec<_> = split_num(a).iter().chain(split_num(b).iter()).chain(split_num(c).iter()).cloned().collect();
            if nums.len() == 9 {
                nums.sort();
                if nums == [1, 2, 3, 4, 5, 6, 7, 8, 9] {
                    result.insert(c);
                }
            }
        }
    }

    println!("{}", result.iter().fold(0, |acc, x| acc + x));

}
