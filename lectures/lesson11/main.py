import datetime


def run_process(argument_one: str, **kwargs) -> None:
    run_date = kwargs.get("run_date") if kwargs.get("run_date") else datetime.datetime.now()
    print(kwargs, run_date)
    
my_dictionary1 = {"a": 1}
my_dictionary2 = {"b": 2}
my_dictionary3 = {"c": 3}


run_process("1", another_argument = 5)