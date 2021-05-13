import pickle


# import pandas as pd
# import numpy as np

def dumpchk(jobdict, location, logger):
    with open(location + '/jobs.pkl', 'wb') as f:
        pickle.dump(jobdict, f)
    # logger.info("=====Updated Checkpoint=====")
    return None


def readchk(location):
    flag = 0
    try:
        with open(location + '/jobs.pkl', 'rb') as f:
            x = pickle.load(f)
        for k in x.keys():
            if x[k] is not None:
                flag = 1
    except:
        flag = 0

    if flag == 1:
        return x
    if flag == 0:
        return None


def updtchk(jobdict, toremove, val, logger, location):
    if toremove == 'gamma':
        jobdict.pop(val)
    if toremove == 'ori':
        for i in jobdict.keys():
            for j in jobdict[i]:
                if j.name == val:
                    jobdict[i].remove(j)
    logger.info("==========Updated Checkpoint: {}==========".format(val))
    dumpchk(jobdict, location, logger)
    return jobdict
