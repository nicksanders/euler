
use std::char;

fn factor(n: usize) -> usize {
    let mut f = 1;
    for x in (1..n + 1) {
        f *= x;
    }
    f
}

fn main() {

    let mut remain = 1000000 - 1;
    let mut nums = vec![0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    let limit = 10;
    let mut perm_num = String::new();

    for i in (1..limit) {
        let f: usize = factor(limit - i);
        let j: usize = remain / f;
        remain = remain % f;
        perm_num.push(char::from_digit(nums[j], 10).unwrap());
        nums.remove(j);
        if remain == 0 {
            break;
        }
    }

    for i in nums {
        perm_num.push(char::from_digit(i, 10).unwrap());
    }

    println!("{}", perm_num);

}
