
'''

Created on 

@author: Raja CSP Raman

source:
    
'''

FILEPATH = 'metrics_result_1.txt'

dict_parts = {
    0 : 'entity',
    1 : 'p',
    2 : 'r',
    3 : 'f1',
    4 : 'tp',
    5 : 'fp',
    6 : 'fn'
}

def set_dict(r_dict, parts):

    # print(f'parts : {parts}')

    for idx, val in enumerate(parts):

        if(idx in [1, 2, 3]):
            r_dict[dict_parts[idx]] = float(val)
        else:
            r_dict[dict_parts[idx]] = val

    return r_dict

def get_metrics_from_text(filepath):

    overall_metric_dict = {

    }

    with open(filepath) as fp:
        for idx, line in enumerate(fp):

            if(idx == 0):
                continue

            line = line.replace('\n', '').strip()

            if(len(line) <= 0):
                continue

            # print(f'[{line}]')

            parts = line.split('\t')
            # print(len(parts))
            r_dict = {
                'entity' : 0,
                'p' : 1,
                'r' : 2,
                'f1' : 3,
                'tp' : 4,
                'fp' : 5,
                'fn' : 2
            }

            r_dict = set_dict(r_dict, parts)

            # print(line)

            overall_metric_dict[r_dict['entity']]  = r_dict

            # print(r_dict)
            

    total_metric = overall_metric_dict['Totals']

    return overall_metric_dict, total_metric

def startpy():

    final_metric, total_metric = get_metrics_from_text(FILEPATH)
    print(total_metric)

if __name__ == '__main__':
    startpy()