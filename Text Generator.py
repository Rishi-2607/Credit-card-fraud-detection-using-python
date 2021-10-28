call the function generate()

 pass in the arguments, they are: [
        'length_minimal', 'length_maximal', 'int_min_length',
        'int_max_length'
    ], they are optional and the default values will be given to them. So the
        output will be like

   generate_code_simple(length_minimal=int, length_maximal=int,
                        int_min_length=int, int_max_length=int).
                         then leave the rest to the packge to generate the type of code for you

 then make a variable like the example
   `code = generate_code_simple()` | don't add the the symbol `|` just write the
   what is inside the variables backticks.

 then at runtime the generated code will be run
 code = generate()
print(f"Generated code is -> {code}")
