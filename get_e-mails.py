import json
import pickle
import auth


def get_emails(f):
    result = []

    for line in f.read().split("\n"):  # go from all lines in file (in fact we have only 1 line)
        if line == "":  # if empty line
            continue
        st = line
        parsed_json = json.loads(st)  # parse by json
        c = 0
        for v in parsed_json['rows']:  # go by all records in DB
            if len(v['cell'][7]) != 8 or True:  # go by all records in DB
            # remove True in order to go only by changed passwords
                res = dict()  # new record
                res["fio"] = v['cell'][8]  # save fio
                res["pas"] = v['cell'][7]  # save password
                res["login"] = v['cell'][6]  # save login
                res["e-mail"] = auth.main(v['cell'][6], v['cell'][7].encode('utf-8'))  # extract e-mail
                print(res["e-mail"])
                # '.encode' because of russian passwords
                result.append(res)  # save result in 'result'
                c += 1
            if c > 3:
                break
    return result


def main():
    f = open("DB.txt", "r")  # open file

    result = get_emails(f)  # extract e-mails

    with open("new_DB.txt", 'wb') as ff:
        pickle.dump(result, ff)  # save data in file

main()