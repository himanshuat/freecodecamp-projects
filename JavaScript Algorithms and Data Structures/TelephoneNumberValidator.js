function telephoneCheck(str) {
    let pattern = /[1]?[\s]?([\d]{3}|\([\d]{3}\))[\s-]?([\d]{3}|\([\d]{3}\))[\s-]?([\d]{4}|\([\d]{4}\))/;
    let result = str.match(pattern);
    return result === null ? false: result[0] === str;
}

telephoneCheck("123**&!!asdf#");