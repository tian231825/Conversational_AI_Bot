# Conversational_AI_Bot

ICWS2020_User Intention Recognition and Requirement Elicitation Method for Conversational AI Service_Project

We push our dataset and project code of experiment in this repository.

2020/01/23 We push the BERT Model Fine-tuning data in Conversation_AI_Bot\project\BERT\model_data

2020/02 data-processing

We add our dialog_policy test data in *data/* 

And we push each module code and input in *project/../* 

> data-normalization

**表1-数据处理**
<center>

| 类型 | 数据类型 | 备注|
| :----: | :----:  | :----: |
| id     | int    | |
| 性别  | int | 男：0，女：1 |
| 民族  | int | 汉：0，满族：1，新疆：2 |
| 年龄  | int | |
| 学历  | int | |
| 在职离职  | int |  'IN'：0，'OFF'：1 |
| 工作经验  | float | 保留一位小数 |
| 服务范围  | int |  见下表2|
| 评价 | float|  保留两位小数 |
| 金额 | float|  归一化之后，保留两位小数 |
| 服务类型 | int | 见表3 |

</center>

**表2-服务范围**
<center>

| id | 对应地区 |
| :----: | :----:  |
| 经区,环翠区     | 0   |
| 经区,高区,环翠区,其他  | 1 |
| 经区,高区,环翠区  | 2  |
| 环翠区  | 3  |
| 高区 | 4 |
| 经区  | 5 |
| 经区,高区  | 6 |
| 高区,环翠区  | 7 |
| 经区,环翠区,其他 | 8|	
| 经区,其他 | 9|	
| 环翠区,其他 | 10|	
| 其他 | 11|	
经区,高区,其他 | 12|	
高区,环翠区,其他 | 13|	

</center>

**表3-服务类型**
<center>

| 类型id | 类型名称 |
| :----: | :----:  |
| 1      | 保姆    |
| 2  | 月嫂 |
| 3  | 育婴师 |
| 4  | 护工 |
| 5  | 产后修复 |
| 6  | 保洁清洁 |
| 7  | 培训学校 |
| 8  | 钟点工 |
| 9 | 社区服务|

</center>