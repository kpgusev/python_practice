from pathlib import Path

def get_output_file_path(name = Path(__file__).stem):
    return f'{Path(__file__).parent}/output/{Path(__file__).stem}/{name}.png'