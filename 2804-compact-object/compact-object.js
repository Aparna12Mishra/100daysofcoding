// takes an object and returns only obj with keys having truthy values only
function compactObject(param) {
    if (param === null) return null;

    // if the param is an array
    if (Array.isArray(param)) {
        // create a newArray
        const compactedArr = [];

        // loop through the array param
        for (let i = 0; i < param.length; i++) {
            // isolate the value at each index position
            const currParam = param[i];

            // check if currParam is null, array, object, or not by running it through this function again
            // accounts for nested objects
            const subResult = compactObject(currParam);

            // if subResult is true, add it to the compactedArr
            if (subResult) {
                compactedArr.push(subResult);
            }
        }

        return compactedArr;
    }

    // at this point, function has checked if param is null or an array. If it's neither and it's also NOT an object
    if (typeof param !== 'object') {
        // then the param itself is returned wherever compactObject(x) has been called
        return param;
    }


    // create a new object
    const compactObj = {};

    // loop through keys in object
    for (const key in param) {
        const currParam = param[key];

        // check if currParam is null, array, object, or not
        const subResult = compactObject(currParam);

        // if subResult is true in this loop
        if (subResult) {
            // add compactObj {"[key]" : "subResult"} 
            compactObj[key] = subResult;
        }
    }

    return compactObj;

}