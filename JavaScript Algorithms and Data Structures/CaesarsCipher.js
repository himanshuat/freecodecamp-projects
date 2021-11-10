const alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
];

function rot13(encodedStr) {
    let decodedStr = '';
    encodedStr = encodedStr.split('');
    encodedStr.forEach(char => {
        let index = alphabets.indexOf(char);
        if (index > -1) {
            if (index - 13 > -1) {
                decodedStr += alphabets[index - 13];
            } else {
                decodedStr += alphabets[26 + index - 13];
            }
        } else {
            decodedStr += char;
        }
    })
    return decodedStr;
}

rot13("SERR PBQR PNZC");