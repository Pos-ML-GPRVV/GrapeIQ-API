import pandas as pd
import os
import zipfile

def dict_to_csv(data: dict, path: str = "./app/data") -> list:
    os.makedirs(path, exist_ok=True)

    csv_paths = []
    if isinstance(data, list):
        data_dict = data[0][0]
    else:
        data_dict = data
        
    for section, content in data_dict.items():
        for pad in content:
            for title, register in pad.items():
                file_name = f"{section}_{title}".replace('[', '').replace(']', '').replace(' ', '_')
                file_name = "_".join(file_name.split()) + ".csv"
                file_path = os.path.join(path, file_name)

                df = pd.DataFrame(register)
                df.columns = [col.strip() for col in df.columns]
                df.to_csv(file_path, index=False, encoding='utf-8-sig')
                csv_paths.append(file_path)
    return csv_paths


def zip_files(csv_paths: list ,year: str | int,path: str = "./app/data") -> str:
    zip_name = f"dados_vinho_{year}.zip"
    zip_path = f"{path}/{zip_name}"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in csv_paths:
            zipf.write(file)

    return zip_path