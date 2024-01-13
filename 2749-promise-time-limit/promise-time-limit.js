/**
 * @param {Function} fn
 * @param {number} t
 * @return {Function}
 */
var timeLimit = function (fn, t) {
    return function (...args) {
        return new Promise((resolve, reject) => {
            const originalPromise = fn(...args)
            const timeoutPromise = new Promise((_resolve, _reject) => {
                setTimeout(() => {_reject("Time Limit Exceeded")},t)
            })

            Promise.race([originalPromise, timeoutPromise])
            .then(resolve)
            .catch(reject)
        })
    }
};

/**
 * const limited = timeLimit((t) => new Promise(res => setTimeout(res, t)), 100);
 * limited(150).catch(console.log) // "Time Limit Exceeded" at t=100ms
 */