def main():
    print(snake_case_string)



def camel_to_snake(camel_case):
    snake_case = "".join(["_" + c.lower() if c.isupper() else c for c in camel_case]).lstrip()
    return snake_case

camel_case_string = input ("camelCase string: ")

snake_case_string = camel_to_snake(camel_case_string)

main()
