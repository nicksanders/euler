
use std::collections::HashSet;

mod common;
use common::{split_num, gcd};

fn main() {

    let mut numerator = 1;
    let mut denominator = 1;

    for a in (10..100) {
        for b in (a + 1..100) {
            if b % 10 == 0 || a == b {
                continue
            }
            let c = a / b;
            let a2 = split_num(a);
            let b2 = split_num(b);

            if a2.iter().any(|x| b2.binary_search(x) == Ok()) && !a2.iter().all(|x| b2.binary_search(x) == Ok()) {
                let d = b2.remove(0);
                if d == a[0] {

                } else if

                }
                match b2.binary_search(a2[0]) {
                    Ok(i) =>
                    Err(_) => match b2.binary_search(a2[1]) {
                        Ok(i) =>
                        Err(_) => panic!("Argh")
                    }
                }
                } else {
                    a2[1]
                };
                a2.remove(x);
                b2.remove(x);
            }
            if any(i in b2 for i in a2) and not all(i in b2 for i in a2):
                if a2[0] in b2:
                    x = a2[0]
                else:
                    x = a2[1]
                a2.remove(x)
                b2.remove(x)
                if b2[0] > 0 and a2[0] / b2[0] == c:
                    numerator *= a2[0]
                    denominator *= b2[0]
        }
    }

    println!("{}", denominator / gcd(numerator, denominator));

}
