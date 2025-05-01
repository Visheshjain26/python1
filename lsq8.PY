def queue_menu():
    queue = []
    while True:
        print("\nMenu:\n1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            val = input("Enter value to enqueue: ")
            queue.append(val)
            print("Queue after enqueue:", queue)
        elif choice == 2:
            if queue:
                print("Dequeued element:", queue.pop(0))
            else:
                print("Queue is empty")
        elif choice == 3:
            print("Current Queue:", queue)
        elif choice == 4:
            break
        else:
            print("Invalid choice")