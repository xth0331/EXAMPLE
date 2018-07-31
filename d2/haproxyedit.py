#!/usr/bin/env python
# -*- coding:utf-8 -*-



import os,sys


def numif(number_input): # 判断输入是否为数字
    while not number_input.isdigit():    # 输入不是数字就进入循环
        number_input = input('\033[31m 输入%s不是数字，请重新输入!\033[0m' % number_input)    # 提示重新输入
    number = number_input
    return number


def show_list(file):   # 查询显示并将文本生成程序需要的字典和列表
    backend_list = []
    backend_all_dict = {}
    backend_dict = {}
    server_list = []
    with open(file,'r') as f:    # 读取haproxy文件
        for line in f:

            line = line.strip()
            if line.startswith('backend') == True:    # 判断是否是backend开头，读取backend信息写到backend_list中
                backend_name = line.split()[1]
                backend_list.append(backend_name)    # 将文件中backend加到列表中
                server_list = []   # 清空server_list里的记录，遇到新backend可以输入新的server_list

            elif line.startswith('server') == True:    # 判断是否是server开头，读取server信息写到backend_all_dict中
                backend_dict['name'] = line.split()[1]    # 读取文件中server的name
                backend_dict['IP'] = line.split()[2]    # 读取文件中server的IP
                backend_dict['weight'] = line.split()[4]    # 读取文件中server的weight
                backend_dict['maxconn'] = line.split()[6]   # 读取文件中server的maxconn
                server_list.append(backend_dict.copy())    # 将backend中的信息加到server_list中,此处需要用copy
                backend_all_dict[backend_name] = server_list    # 将server信息对应backend存到字典中

    return (backend_list,backend_all_dict)    # 返回backend和server信息


def backend_show(backend_list):    # 展示backend列表内容
    backend_show_dict = {}
    print("-------------------------------------------------")
    print("\t\t\t欢迎来到HAproxy文件配置平台")
    print("-------------------------------------------------")
    print("backend列表信息如下：")
    for k,v in enumerate(backend_list,1):    # 逐行读取backend信息并展示
        print(k, v)
        backend_show_dict[str(k)] = v
    return backend_show_dict    # 返回backend和对应编号


def server_show(backend_input,backend_all_dict):    # 展示backend下server内容
    server_show_dict = {}
    server_list = backend_all_dict[backend_input]
    for k,v in enumerate(server_list,1):    # 编号展示server信息
        print(k,"name:",v['name'],"\tIP:",v['IP'],"\tweight:",v['weight'],"\tmaxconn:",v['maxconn'])
        server_show_dict[k] = v
    return server_show_dict    # 返回编号对应的server字典


def action_list():    # 显示操作列表和编号，并返回操作编号
    print("-------------------------------------------------")
    print("操作清单如下：")
    print('''
    1.查询backend和server信息
    2.添加backend和server信息
    3.修改backend和server信息
    4.删除backend和server信息
    5.退出
    ''')
    print("-------------------------------------------------")
    action_num = numif(input("请输入需要操作的编号：（请输入数字）"))
    return action_num


def inquiry(inquiry_input):    # 定义查询功能
    while True:
        if inquiry_input in backend_show_dict:    # 编号输入分支
            backend_input = backend_show_dict[inquiry_input]    # 输入编号得到backend
            print(backend_input, ":")
            server_show(backend_input, backend_all_dict)    # 调用server_show，展示backend下server
            break

        elif inquiry_input in backend_show_dict.values():    # backend名称输入分支
            print(inquiry_input, ":")
            server_show(inquiry_input, backend_all_dict)    # 调用server_show，展示backend下server
            break

        else:    # 校验异常输入
            inquiry_input = input("输入错误，请重新输入：")


