import json
import os
import hashlib

blockchain_dir = os.curdir + "/blocks/"


def get_hash(filename):
    # возвращает хэш файла
    file= open(blockchain_dir + filename, 'rb').read()
    return hashlib.md5(file).hexdigest()


def get_files():
    # возвращает список файлов в директории
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])


def check_integrity():
    # считать хэш предыдушего блока
    # вычислить хэш предыдущего блока
    # сравнить их
    files = get_files()
    results = []

    for file in files[3:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']
        prev_file = str(file - 1)
        actual_file = get_hash(prev_file)
        res = 'Ok' if h == actual_file else 'Corrupted'
        results.append({'block':prev_file, 'result': res})
        f.close()
    if len(files) > 2:
        last_file = str(files[-1])
        h1 = get_hash(last_file)
        secret_file = open(blockchain_dir + "-1")
        h2 = json.load(secret_file)['hash']
        res = 'Ok' if h1 == h2 else 'Corrupted'
        results.append({'block':str(files[-1]), 'result': res})
        secret_file.close()
    return results


def write_block(name, amount, receiver):
    # добавление нового блока
    files = get_files()
    last_file = files[-1]
    filename = str(last_file + 1)
    prev_hash = get_hash(str(last_file))

    data = {'name': name, 'amount':amount, 'receiver':receiver, 'hash':prev_hash}
    # сохраняем блок
    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    # сохраняем хэш нового блока в файл -1
    with open(blockchain_dir + str("-1"), 'w') as file2:
        d = {'hash': get_hash(filename)}
        json.dump(d, file2, indent=1, ensure_ascii=False)


def main():
    pass


if __name__ == '__main__':
    main()


