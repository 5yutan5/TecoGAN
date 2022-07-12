import logging
from pathlib import Path

import cv2
import numpy as np
import pandas as pd


def create_logger(logger_name: str) -> logging.Logger:
    logger = logging.getLogger(logger_name)
    logger.propagate = False
    ch = logging.StreamHandler()
    ch.setFormatter(logging.Formatter("[%(name)s] [%(levelname)s] %(message)s"))
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    return logger


logger = create_logger(__name__)


def csv_to_img(csv_path: Path, output_path: Path, threshold: int = 255) -> None:
    csv = pd.read_csv(csv_path, sep=",")
    csv = csv.iloc[:, 1:].iloc[:, :-1]
    csv = csv.values

    rows, _ = csv.shape

    # 保存フォルダ作成
    if not output_path.exists():
        logger.info("Create output directory.")
        output_path.mkdir()
    else:
        logger.info("Output directory already exists.")

    for i in range(rows):
        img = csv[i].reshape((48, 48)) * 255 // threshold
        img = img.astype(np.uint8)
        heatmap = cv2.applyColorMap(img, cv2.COLORMAP_JET)

        image_file_name = output_path / f"output_{str(i).zfill(8)}.png"
        logger.info(f"Output {image_file_name}")
        cv2.imwrite(str(image_file_name), heatmap)


if __name__ == "__main__":
    csv_to_img(Path("sensor_1d.csv"), Path("result_img"), 166)
