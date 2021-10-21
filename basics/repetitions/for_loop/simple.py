def run():
    print("How many mountains should I display?")
    mountains = int(input())
    print("...Displaying")
    for _ in range(mountains):
        print("""
                 __
                /  \\_  
               /^    \\
              /  ^    \\_
            _/ ^ ^     ^\\
           /  ^     ^    \\
    
        """)
if __name__ == "__main__":
    run()