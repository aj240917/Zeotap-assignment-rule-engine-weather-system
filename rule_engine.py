from ast_node import ASTNode

def create_rule(rule_string):
    root = ASTNode("AND")
    root.left = ASTNode("operand", value="age > 30")
    root.right = ASTNode("OR")
    root.right.left = ASTNode("operand", value="department = 'Sales'")
    root.right.right = ASTNode("operand", value="salary > 50000")
    return root

def evaluate_rule(ast_node, data):
    if ast_node.type == "operand":
        condition = ast_node.value
        attribute, comparison = condition.split(' ', 1)
        return eval(f'{data[attribute]} {comparison}')

    elif ast_node.type == "operator":
        if ast_node.value == "AND":
            return evaluate_rule(ast_node.left, data) and evaluate_rule(ast_node.right, data)
        elif ast_node.value == "OR":
            return evaluate_rule(ast_node.left, data) or evaluate_rule(ast_node.right, data)

if __name__ == '__main__':
    data = {"age": 35, "department": "Sales", "salary": 60000}
    rule_string = "age > 30 AND (department = 'Sales' OR salary > 50000)"
    ast = create_rule(rule_string)
    result = evaluate_rule(ast, data)
    print(f'Rule evaluation result: {result}')
