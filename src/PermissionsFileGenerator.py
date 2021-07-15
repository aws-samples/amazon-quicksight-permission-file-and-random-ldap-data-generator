# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import csv
import os

class PermissionsFileGenerator():

    def __init__(self, list_of_emp_ids, number_of_levels):
        self.list_of_emp_ids = list_of_emp_ids
        self.number_of_levels = number_of_levels

    def create_permissions_file(self):
        print("Creating permissions file")
        output_header=["ceo_" + str(i) if i!=0 else 'ceo' for i in range(self.number_of_levels)]
        output_header.insert(0,'UserName')
        f=open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "sample_permissions_file.csv"), 'w')
        writer = csv.writer(f)
        writer.writerow(output_header)
        for i in self.list_of_emp_ids:
            for j in range(1,len(output_header)):
                l = [None] * (len(output_header))
                l[j]=i
                l[0]=i
                writer.writerow(l)
        f.close()
        print("Finished creating permissions file")

if __name__ == '__main__':
    # Test with 200 emp
    permissionsFileGeneratorObj = PermissionsFileGenerator(list(range(200)), 11)
    permissionsFileGeneratorObj.create_permissions_file()