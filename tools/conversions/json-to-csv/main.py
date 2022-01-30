import pandas as pd
import os
import json
import copy

JSON_DIR = '../../../source/json/'
CSV_DIR = '../../../source/csv/'

def getjsondata(filename):
    ob = json.loads(filename)
    ob_copy = copy.copy(ob)
    for k, v in ob_copy.items():
        if isinstance(v, list):
            ob[k] = ','.join(v)
        elif isinstance(v, dict):
            for kk, vv in v.items():
                ob['%s_%s' % (k, kk)] = vv
            del ob[k]
    return ob
    

if __name__ == '__main__':
    for file in os.listdir(JSON_DIR):
        json_filename = os.fsdecode(file)
        csv_filename = '%s.csv' % json_filename[:-5]
        json_file = JSON_DIR+json_filename
        csv_file = CSV_DIR+csv_filename

        print("converting "+json_filename)
        df = pd.DataFrame([getjsondata(line) for line in open(json_file)])
        
        filePath = '/home/somedir/Documents/python/logs';
        # As file at csv_file is deleted now, so we should check if file exists or not not before deleting them
        if os.path.exists(csv_file):
            os.remove(csv_file)
        else:
            print("Can not delete the file as it doesn't exists")
        df.to_csv(csv_file, index=False)
        
        print("done converting"+csv_filename)