def add(add_input,file):    # 定义添加功能
    (backend_list, backend_all_dict) = show_list(file)
    while True:
        if add_input in backend_show_dict:    #添加原有backend下server
            add_dict = {}
            add_dict['name'] = input("请输入需增加server名称：")
            add_dict['IP'] = input("请输入需增加IP地址：")
            add_dict['weight'] = input("请输入需增加weight值：")
            add_dict['maxconn'] = input("请输入需增加maxcoon值：")
            backend_name_add = backend_list[int(add_input)-1]

            for dict in backend_all_dict[backend_name_add]:    # 实现IP已存在，更新weight信息和maxconn信息
                if add_dict['IP'] in dict.values():
                    dict['weight'] = add_dict['weight']
                    dict['maxconn'] = add_dict['maxconn']
                    break

                else:    # IP不存在，就将server增加到backend下
                    backend_all_dict[backend_name_add].append(add_dict)

            backup(file,backend_name_add,backend_all_dict)    # 调用backup函数，将新增内容读写到文件中
            print('''name：%s IP：%s weight：%s maxconn：%s已添加成功'''%(
            add_dict['name'],add_dict['IP'],add_dict['weight'],add_dict['maxconn']))    # 提示添加成功
            break

        else:    # 添加新backend下的server
            add_dict = {}
            add_dict['name'] = input("请输入%s下新增server名称："%add_input)
            add_dict['IP'] = input("请输入%s下新增IP地址："%add_input)
            add_dict['weight'] = input("请输入%s下新增weight值："%add_input)
            add_dict['maxconn'] = input("请输入%s下新增maxcoon值："%add_input)
            backend_name_add = add_input
            backend_all_dict[backend_name_add] = add_dict    # 将新增backend和对应server存到字典中

            file_new = "%s_new" % file    # 新建一个文件，用来新增数据
            with open(file, 'r') as f_read, open(file_new, 'a+') as f_write:   # 读取file文件，追加backend信息
                for line in f_read:
                    f_write.write(line)
                f_write.write("\nbackend %s" % backend_name_add)    # 追加backend信息
                server_line_write = '\n\t\tserver {name} {IP} weight {weight} maxconn {maxconn}\n'    # 追加server信息
                f_write.write(server_line_write.format(**add_dict))    # 格式化输出

            os.system('mv %s %s_backup' % (file, file))    # 将file文件名改为file_backup
            os.system('mv %s %s' % (file_new, file))    # 将file_new文件名改为file，实现备份
            print("\nbackend %s" % backend_name_add)
            print('''name：%s IP：%s weight：%s maxconn：%s已添加成功''' % (
            add_dict['name'], add_dict['IP'], add_dict['weight'], add_dict['maxconn']))    # 提示添加成功
            break


def revise(revise_input):    # 定义修改功能
    revise_dict = {}
    if revise_input in backend_show_dict:    # 判断输入是否存在
        backend_revise = backend_show_dict[revise_input]    # 通过编号获取backend
        revise_choise = input("是否需要修改该backend名称：%s；确认请按'y'，按任意键继续："%backend_revise)    # 确认是否修改backend名，输入y修改，否则继续修改
        if revise_choise == 'y':
            backend_revise_new = input("请输入修改后的backend名：")    # 修改backend名
            backend_all_dict[backend_revise_new] = backend_all_dict.pop(backend_revise)    # 将旧backend的server对应到修改后的backend上
            revise_choise_server = input("是否需要继续修改%s下的server：确认请按'y'，按任意键继续："%backend_revise_new)    # 询问是否继续修改
            if revise_choise_server == 'y':    # 继续修改server
                server_revise_dict = server_show(backend_revise_new, backend_all_dict)    # 展示server信息
                server_revise_num = numif(input("请输入需要修改的server编号："))   # 获取需要修改的server编号
                revise_dict['name'] = input("请输入修改后的name：")
                revise_dict['IP'] = input("请输入修改后的IP：")
                revise_dict['weight'] = input("请输入修改后的weight：")
                revise_dict['maxconn'] = input("请输入修改后的maxconn：")
                server_revise_dict[int(server_revise_num)] = revise_dict    # 通过编号修改server信息
                server_revise_dict_backup = {}
                server_revise_dict_backup[backend_revise_new] = server_revise_dict.values()    # 将修改的server信息对应到修改后的backend存到字典中
                backup(file, backend_revise, server_revise_dict_backup,backend_revise_new)    # 调用backup函数，操作文件

            else:    # 不修改server，只修改了backend
                backup(file, backend_revise, backend_all_dict,backend_revise_new)
        else:    # 未修改backend名情况时修改server信息
            server_revise_dict = server_show(backend_revise, backend_all_dict)
            server_revise_num = numif(input("请输入需要修改的server编号："))    # 获取需修改的server编号
            revise_dict['name'] = input("请输入修改后的name：")
            revise_dict['IP'] = input("请输入修改后的IP：")
            revise_dict['weight'] = input("请输入修改后的weight：")
            revise_dict['maxconn'] = input("请输入修改后的maxconn：")
            server_revise_dict[int(server_revise_num)] = revise_dict    # 修改的server信息对应到编号中存到字典中
            server_revise_dict_backup = {}
            server_revise_dict_backup[backend_revise] = server_revise_dict.values()    # 将修改后的server信息对应backend存到字典中
            backup(file,backend_revise,server_revise_dict_backup)    # 调用backup函数，操作文件
    else:    # 输入错误提示重新输入
        revise_input_return = input("需修改backend不存在，请重新输入：")
        revise(revise_input_return)


