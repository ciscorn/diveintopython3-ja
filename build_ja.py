#!/usr/bin/env python3

import os
import os.path
import shutil
from glob import glob
from itertools import count


def load_trans(trans_path):
    COMMENT, EN, JA = "#", "en:", "ja:"
    trans_dict = {}
    en = None
    with open(trans_path) as f:
        for (lineno, line) in zip(count(1), f):
            if line.startswith(COMMENT):
                pass
            elif line.startswith(EN):
                en = line[len(EN):].rstrip()
            elif line.startswith(JA):
                if not en:
                    raise Exception(
                        "invalid en-ja pair found at line " + str(lineno))
                trans_dict[en] = line[len(JA):].rstrip()
                en = None
            else:
                if line.rstrip():
                    raise Exception(
                        "invalid line found at line " + str(lineno))
    return trans_dict


def translate(trans_path, src_path, dst_path):
    print("generating", dst_path, "...")

    trans_dict = load_trans(trans_path)
    trans_dict.update(load_trans("trans/common.trans"))

    with open(src_path, encoding="utf-8") as srcf:
        with open(dst_path, mode="w", encoding="utf-8") as dstf:
            for line in srcf:
                en = line.rstrip()
                dstf.write(trans_dict.get(en, en) + '\n')


if __name__ == "__main__":
    output_files = set()
    if not os.path.exists("output"):
        os.mkdir("output")

    for src_path in glob("original/*.html"):
        (dirs, filename) = os.path.split(src_path)
        trans_path = os.path.join("trans", filename + ".trans")
        if os.path.exists(trans_path):
            dst_path = os.path.join("output", filename)
            translate(trans_path, src_path, dst_path)
            output_files.add(dst_path)

    for path in (set(glob("output/*")) - output_files):
        if os.path.isdir(path):
            print('removing', path, '...')
            shutil.rmtree(path)
        else:
            print('removing', path, '...')
            os.remove(path)
