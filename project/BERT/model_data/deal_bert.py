#!/usr/bin/env python

# encoding: utf-8
'''
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/2/24 11:24
# @Author  : junruit
# @File    : deal_bert.py
# @desc: PyCharm
'''

import random


def write_divide_corpus():
    with open("corpus_1.txt", 'w', encoding='utf-8') as fw:
        with open("corpus.txt", 'r', encoding='utf-8') as f0:
            content = f0.readline()
            while content:
                content = content.replace("。", " ")
                content = content.replace("？", " ")
                content = content.replace("?", ",")
                content = ' '.join(content.split())
                for i in content:
                    str = i + " O\n"
                    fw.write(str)
                content = f0.readline()


def deal_jiajiao():
    with open("corpus_2.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("家 O\n教 O\n中 O\n心 O\n", "家 B-org\n教 I-org\n中 I-org\n心 I-org\n")
            content = content.replace("家 O\n教 O\n", "家 B-pro\n教 I-pro\n")
            fw.write(content)


def deal_duoshaoqian():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("多 O\n少 O\n钱 O\n", "多 B-pri\n少 I-pri\n钱 I-pri\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_shanghaichongqing():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("重 O\n庆 O\n", "重 B-loc\n庆 I-loc\n")
            content = content.replace("上 O\n海 O\n", "上 B-loc\n海 I-loc\n")
            content = content.replace("北 O\n京 O\n", "北 B-loc\n京 I-loc\n")
            content = content.replace("长 O\n沙 O\n", "长 B-loc\n沙 I-loc\n")
            content = content.replace("广 O\n州 O\n", "广 B-loc\n州 I-loc\n")
            content = content.replace("湖 O\n州 O\n", "湖 B-loc\n州 I-loc\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_qingdao():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("青 O\n岛 O\n", "青 B-loc\n岛 I-loc\n")
            content = content.replace("南 O\n京 O\n", "南 B-loc\n京 I-loc\n")
            content = content.replace("培 O\n训 O\n班 O\n", "培 B-org\n训 I-org\n班 I-org\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_fudaoban():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("杭 O\n州 O\n", "杭 B-loc\n州 I-loc\n")
            content = content.replace("湛 O\n江 O\n", "湛 B-loc\n江 I-loc\n")
            content = content.replace("辅 O\n导 O\n班 O\n", "辅 B-org\n导 I-org\n班 I-org\n")
            content = content.replace("中 O\n文 O\n老 O\n师 O\n", "中 B-pro\n文 I-pro\n老 I-pro\n师 I-pro\n")
            content = content.replace("老 O\n师 O\n", "老 B-pro\n师 I-pro\n")
            content = content.replace("教 O\n师 O\n", "教 B-pro\n师 I-pro\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_yuyingshi():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("江 O\n苏 O\n", "江 B-loc\n苏 I-loc\n")
            content = content.replace("苏 O\n州 O\n", "苏 B-loc\n州 I-loc\n")
            content = content.replace("大 O\n连 O\n", "大 B-loc\n连 I-loc\n")
            content = content.replace("广 O\n东 O\n", "广 B-loc\n东 I-loc\n")
            content = content.replace("化 O\n妆 O\n培 O\n训 O\n学 O\n校 O\n", "化 B-org\n妆 I-org\n培 I-org\n训 I-org\n学 I-org\n校 I-org\n")
            content = content.replace("化 O\n妆 O\n培 O\n训 O\n公 O\n司 O\n",
                                      "化 B-org\n妆 I-org\n培 I-org\n训 I-org\n公 I-org\n司 I-org\n")
            content = content.replace("育 O\n婴 O\n师 O\n培 O\n训 O\n", "育 B-org\n婴 I-org\n师 I-org\n培 I-org\n训 I-org\n")
            content = content.replace("育 O\n婴 O\n师 O\n", "育 B-pro\n婴 I-pro\n师 I-pro\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_hushi():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("护 O\n士 O\n", "护 B-loc\n士 I-loc\n")
            content = content.replace("保 O\n洁 O\n公 O\n司 O\n", "保 B-org\n洁 I-org\n公 I-org\n司 I-org\n")
            content = content.replace("保 O\n洁 O\n工 O\n", "保 B-pro\n洁 I-pro\n工 I-pro\n")
            content = content.replace("保 O\n洁 O\n员 O\n", "保 B-pro\n洁 I-pro\n员 I-pro\n")
            content = content.replace("保 O\n洁 O\n", "保 B-pro\n洁 I-pro\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_peixunjigou():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("合 O\n肥 O\n", "合 B-loc\n肥 I-loc\n")
            content = content.replace("护 B-loc\n士 I-loc\n", "护 B-pro\n士 I-pro\n")
            content = content.replace("培 O\n训 O\n机 O\n构 O\n", "培 B-org\n训 I-org\n机 I-org\n构 I-org\n")
            content = content.replace("女 O\n儿 O\n", "女 B-gen\n儿 I-gen\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_peixunxuexiao():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("培 O\n训 O\n学 O\n校 O\n", "培 B-org\n训 I-org\n学 I-org\n校 I-org\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_chengdu():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("成 O\n都 O\n", "成 B-loc\n都 I-loc\n")
            # content = content.replace("贵 B-loc\n阳 I-loc\n", "贵 B-pro\n阳 I-pro\n")
            content = content.replace("贵 B-pro\n阳 I-pro\n", "贵 B-loc\n阳 I-loc\n")
            content = content.replace("贵 O\n阳 O\n", "贵 B-loc\n阳 I-loc\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_hunan():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("湖 O\n南 O\n", "湖 B-loc\n南 I-loc\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_yingyupeixun():
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace("西 O\n安 O\n", "西 B-loc\n安 I-loc\n")
            content = content.replace("天 O\n津 O\n", "天 B-loc\n津 I-loc\n")
            content = content.replace("英 O\n语 O\n培 B-org\n训 I-org\n班 I-org\n", "英 B-org\n语 I-org\n培 I-org\n训 I-org\n班 I-org\n")
            content = content.replace("英 O\n语 O\n培 B-org\n训 I-org\n学 I-org\n校 I-org\n",
                                      "英 B-org\n语 I-org\n培 I-org\n训 I-org\n学 I-org\n校 I-org\n")
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_biaozhutihuan(old, new):
    with open("corpus_1.txt", 'w', encoding="utf-8") as fw:
        with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
            content = f1.read()
            content = content.replace(old, new)
            fw.write(content)
    with open("corpus_2.txt", 'w', encoding="utf-8") as f4:
        with open("corpus_1.txt", 'r', encoding="utf-8") as f3:
            content = f3.read()
            f4.write(content)


def deal_search(s):
    with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
        content = f1.read()
        # content = content.replace(old, new)
        # fw.write(content)
        # if s in content:
        #     return 1
        # else:
        #     return 0
        for i in range(0, len(content)):
            if content[i] == 'o' and content[i+1] == 'r' and content[i+2] != 'g':
                s1 = content[i-2] + content[i-1] + content[i] + content[i+1] + content[i+2] + content[i+3]
                print(s1)
                return 1

        return 0


def deal_search_p(s):
    with open("corpus_2.txt", 'r', encoding="utf-8") as f1:
        content = f1.read()
        # content = content.replace(old, new)
        # fw.write(content)
        # if s in content:
        #     return 1
        # else:
        #     return 0
        for i in range(0, len(content)-4):
            if content[i+1] == 'I' and content[i+2] == '-' and content[i+3] == 'A' :
                s1 = content[i-2] + content[i-1] + content[i] + content[i+1] + content[i+2] + content[i+3]
                print(1234567)
                return 1

        return 0


def valid_test():
    # rule 1 判定正确性，保证语料标注中每行“一个字+空格+对应标签”，语料之中句子与句子之前单独使用一个回车\n来隔断
    # 无遗漏，无错误标签
    # label.txt 文件包含标签目录，同时最后一行无回车\n
    with open("label.txt", 'r', encoding='utf-8') as fd:
        content = fd.read()
    label = content.split("\n")
    print(label)

    with open("corpus_2.txt", 'r', encoding='utf-8') as f4:
        content = f4.read()
    word_vector = content.split("\n")
    # word_vector = [i for i in word_vector if(len(str(i)) != 0)]
    print(word_vector)

    num = 0
    for word in word_vector:
        num = num + 1
        if word != "":
            if word[0] == " ":
                print(num)
                print("wrong")
            chinese = word.split(" ")
            if chinese[1] not in label:
                print(num)
                print(chinese[1])
                print("有标错的标签")
                break
    print("标签正确性检测通过")

    # rule 2 test IBO 标准原则
    num = 43042
    logo = []
    # 把标签组取出
    for word in word_vector:
        if word != "":
            chinese = word.split(" ")
            logo.append(chinese[1])
        else:
            logo.append(word)
    #
    for i in range(0, len(logo))[::-1]:
        num = num - 1
        temp = i
        lab = logo[temp]
        if len(lab) > 0 and logo[temp][0] == "I":
            label_word = logo[temp][2:]
            str_test = 'B-' + label_word
            str_test_2 = 'I-' + label_word
            # 设定报错阈值 100
            length = 1
            while logo[temp] != str_test:
                if logo[temp] != str_test_2:
                    print(num)
                    print("wrong")
                    return -1
                temp = temp - 1
                length = length + 1
    print("IBO规则通过")

    # rule 3 按句子 将顺序打混 并切分文件
    with open("corpus_2.txt", 'r', encoding='utf-8') as fa:
        content = fa.read()
    # for w in range(0, len(content)):
    #     if content[w] == "\n":
    #         num = num + 1
    #     if content[w] == "\n" and content[w+1] == "\n" and content[w+2] == "\n":
    #         print(num)
    #     break
    # if "\n\n\n" in content:
    #     print("aaaaa")
    sentence_vector = content.split("\n\n")
    print(sentence_vector)
    random.shuffle(sentence_vector)
    print(sentence_vector)
    with open("corpus_1.txt", 'w', encoding='utf-8') as fw:
        for sentence in sentence_vector:
            fw.write(sentence)
            fw.write("\n\n")
    # 按比例拆分成文件后最终保证dev.txt,train.txt等以两个\n结束作为模型训练的输入
    # 43000 * 8/10
    print(len(sentence_vector))
    with open("train.txt", 'w', encoding='utf-8') as ftr:
        for ss in range(0, 1250):
            ftr.write(sentence)
            ftr.write("\n\n")
    with open("dev.txt", 'w', encoding='utf-8') as ftr:
        for ss in range(1250, 1850):
            ftr.write(sentence)
            ftr.write("\n\n")
    with open("test.txt", 'w', encoding='utf-8') as ftr:
        for ss in range(1850, len(sentence_vector)):
            ftr.write(sentence)
            ftr.write("\n\n")
    return 1

def haoqiguai():
    with open("corpus_1.txt", 'r', encoding = 'utf-8') as ft:
        content = ft.readline()
        num = 1
        while content:
            if content != "\n":
                num = num + 1
            content = ft.readline()
    print(num)
    with open("corpus_2.txt", 'r', encoding = 'utf-8') as fk:
        content = fk.readline()
        num = 1
        while content:
            if content != "\n":
                num = num + 1
            content = fk.readline()
    print(num)

# deal_biaozhutihuan("深 O\n圳 O\n", "深 B-loc\n圳 I-loc\n")
# deal_biaozhutihuan("费 O\n用 O\n多 O\n少 O\n", "费 B-pri\n用 I-pri\n多 O\n少 O\n")
# deal_biaozhutihuan("沈 O\n阳 O\n", "沈 B-loc\n阳 I-loc\n")
# deal_biaozhutihuan("珠 O\n海 O\n", "珠 B-loc\n海 I-loc\n")
# deal_biaozhutihuan("宁 O\n波 O\n", "宁 B-loc\n波 I-loc\n")
# deal_biaozhutihuan("山 O\n东 O\n", "山 B-loc\n东 I-loc\n")
# deal_biaozhutihuan("英 O\n语 O\n培 B-org\n训 I-org\n机 I-org\n构 I-org\n", "英 B-org\n语 I-org\n培 I-org\n训 I-org\n机 I-org\n构 I-org\n")
# deal_biaozhutihuan("海 O\n南 O\n", "海 B-loc\n南 I-loc\n")
# deal_biaozhutihuan("电 O\n脑 O\n培 O\n训 O\n", "电 B-pro\n脑 I-pro\n培 I-pro\n训 I-pro\n")
# deal_biaozhutihuan("昆 O\n明 O\n", "昆 B-loc\n明 I-loc\n")
# deal_biaozhutihuan("英 O\n语 O\n培 O\n训 O\n", "英 B-pro\n语 I-pro\n培 I-pro\n训 I-pro\n")
# deal_biaozhutihuan("少 O\n儿 O\n", "少 B-age\n儿 I-age\n")
# deal_biaozhutihuan("福 O\n州 O\n", "福 B-loc\n州 I-loc\n")
# deal_biaozhutihuan("厦 O\n门 O\n", "厦 B-loc\n门 I-loc\n")
# deal_biaozhutihuan("海 O\n口 O\n", "海 B-loc\n口 I-loc\n")
# deal_biaozhutihuan("武 O\n汉 O\n", "武 B-loc\n汉 I-loc\n")
# deal_biaozhutihuan("云 O\n南 O\n", "云 B-loc\n南 I-loc\n")
# deal_biaozhutihuan("石 O\n家 O\n庄 O\n", "石 B-loc\n家 I-loc\n庄 I-loc\n")
# deal_biaozhutihuan("暑 O\n假 O\n", "暑 B-tim\n假 I-tim\n")
# deal_biaozhutihuan("东 O\n菀 O\n", "东 B-loc\n菀 I-loc\n")
# deal_biaozhutihuan("郑 O\n州 O\n", "郑 B-loc\n州 I-loc\n")
# deal_biaozhutihuan("网 O\n页 O\n设 O\n计 O\n", "网 B-pro\n页 I-pro\n设 I-pro\n计 I-pro\n")
# deal_biaozhutihuan("山 O\n西 O\n", "山 B-loc\n西 I-loc\n")
# deal_biaozhutihuan("小 O\n学 O\n", "小 B-tim\n学 I-tim\n")
# deal_biaozhutihuan("幼 O\n儿 O\n", "幼 B-tim\n儿 I-tim\n")
# deal_biaozhutihuan("汕 O\n头 O\n", "汕 B-loc\n头 I-loc\n")
# deal_biaozhutihuan("高 O\n中 O\n", "高 B-tim\n中 I-tim\n")
# deal_biaozhutihuan("东 O\n莞 O\n", "东 B-loc\n莞 I-loc\n")
# deal_biaozhutihuan("菀 I-loc\n", "莞 I-loc\n")
# deal_biaozhutihuan("哈 O\n尔 O\n滨 O\n", "哈 B-loc\n尔 I-loc\n滨 I-loc\n")
# deal_biaozhutihuan("江 O\n门 O\n", "江 B-loc\n门 I-loc\n")
# deal_biaozhutihuan("松 O\n江 O\n", "松 B-loc\n江 I-loc\n")
# deal_biaozhutihuan("中 O\n山 O\n", "中 B-loc\n山 I-loc\n")
# deal_biaozhutihuan("济 O\n南 O\n", "济 B-loc\n南 I-loc\n")

# deal_biaozhutihuan("嵌 O\n入 O\n式 O\n", "嵌 B-pro\n入 I-pro\n式 I-pro\n")
# deal_biaozhutihuan("长 O\n春 O\n", "长 B-loc\n春 I-loc\n")
# print(deal_search("or"))
# deal_biaozhutihuan("佛 O\n山 O\n", "佛 B-loc\n山 I-loc\n")
# deal_biaozhutihuan("包 O\n头 O\n", "包 B-loc\n头 I-loc\n")
# deal_biaozhutihuan("泉 O\n州 O\n", "泉 B-loc\n州 I-loc\n")
# deal_biaozhutihuan("宜 O\n昌 O\n", "宜 B-loc\n昌 I-loc\n")
# deal_biaozhutihuan("惠 O\n州 O\n", "惠 B-loc\n州 I-loc\n")
# deal_biaozhutihuan("南 O\n宁 O\n", "南 B-loc\n宁 I-loc\n")
# deal_biaozhutihuan("洛 O\n阳 O\n", "洛 B-loc\n阳 I-loc\n")
# deal_biaozhutihuan("乐 O\n山 O\n", "乐 B-loc\n山 I-loc\n")
# deal_biaozhutihuan("陕 O\n西 O\n", "陕 B-loc\n西 I-loc\n")
# deal_biaozhutihuan("南 O\n昌 O\n", "南 B-loc\n昌 I-loc\n")
# deal_biaozhutihuan("绍 O\n兴 O\n", "绍 B-loc\n兴 I-loc\n")
# deal_biaozhutihuan("无 O\n锡 O\n", "无 B-loc\n锡 I-loc\n")
# deal_biaozhutihuan("望 O\n京 O\n", "望 B-loc\n京 I-loc\n")
# deal_biaozhutihuan("搬 O\n家 O\n公 O\n司 O\n", "搬 B-org\n家 I-org\n公 I-org\n司 I-org\n")
# deal_biaozhutihuan("太 O\n原 O\n", "太 B-loc\n原 I-loc\n")
# deal_biaozhutihuan("装 O\n修 O\n公 O\n司 O\n", "装 B-org\n修 I-org\n公 I-org\n司 I-org\n")
# deal_biaozhutihuan("海 O\n宁 O\n", "海 B-loc\n宁 I-loc\n")
# deal_biaozhutihuan("养 O\n老 O\n院 O\n", "养 B-org\n老 I-org\n院 I-org\n")
# deal_biaozhutihuan("常 O\n州 O\n", "常 B-loc\n州 I-loc\n")
# deal_search_p(2)
# deal_biaozhutihuan("月 O\n子 O\n中 O\n心 O\n", "月 B-org\n子 I-org\n中 I-org\n心 I-org\n")
# deal_biaozhutihuan("鞍 O\n山 O\n", "鞍 B-loc\n山 I-loc\n")
#deal_biaozhutihuan("产 O\n后 O\n恢 O\n复 O\n中 O\n心 O\n", "产 B-org\n后 I-org\n恢 I-org\n复 I-org\n中 I-org\n心 I-org\n")
# deal_biaozhutihuan("产 O\n后 O\n修 O\n复 O\n中 O\n心 O\n", "产 B-org\n后 I-org\n修 I-org\n复 I-org\n中 I-org\n心 I-org\n")
# deal_biaozhutihuan("催 O\n乳 O\n师 O\n", "催 B-pro\n乳 I-pro\n师 I-pro\n")
# deal_biaozhutihuan("家 O\n政 O\n公 O\n司 O\n", "家 B-org\n政 I-org\n公 I-org\n司 I-org\n")
# deal_biaozhutihuan("温 O\n州 O\n", "温 B-loc\n州 I-loc\n")
# deal_biaozhutihuan("产 O\n后 O\n护 O\n理 O\n中 O\n心 O\n", "产 B-org\n后 I-org\n护 I-org\n理 I-org\n中 I-org\n心 I-org\n")
# deal_biaozhutihuan("月 O\n子 O\n护 O\n理 O\n中 O\n心 O\n", "月 B-org\n子 I-org\n护 I-org\n理 I-org\n中 I-org\n心 I-org\n")
# deal_biaozhutihuan("月 O\n子 O\n会 O\n所 O\n", "月 B-org\n子 I-org\n会 I-org\n所 I-org\n")
# deal_biaozhutihuan("肇 O\n庆 O\n", "肇 B-loc\n庆 I-loc\n")
# deal_biaozhutihuan("广 O\n西 O\n", "广 B-loc\n西 I-loc\n")
# deal_biaozhutihuan("黑 O\n龙 O\n江 O\n", "黑 B-loc\n龙 I-loc\n江 I-loc\n")
# deal_biaozhutihuan("秦 O\n皇 O\n岛 O\n", "秦 B-loc\n皇 I-loc\n岛 I-loc\n")
# deal_biaozhutihuan("123", "123")
valid_test()
# haoqiguai()

