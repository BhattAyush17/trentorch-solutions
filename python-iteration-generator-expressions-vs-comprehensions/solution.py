def eager_double(values) -> list:
    """
    Return a concrete list containing every value in `values`
    multiplied by 2.
    """
    
    return [value *2 for  value in values]


def lazy_double(values):
    """
    Return a generator expression that lazily produces values * 2.
    """
  
    return (values * 2 for values in values)


def lazy_positive(values):
    """
    Return a generator expression that lazily produces only
    positive values.
    """
    return (value for value in values if value > 0)
    return (vlaue for value in values if value>0)
