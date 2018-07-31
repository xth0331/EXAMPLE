def select(arg):
    server_list = []
    flag = "Backend"
    with open("haproxy.cfg", "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line == "backend %s" % arg:
                flag = "Server"
                continue
            if line.startswith("backend"):
                flag = "Backend"
            if flag == "Server":
                server_list.append(line)
    return server_list


def edit(type, old_backends, new_backends):
    with open("haproxy.cfg", "r", encoding="utf-8") as old, open("haproxy.cfg.bak", 'w', encoding="utf-8") as new:
        for oldline in old:
            if oldline.strip() == '%s %s' %(type,old_backends):
                oldline = oldline.replace(old_backends, new_backends)
                new.write(oldline)
            else:
                new.write(oldline)



