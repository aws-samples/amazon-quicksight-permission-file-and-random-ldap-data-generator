# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import csv
import os

def create_permissions_file(list_of_emp_ids, number_of_levels):
    print("Creating permissions file")
    output_header=["ceo_" + str(i) if i!=0 else 'ceo' for i in range(number_of_levels)]
    output_header.insert(0,'UserName')
    f=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "sample_permissions_file.csv"), 'w')
    writer = csv.writer(f)
    writer.writerow(output_header)
    for i in list_of_emp_ids:
        for j in range(1,len(output_header)):
            l = [None] * (len(output_header))
            l[j]=i
            l[0]=i
            writer.writerow(l)
    f.close()
    print("Finished creating permissions file")

if __name__ == '__main__':
    # Test with 200 emp
    create_permissions_file(list(range(200)), 11)