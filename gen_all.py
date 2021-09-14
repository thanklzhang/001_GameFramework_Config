# -*- coding: utf-8 -*-
#!/usr/bin/python

import gen_logic
import sys

import os
import shutil

################ 配置
# table 文件输入目录
table_input_dir = 'data_table'

# 客户端 cs define 文件输出目录
client_cs_out_dir = "../001_GameFramework_Client/Assets/Script/Data/Define/Table"
# 客户端 json 文件输出目录
client_json_out_dir = "../001_GameFramework_Client/Assets/BuildRes/TableData"

# 服务端 cs define 文件输出目录
server_cs_out_dir = "../001_GameFramework_Server/GameServer/Common/Config/Table/Define"
# 服务端 json 文件输出目录
server_json_out_dir = "../001_GameFramework_Server/GameServer/netcoreapp3.1/Resource/Table"
#服务器端有可能在 IDE 中调试 所以在每个工程下都复制下所有 json
battle_self_table_path = "../001_GameFramework_Server/GameServer/BattleServer/bin/Debug/netcoreapp3.1/Resource/Table"

#################

def main(argv):

    #这里目前用的是一样的导表 看情况前后端可以用两套导表逻辑

    #client
    gen_logic.gen(table_input_dir,client_cs_out_dir,gen_logic.OpType.cs)
    gen_logic.gen(table_input_dir,client_json_out_dir,gen_logic.OpType.json)
    
    #server
    gen_logic.gen(table_input_dir,server_cs_out_dir,gen_logic.OpType.cs)
    gen_logic.gen(table_input_dir,server_json_out_dir,gen_logic.OpType.json)
   
    Copy(server_json_out_dir,battle_self_table_path)
    


def Copy(source_path,target_path):
    print('start to copy files ... : ' + source_path + " -> " + target_path)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file)
                shutil.copy(src_file, target_path)
                print(src_file)
    print('copy files finished!')

##################
if __name__ == "__main__":
    main(sys.argv)
