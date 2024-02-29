import random

class App:
    @staticmethod
    def start() -> None:
        print("Hello World. Type 'exit' to exit.")
        
        while True:
            user_input = input(">>> ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            elif user_input.lower() == "/random":
                print(random.randint(1, 100))
            else:
                # Here, you could add additional commands and their handling
                print("Unknown command. Type 'exit' to exit.")

        