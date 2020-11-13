// isObj and has keys
let isObj = (o: any) => {
    return (o && typeof o === 'object' && !Array.isArray(o) && Object.keys(o).length !== 0);
};

let isEmptyObjectOrArray = (oa: any) => {
    return (
        oa === undefined ||
        oa === null || oa === '' ||
        (Array.isArray(oa) && oa.length === 0) ||
        (typeof oa === 'object' && !Array.isArray(oa) && Object.keys(oa).length === 0)
    );
};

// is array with stuff inside
let isArray = (a: any) => {
    return Array.isArray(a) && a.length > 0;
};

let removeEmpty = (obj: any) => {
    Object.keys(obj).forEach(key => {
        // look at objects
        // If object then go deep in the keys
        if (isObj(obj[key])) {
            removeEmpty(obj[key]);
            if (isEmptyObjectOrArray(obj[key])) {
                delete obj[key];
            }
        // If after deleting keys the object is empty delete it as well
        } else if (isEmptyObjectOrArray(obj[key])) {
            delete obj[key];
        // If an array
        } else if (isArray(obj[key])) {
            let i = 0;
            let N = obj[key].length;
            while (i < N) {
                // Go deep in the potential objects in the array
                removeEmpty(obj[key]);

                // If you find empty stuff then remove the item from the array 
                // which shifts the array so don't increase the index, but decrease the length
                if (isEmptyObjectOrArray(obj[key][i])) {
                    obj[key].splice(i, 1);
                    N--;
                // Otherwise increase the index go to the next index
                } else {
                    i++;
                }
            }

            // if after done with the array it's empty then delete
            if (isEmptyObjectOrArray(obj[key])) {
                delete obj[key];
            }
        }
    });
    return obj;
};
