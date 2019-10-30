actor_backup = open("C:/Users/Matthew/Documents/db_ass3/worked_as_orig.txt", "r")
actor_restore = open("C:/Users/Matthew/Documents/db_ass3/worked_as_insert.txt", "w+")

actor_insert_lines = actor_backup.readlines()

for line in actor_insert_lines:
    txt = line.split("\t")
    txt[1] = txt[1].rstrip("\r\n")
    #txt[5] = txt[5].rstrip(" ")
    #txt[4] = txt[4].rstrip(" ")
    #txt[1] = txt[1].replace("'", "''")
    newLine = "insert into public.worked_as values (" + "'" + txt[0] + "'" + ", "+ "'" + txt[1] + "'"");\n"

    newLine = newLine.replace("'\\N'", "null")
    actor_restore.write(newLine)


actor_backup.close()
actor_restore.close()
