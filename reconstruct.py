import os
from src.shamir import reconstruct

def main():

    # Load shares from all .txt files in the input directory
    shares = []
    input_dir = "./reconstruct/input/"
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            file_path = os.path.join(input_dir, filename)
            share_tuple = read_tuple_from_file(file_path)
            shares.append(share_tuple)

    # Reconstruct private key from shares
    private_key = reconstruct(shares)
    private_key = private_key[2:]
    
    # Save reconstructed private key to file
    output_dir = "./reconstruct/output/"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the output directory exists
    with open(os.path.join(output_dir, "private_key.txt"), "w") as file:
        file.write(private_key)
    print("Reconstructed private key saved to file: private_key.txt")

def read_tuple_from_file(file_path):

    with open(file_path, 'r') as file:
        line = file.readline().strip()
        tuple_values = line.strip('()').split(',')
        value1 = int(tuple_values[0].strip())
        value2 = int(tuple_values[1].strip())
        
        # Return the tuple
        return (value1, value2)

if __name__ == "__main__":
    main()