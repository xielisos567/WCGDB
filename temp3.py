#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 打开名为 LINE.txt 的文件，读取其中的所有行，去除每行末尾的换行符，将结果存储在列表 query_list 中
with open(r"list_salmonella.txt", "r", encoding="utf-8") as query_file:
    text_list = query_file.readlines()
    query_list = []
    for i in text_list:
        query_list.append(i.strip())

# 打开名为 assembly.txt 的文件，读取其中的所有行，将每行以制表符为分隔符拆分成两个部分，将第一部分作为键，将整行作为值，存储在 ref_list 中
with open(r"Salmonella_link_guoyaqiong.txt", "r", encoding="utf-8") as reference_file:
    ref_list = []   #这里注意要用列表[]格式而不是字典{}格式，否则重复的抓不出来，反之亦然，重复值只抓取一个则用字典格式
    while True:
        text = reference_file.readline()
        if not text:
            break
        seq_name = text.strip().split("\t")[0]
        ref_list.append(text)

# 打开名为 matching.txt 和 not_matching.txt 的文件，用于存储匹配和不匹配的数据
with open(r"matching.txt", "w", encoding="utf-8") as match_file:
    with open(r"not_matching.txt", "w", encoding="utf-8") as not_match_file:
        # 遍历 ref_list 中的每个元素，将每个元素以制表符为分隔符拆分成两个部分，将第一部分作为键值，判断该键值是否在 query_list 中，如果在则将整个元素写入 matching.txt 文件中，否则将整个元素写入 not_matching.txt 文件中
        for ref_text in ref_list:
            seq_name = ref_text.strip().split("\t")[0]
            if seq_name in query_list:
                match_file.write(ref_text)
            else:
                not_match_file.write(ref_text)

