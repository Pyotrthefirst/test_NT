import sys
import json

def make_report(test, values):
    if test['id'] in values:
        test['value']=values[test['id']]

    if 'values' in test:
        for sub_test in test['values']:
            make_report(sub_test, values)


values_path = sys.argv[1]
tests_path = sys.argv[2]
report_path = sys.argv[3]


with open(values_path, 'r', encoding='utf-8') as f:
    values_data = json.load(f)

with open(tests_path, 'r', encoding='utf-8') as f:
    tests_data = json.load(f)

values_dict={item['id']: item['value'] for item in values_data['values']}
for test in tests_data['tests']:
    make_report(test, values_dict)

with open(report_path, 'w', encoding='utf-8') as f:
    json.dump(tests_data, f, indent=2)