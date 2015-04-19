
extern crate num;

fn split_num(mut n: usize) -> Vec<usize> {
    let mut nums = vec![];
    while n > 0 {
        let x = n % 10;
        n = (n - x) / 10;
        nums.push(x);
    }
    nums
}

fn main() {

    let mut result = 0;

    for i in (2..1000000) {
        let res = split_num(i).iter().map(|&x| num::pow(x, 5)).fold(0, |acc, x| acc + x);
        if res == i {
            result += i;
        }
    }

    println!("{:?}", result);

}
