
extern crate num;

use num::bigint::ToBigUint;

fn main() {

    let mut res = 2.to_biguint().unwrap();
    res = num::pow(res, 1000);

    println!("{}", res.to_string().chars().map(|x| x.to_string().parse::<usize>().unwrap()).fold(0, |acc, x| acc + x));

}
