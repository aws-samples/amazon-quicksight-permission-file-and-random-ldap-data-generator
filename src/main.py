# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from LdapDataGenerator import LdapDataGenerator
from TicketingDataGenerator import TicketingDataGenerator
from create_permissions_file import create_permissions_file

number_of_employees = 200
number_of_levels = 11
num_of_tickets = 50

ldapGeneratorObj = LdapDataGenerator()
ldapGeneratorObj.main()

create_permissions_file(list(range(number_of_employees)), number_of_levels)

ticketingDataGeneratorObj = TicketingDataGenerator(num_of_tickets=num_of_tickets)
ticketingDataGeneratorObj.main()