def delete(delete_input):    # 定义删除功能
    if delete_input in backend_show_dict:
        backend_delete = backend_show_dict[delete_input]
        delete_choise = input("是否需要删除该backend：%s；确认请按'y'，按任意键继续："%backend_delete)
        if delete_choise == 'y':    # 判断是否删除backend信息
            del backend_all_dict[backend_delete]    # 在backend与server总字典中删除backend
            backup(file, backend_delete, backend_all_dict)    # 调用backup函数，操作文件

        else:    # 删除server
            server_delete_dict = server_show(backend_delete, backend_all_dict)
            server_delete_num = int(numif(input("请输入需要删除的server编号：")))    # 除判断是否时数字外，还需转换为整数型
            while True:    # 删除backend下的server循环
                if server_delete_num in server_delete_dict:    # 判断输入编号是否存在
                    server_delete_dict.pop(server_delete_num)
                    server_delete_dict_backup = {}
                    server_delete_dict_backup[backend_delete] = server_delete_dict.values()
                    backup(file, backend_delete, server_delete_dict_backup)    # 调用backup函数，操作文件
                    break
                else:
                    server_delete_num = input("输入编号不存在，请重新输入：")    # 提示输入错误


def backup(file,backend_name_action,backend_backup_dict,*backend_name_revise):    # 定义文档备份与回写功能
    file_new = "%s_new"%file
    add_flag = False    # 为跳过原backend下server存在
    with open(file,'r') as f_read , open(file_new,'w+') as f_write:    # 同时打开读文件和写文件
        for line in f_read:    # 读取每行信息
            backend_name = "backend %s" % backend_name_action
            backend_name_revise = "".join(tuple(backend_name_revise))    # 修改功能会传参，将元组转换为字符串
            if line.strip() == backend_name:    # 读取某行中有参数中的backend
                if backend_name_action not in backend_backup_dict and backend_name_revise not in backend_backup_dict:  # 为了删除backend而存在
                    add_flag = True
                    pass

                elif backend_name_revise in backend_backup_dict:    # 判断修改功能中修改后backend存在与字典中
                    line_revise = "backend %s\n" % backend_name_revise
                    f_write.write(line_revise)
                    for add_dict in backend_backup_dict[backend_name_revise]:    # 逐行读取修改backend下的server信息
                        server_line_write = '\t\tserver {name} {IP} weight {weight} maxconn {maxconn}\n'
                        f_write.write(server_line_write.format(**add_dict))    # 格式化输出
                    add_flag = True

                else:
                    f_write.write(line)    # 将此行写在文件中
                    for add_dict in backend_backup_dict[backend_name_action]:    # 读取该backend下所有server信息
                        server_line_write = '\t\tserver {name} {IP} weight {weight} maxconn {maxconn}\n'
                        f_write.write(server_line_write.format(**add_dict))
                    add_flag = True

            elif line.strip().startswith("server") == True and add_flag == True:  # 为了跳过原backend下的server
                pass

            else:    # 写无用行
                f_write.write(line)
                add_flag = False    # 写下无用行后可以继续循环

    os.system('mv %s %s_backup' % (file, file))
    os.system('mv %s %s' % (file_new, file))


def backend_exit():    #定义退出功能
    flag_exit = True
    b_input = input("操作完毕退出请按'b'：")
    while flag_exit:
        if b_input == 'b':
            flag_exit = False
            return flag_exit

        else:
            return backend_exit()   #使用尾递归优化，加上return帮助直接退出，而不需要递归一层层退出


flag = True    # 主函数开始
while flag:
    flag_main = True
    flag_action = True
    file = 'haproxy'    # 文件名赋值
    (backend_list, backend_all_dict) = show_list(file)    # 调用show_list函数获取backend和server信息
    backend_show_dict = backend_show(backend_list)    # 展示backend信息
    action_num = action_list()    # 展示功能项，并输入操作编号
    while flag_main:
        if action_num == '1':
            inquiry(input("请输入需要查询的backend编号或名称："))
            flag_main = backend_exit()
            break

        if action_num == '2':
            add(input("请输入需要添加的现有backend编号或新backend名称："), file)
            flag_main = backend_exit()
            break

        if action_num == '3':
            revise(input("请输入需要修改的backend编号或名称："))
            flag_main = backend_exit()
            break

        if action_num == '4':
            delete(input("请输入需要删除的backend编号或名称："))
            flag_main = backend_exit()
            break

        if action_num == '5':
            sys.exit()

        elif action_num not in range(5):    # 当输入不在编号中，提示并重新输入
            print("\033[31;1m输入错误请重新输入！\033[0m")
            flag_main = False