

# String has easy built in methods for string manipulation
# .split( delimiter ) will split the string into a list of strings, splitting based on delimiter used
# '<joiner>'.join( strs ) take in iterable of strings, and join them with joiner string

def split_and_join(line):
    return '-'.join( line.split() )