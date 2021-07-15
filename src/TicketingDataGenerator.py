# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

import sys
import os
import csv 
import json
import datetime
import random
import pandas as pd


class TicketingDataGenerator():

    def __init__(self, num_of_tickets=50):
        self.num_of_tickets=num_of_tickets
        f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "leaves.txt"))
        self.leaves = f.read().replace(" ","").split(",")

    def random_date(self, num_days=500):
        return (datetime.datetime.now() - datetime.timedelta(days=random.randrange(0, num_days, 1))).date()

    def random_status(self):
        return random.choice(["In Progress","Assigned", "In Review", "Closed", "Reassigned", "Pending"])

    def random_category(self):
        return random.choice(["Security", "Payment", "Order", "Retail", "Internal", "Human Resources", "IT", "Finance", "Training", "CTO", "Web", "Billing","CRM", "CS", "BI"])

    def random_FiledAgainst(self):
        return random.choice(["Software","Access/Login","Systems","Hardware"])

    def main(self):
        df = pd.DataFrame(columns=['ticket_num','assigned_to_emp_id','category', 'status',
                                'creation_date','requestor','FiledAgainst','TicketType',
                                'Severity','Priority'])
        for ticket_num in range(self.num_of_tickets):
            df = df.append({'ticket_num': "TICKET-"+str(ticket_num), 
                                'assigned_to_emp_id':self.leaves[random.randrange(0, len(self.leaves), 1)],
                                'category':self.random_category(),
                                'status':self.random_status(),
                                'creation_date':self.random_date(),
                                'requestor':self.leaves[random.randrange(0, len(self.leaves), 1)],
                            'FiledAgainst':self.random_FiledAgainst(),
                            'TicketType':random.choice(["Issue","Request"]),
                            'Severity':random.choice(["0 - Unclassified","1 - Minor","2 - Normal","3 - Major","4 - Critical"]),
                            'Priority':random.choice(["0 - Unassigned","1 - Low","2 - Medium","3 - High"])
                            }, ignore_index=True)

        df.to_csv(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "ticketing.csv"))

if __name__ == '__main__':
    ticketingDataGeneratorObj = TicketingDataGenerator(num_of_tickets=50)
    ticketingDataGeneratorObj.main()