import pickle
import pprint
import sys

def pkl_to_text_pprint(pkl_file_path, output_text_path):
    """
    Loads a .pkl file and saves its content as a human-readable text file 
    using pprint.
    """
    try:
        # Load the data from the .pkl file in read binary mode ('rb')
        with open(pkl_file_path, 'rb') as f:
            data = pickle.load(f)
        
        # Save the loaded data to a text file using pretty print
        with open(output_text_path, 'w') as f_out:
            pprint.pprint(data, stream=f_out)
        
        print(f"Successfully converted '{pkl_file_path}' to '{output_text_path}' using pprint.")

    except Exception as e:
        print(f"An error occurred: {e}")
        print("Ensure the input file path is correct and the pickle file is not corrupt.")

if __name__ == "__main__":
    # Replace 'input_file.pkl' with the path to your .pkl file
    # Replace 'output_file.txt' with the desired output text file path
    pkl_to_text_pprint('cid_acc_maps.pkl', 'cid_acc_maps.txt')
    pkl_to_text_pprint('len-seq.pkl', 'len-seq.txt')
    pkl_to_text_pprint('mapping_ids.pkl', 'mapping_ids.txt')
