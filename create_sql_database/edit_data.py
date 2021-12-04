import os

names_of_files = os.listdir(r"database food")[22:]

for name in names_of_files:

    with open(os.path.join(r"database food", name), "r", encoding="utf-8") as out_file, \
            open(os.path.join(r"database food e", name), "w") as input_file:

        data = out_file.readlines()
        data = list(map(lambda x: x.split("\t"), data))

        for elem in range(len(data)):

            data[elem][-1] = data[elem][-1].strip()
            try:
                if data[elem][0] == data[elem][1]:
                    del data[elem][0]
            except IndexError:
                print(elem)

            if len(data[elem]) <= 2:
                del data[elem]

        for elem in data:
            try:
                print(*elem, sep='\t', end='\n', file=input_file)
            except UnicodeEncodeError:
                continue

