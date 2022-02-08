function checkCashRegister(price, cash, cid) {
    let unitValues = [0.01, 0.05, 0.1, 0.25, 1, 5, 10, 20, 100];
    let change = [];
    let cashData = {};
    let amountInDrawer = 0;
    let changeAmount = cash - price;

    for (let i = 0; i < cid.length; ++i) {
        amountInDrawer += cid[i][1];
    }

    if (changeAmount === amountInDrawer) {
        return {status: "CLOSED", change: cid};
    }
    else if (changeAmount > amountInDrawer) {
        return {status: "INSUFFICIENT_FUNDS", change: []};
    }

    for (let i = 0; i < cid.length; ++i) {
        cashData[cid[i][0]] = {
            name: cid[i][0],
            value: unitValues[i],
            count: Math.floor(cid[i][1] / unitValues[i])
        }
    }
    
    for (let i = cid.length - 1; i >= 0 ; --i) {
        if (changeAmount > unitValues[i]) {
            let possibleCountOfUnit = Math.floor(changeAmount / unitValues[i]);
            let unitAmoutToReturn = Math.min(possibleCountOfUnit, cashData[cid[i][0]].count) * unitValues[i];
            change.push([cashData[cid[i][0]].name, unitAmoutToReturn]);
            // Round the value to two decimal places
            changeAmount = Math.round((changeAmount - unitAmoutToReturn) * 100) / 100;
        }

        if (changeAmount === 0) {
            break;
        }
    }

    if (changeAmount > 0) {
        return {status: "INSUFFICIENT_FUNDS", change: []};
    }

    return {status: "OPEN", change: change};
}