
function memoize (fn)
{
    const cache = new Map();
    
    let callCount = 0;

    return function (...args)
    {
        const argumentsAsString = args.toString();

        if ( cache.has(argumentsAsString) )
            return cache.get(argumentsAsString);
        
        const result = fn(...args);

        cache.set(argumentsAsString, result);

        callCount += 1;

        return result;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */