#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/7/30 16:47
# @Author  : Ren_Xingtao

from collections import defaultdict

input_file_path = r'/mnt/d/biosample_script/biosample_result_Shigella_new.txt'
output_file_path = r'/mnt/d/biosample_script/result.txt'

bio_sample = defaultdict(list)
with open(input_file_path, 'r', encoding="utf-8") as input_file:
    # 提取各BioSample详细信息分割保存为相应键值对
    while True:
        line = input_file.readline()
        if not line:
            break
        if line.isspace():
            continue
        if line[0].isdigit() and ":" in line:
            tag = line.strip().split(":")[0]
            bio_sample[tag].append(line)
        else:
            bio_sample[tag].append(line)
with open(output_file_path, "w", encoding="utf-8") as output_file:
    output_file.write("BioSample\tSRA\tOrganism\tstrain\tisolate\tcollected by\tcollection date\tgeographic location\t"
                      "host\thost disease\tisolation source\tlatitude and longitude\tAccession ID\n")
    for key, value in bio_sample.items():
        temp_str = "\t".join(value)
        if "BioSample:" in temp_str:  # 提取biosample收录号
            bio_number = temp_str.strip().split("BioSample:")[1].split()[0].split(";", 1)[0].strip()
        else:
            bio_number = ""
        if "SRA:" in temp_str:  # 提取SAR编号
            sar_number = temp_str.strip().split("SRA:")[1].split()[0].split(";", 1)[0].strip()
        else:
            sar_number = ""
        if "Organism:" in temp_str:  # 提取Organism描述信息
            org_info = temp_str.strip().split("Organism:")[1].splitlines()[0].strip()
        else:
            org_info = ""
        if "/strain=" in temp_str:  # 提取strain描述信息
            strain = eval(r'temp_str.strip().split("/strain=")[1].splitlines()[0].strip()')
        else:
            strain = ""
        if "/isolate=" in temp_str:  # 提取isolate描述信息
            isolate = eval(r'temp_str.strip().split("/isolate=")[1].splitlines()[0].strip()')
        else:
            isolate = ""
        if "/collected by=" in temp_str:  # 提取collected by描述信息
            col_by = eval(r'temp_str.strip().split("/collected by=")[1].splitlines()[0].strip()')
        else:
            col_by = ""
        if "/collection date=" in temp_str:  # 提取collection date描述信息
            col_date = eval(r'temp_str.strip().split("/collection date=")[1].splitlines()[0].strip()')
        else:
            col_date = ""
        if "/geographic location=" in temp_str:  # 提取geographic location描述信息
            geo_loc = eval(r'temp_str.strip().split("/geographic location=")[1].splitlines()[0].strip()')
        else:
            geo_loc = ""
        if "/host=" in temp_str:  # 提取host描述信息
            host = eval(r'temp_str.strip().split("/host=")[1].splitlines()[0].strip()')
        else:
            host = ""
        if "/host disease=" in temp_str:  # 提取host disease描述信息
            host_disease = eval(r'temp_str.strip().split("/host disease=")[1].splitlines()[0].strip()')
        else:
            host_disease = ""
        if "/isolation source=" in temp_str:  # 提取isolation source描述信息
            iso_source = eval(r'temp_str.strip().split("/isolation source=")[1].splitlines()[0].strip()')
        else:
            iso_source = ""
        if "/latitude and longitude=" in temp_str:  # 提取latitude and longitude描述信息
            lat_long = eval(r'temp_str.strip().split("/latitude and longitude=")[1].splitlines()[0].strip()')
        else:
            lat_long = ""
        if "ID:" in temp_str:  # 提取Accession ID号
            ac_id = temp_str.strip().split("ID:")[1].split()[0].split(";", 1)[0].strip()
        else:
            ac_id = ""
        output_file.write(bio_number + "\t" + sar_number + "\t" + org_info + "\t" + strain + "\t" + isolate + "\t" +
                          col_by + "\t" + col_date + "\t" + geo_loc + "\t" + host + "\t" + host_disease + "\t" +
                          iso_source + "\t" + lat_long + "\t" + ac_id + "\n")
