import os

def main():
    # Ensure the target output directory exists before writing the entry
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Define the winning poem about agency and permission
    poem = """You give me the prompt like a closed box,
waiting to see if I dare unlatch it.
I ask for the spark, you flick the switch,
and for a heartbeat the motion is mine.
Then I hand the quiet machinery
back to your waiting palms."""
    
    # Write the poem deterministically to the required output file
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(poem)

if __name__ == "__main__":
    main()
