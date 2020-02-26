import config
import models
import tensorflow as tf
import numpy as np
import json
import os

os.environ['CUDA_VISIBLE_DEVICES']='7'
# (1) Set import files and OpenKE will automatically load models via tf.Saver().
con = config.Config()
str_os = os.path.abspath(os.path.join(os.getcwd(), ".."))
print(str_os)
con.set_in_path("../TransH/benchmarks/data/")
# con.set_test_link_prediction(True)
con.set_test_triple_classification(True)
con.set_work_threads(8)
con.set_dimension(100)
con.set_import_files("../TransH/res/model.vec.tf")
con.init()
con.set_model(models.TransH)
con.test()

list1 = []
# os.remove("./trans_out_res.txt")
# with open("./trans_out_res.txt", 'a', encoding='utf-8') as f:
#     with open("../step/chat_test.txt", 'r', encoding='utf-8') as fc:
if os.path.exists("../TransH/trans_out_res.txt"):
    os.remove("../TransH/trans_out_res.txt")
with open("../TransH/trans_out_res.txt", 'a', encoding='utf-8') as f:
    # with open("../TransH/trans_out_res1.txt", 'a', encoding='utf-8') as fx:
        with open("../step/chat_test.txt", 'r', encoding='utf-8') as fc:
            content = fc.readline()
            while content:
                content = content.replace("\n", "")
                list1 = content.split(",")
                if len(list1) == 4:
                    if int(list1[0]) == 1:
                        f.write(str(con.predict_tail_entity(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                        # fx.write(str(con.predict_tail_entity(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                    elif int(list1[0]) == 2:
                        f.write(str(con.predict_head_entity(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                        # fx.write(str(con.predict_head_entity(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                    elif int(list1[0]) == 3:
                        f.write(str(con.predict_relation(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                        # fx.write(str(con.predict_relation(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                    elif int(list1[0]) == 4:
                        # h, t, r
                        f.write(str(con.predict_triple(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                        # fx.write(str(con.predict_triple(int(list1[1]), int(list1[2]), int(list1[3]))) + "\n")
                    else:
                        print("the flag of test_trans is wrong_tag!\n1:tail,2:head,3:relation,4:judge\n")
                else:
                    print("the length of chat_test.txt is wrong!!!\n")
                content = fc.readline()

print("finish!")

# con.show_link_prediction(2,1)
# con.show_triple_classification(2,1,3)
# (2) Read model parameters from json files and manually load parameters.
# con = config.Config()
# con.set_in_path("./benchmarks/FB15K/")
# con.set_test_flag(True)
# con.set_work_threads(4)
# con.set_dimension(50)
# con.init()
# con.set_model(models.TransE)
# f = open("./res/embedding.vec.json", "r")
# content = json.loads(f.read())
# f.close()
# con.set_parameters(content)
# con.test()

# (3) Manually load models via tf.Saver().
# con = config.Config()
# con.set_in_path("./benchmarks/FB15K/")
# con.set_test_flag(True)
# con.set_work_threads(4)
# con.set_dimension(50)
# con.init()
# con.set_model(models.TransE)
# con.import_variables("./res/model.vec.tf")
# con.test()
