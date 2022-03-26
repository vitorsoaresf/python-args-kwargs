import functools
def sum_numbers(*args):
    return functools.reduce(lambda a,b: a+b, args)

def get_multiplied_amount(multiplier, *args):
    return multiplier * functools.reduce(lambda a,b: a+b, args)


def word_concatenator(*args):
    return " ".join(args)


def inverted_word_factory(*args):
    result = [x[::-1] for x in args]
    result.reverse()
    return " ".join(result)


def dictionary_separator(**kwargs):    
    return (list(kwargs.keys()),list(kwargs.values()))


def dictionary_creator(*args, **kwargs):
    result = {}
    if(len(args) < len(kwargs)):
        return None
    
    for element in zip(args,kwargs.values()):
        result[element[0]] = element[1]
    
    return result

def purchase_logger(**kwargs):
    return f"Product {kwargs['name']} costs {kwargs['price']} and was bought {kwargs['quantity']}"


def world_cup_logger(country, *args):
    list_years = [str(year) for year in args]
    list_years = ', '.join(sorted(list_years))

    last_position = list_years.rindex(',')
    
    list_years = list_years[0:last_position] + " e" + list_years[last_position+1:]
    return f"{country} - {list_years}"

