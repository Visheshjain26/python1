def stack_menu():
    stack = []
    while True:
        print("\nMenu:\n1. Push\n2. Pop\n3. Display\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            val = input("Enter value to push: ")
            stack.append(val)
            print("Stack after push:", stack)
        elif choice == 2:
            if stack:
                print("Popped element:", stack.pop())
            else:
                print("Stack is empty")
        elif choice == 3:
            print("Current Stack:", stack)
        elif choice == 4:
            break
        else:
            print("Invalid choice")