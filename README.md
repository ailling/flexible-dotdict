# Flexible dotted dictionary

A dictionary that allows access to keys via the dot operator, so that `instance.value` is equivalent to `instance['value']`.

## Examples

    from dotdict import DotDict
    
    # create from a regular dictionary
    obj = DotDict({
        'foo': 'bar',
        'value': 15,
        'sub': {
            'bam': 'baz'
        }
    })
    
    # or from named arguments
    obj = DotDict(foo='bar', value=15)
    
    # also works with dictionaries as arguments
    obj = DotDict(foo='bar', value=15, sub={'bam': 'baz'})

    # and now attributes can be access via dot operator:
    print(obj.foo) # prints bar
    print(obj.sub) # prints {'bam': 'baz'}
    print(obj.sub.bam) # prints baz

## Installation

Install with pip

    pip install flexible-dotdict

## Check version

    import dotdict
    print(dotdict.VERSION)

## License

Covered under the MIT license; see LICENSE for details.
