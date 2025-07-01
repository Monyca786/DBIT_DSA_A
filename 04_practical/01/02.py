stack = [10]  # Make sure the stack is not empty
print(f" Initial stack: {stack}")

stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)
stack.append(60)

print(f" After pushing: {stack}")

popped = stack.pop()
print(f" Popped item: {popped}")
print(f" Stack after pop: {stack}")

if stack:
    print(f" Top of stack (peek): {stack[-1]}")
else:
    print(f" Stack is empty")

print(f" Is stack empty? {len(stack) == 0}")  # This is now false

print(f" Stack contents (top to bottom):")
for item in reversed(stack):
    print(f" {item}")