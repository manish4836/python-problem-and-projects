def outer_funtion(msg):
    def inner_function():  # this is the closure function
        print(msg)
    inner_function()

outer_funtion("Hello World!")

#inner_function()  # ye error dega kyuki inner function sirf outer function ke andar hi call ho sakta hai