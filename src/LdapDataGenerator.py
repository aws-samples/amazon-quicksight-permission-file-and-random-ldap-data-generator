# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import os
import datetime
import random
import pandas as pd
from treelib import Tree

class LdapDataGenerator():


    def __init__(self, number_of_employees=200):
        self.number_of_employees = number_of_employees
        self.data={}
        for subdir, dirs, files in os.walk(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'input')):
            for file in files:
                filepath = subdir + os.sep + file
                print("reading %s" % file)
                self.data[file.replace(".txt","").replace("-","_")] = open(filepath,"r").read().split('\n')


    def random_dob(self):
        start_date = datetime.datetime.today() - datetime.timedelta(25000)
        end_date = datetime.datetime.today() - datetime.timedelta(7665)
        time_between_dates = end_date - start_date
        random_number_of_days = random.randrange(time_between_dates.days)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date.date()


    def random_name(self):
        if random.choice([True, False]):
            return self.data['surnames'][random.randrange(0, len(self.data['surnames']), 1)] +", "+ self.data['givennames_f'][random.randrange(0, len(self.data['givennames_f']), 1)]
        else:
            return self.data['surnames'][random.randrange(0, len(self.data['surnames']), 1)] +", "+  self.data['givennames_m'][random.randrange(0, len(self.data['givennames_m']), 1)]


    def random_department(self):
        return self.data['structnames'][random.randrange(0, len(self.data['structnames']), 1)]


    def generate_data(self):
        tree = Tree()
        df = pd.DataFrame(columns=['Employee_id','Manager_id','name', 'dob','dept'])

        for emp_id in range(self.number_of_employees):
            if emp_id >1:
                Manager_id=random.randrange(0, emp_id-1, 1)
                tree.create_node(emp_id,emp_id, parent=Manager_id)
                df = df.append({'Employee_id': int(emp_id), 
                                'Manager_id':int(Manager_id),
                                'name':self.random_name(),
                                'dob':self.random_dob(),
                                'dept':self.random_department()
                            }, ignore_index=True)
            elif emp_id==1:
                tree.create_node(emp_id,emp_id, parent=0)
                df = df.append({'Employee_id': int(emp_id), 
                                'Manager_id':int(0),
                                'name':self.random_name(),
                                'dob':self.random_dob(),
                                'dept':self.random_department()
                            }, ignore_index=True)
            else:
                tree.create_node(emp_id,emp_id)
                df = df.append({'Employee_id': int(emp_id), 
                                'Manager_id':None,
                                'name':self.random_name(),
                                'dob':self.random_dob(),
                                'dept':None
                            }, ignore_index=True)
        return tree, df


    def main(self):
        print("Generating random LDAP data")
        tree, df = self.generate_data()
        print("Depth of the tree is : %s " % tree.depth())
        print(tree.show(line_type="ascii-em"))
        print("Sample employee data :: ")
        df.head(20)
        df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'sample_ldap_data.csv'))
        tree.save2file(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'tree.txt'))
        leaves=[]
        for i in tree.leaves():
            leaves.append(i.tag)
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'leaves.txt'), "w") as output:
            output.write(str(leaves))
        print("Finished generating random LDAP data")


if __name__ == '__main__':
    ldapDataGeneratorObj = LdapDataGenerator()
    ldapDataGeneratorObj.main()