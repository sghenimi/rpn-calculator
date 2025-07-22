from src.rpn_calculator.services.operations import Operation, Addition, Substraction, Multiplication, Division


def get_operation(operation: str) -> Operation:
    if operation == '+':
        return Addition()
    elif operation == '-':
        return Substraction()
    elif operation == '*':
        return Multiplication()
    elif operation == '/':
        return Division()