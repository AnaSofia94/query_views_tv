import pandas as pd
import tempfile
import os
from globals import data_frame_manager


async def process_uploaded_file(file):
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        file_path = tmp_file.name
        tmp_file.write(await file.read())
    file_extension = file.filename.split('.')[-1].lower()
    column_names = ["content_id", "actual_label", "predicted_label", "feature_vector", "tvshow"]
    if file_extension == 'csv':
        df = pd.read_csv(file_path, delimiter=";", names=column_names, header=0)
    elif file_extension == 'json':
        df = pd.read_json(file_path)
        df.columns = column_names
    else:
        os.remove(file_path)
        raise ValueError(f"Unsupported file format: {file_extension}")
    data_frame_manager.set_dataframe(df)
    os.remove(file_path)