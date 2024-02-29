import printing_functions

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print("Before starting, print both lists")
print("unprinted_designs:", unprinted_designs)
print("completed_models:",completed_models,"\n")

printing_functions.print_models(unprinted_designs, completed_models)
printing_functions.show_completed_models(completed_models)

print("\nAfter finishing, print both lists")
print("unprinted_designs:", unprinted_designs)
print("completed_models:",completed_models)
