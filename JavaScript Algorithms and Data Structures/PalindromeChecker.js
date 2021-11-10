function palindrome(str) {
    str = str.replace(/\W/g, '').toLowerCase();
    str = str.replaceAll('-', '').replaceAll('_', '');
    let rev = str.split('').reverse();
    rev = rev.join('');
    return str === rev ? true : false;
}

palindrome("eye");