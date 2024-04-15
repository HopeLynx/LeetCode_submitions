/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    return args.length
};

/**
 * argumentsLength(1, 2, 3); // 3
 */

// Runtime: 46 ms Beats 84.66% of users with JavaScript
// Memory Usage: 48.44 MB Beats 84.61% of users with JavaScript