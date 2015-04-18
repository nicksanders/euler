
extern crate num;

use std::iter;
use num::bigint::{BigUint, ToBigUint};

fn main() {

    let limit_len = 1000;

    let mut a = 1.to_biguint().unwrap();
    let mut b = 0.to_biguint().unwrap();
    let mut n = 1;

    let limit = iter::repeat("9").take(limit_len - 1).collect::<String>().parse::<BigUint>().unwrap();

    while a <= limit {
        let tmp = a.clone();
        a = a + b;
        b = tmp;
        n += 1;
    }

    println!("{}", n);

}
