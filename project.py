import argparse
import json

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Ścieżka do pliku wejściowego')
    parser.add_argument('output_file', help='Ścieżka do pliku wyjściowego')
    args = parser.parse_args()
    return args.input_file, args.output_file

input_file, output_file = parse_arguments()

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
            return data
        except json.JSONDecodeError as e:
            print(f"Błąd dekodowania pliku JSON: {e}")
            return None

json_data = read_json_file(input_file)
if json_data:
    print("Dane z pliku JSON:")
    print(json_data)