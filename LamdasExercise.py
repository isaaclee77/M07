import csv
from functools import reduce
import json

csvf = open("911_Calls_for_Service_(Last_30_Days).csv")
reader = csv.DictReader(csvf)

filtered_list = list(filter(lambda row: row["zip_code"] != "" and row["neighborhood"] != "" and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "", reader))

TotalResponse = reduce(lambda time1, time2: time1 + float(time2["totalresponsetime"]), filtered_list, 0)
average_response_time = TotalResponse / len(filtered_list)
print(f"Average total response time: {average_response_time}")

total_dispatch_time = reduce(lambda t1, t2: t1 + float(t2["dispatchtime"]), filtered_list, 0)
avg_dispatch_time = total_dispatch_time / len(filtered_list)
print(f"Average dispatch time: {avg_dispatch_time}")

tot_time = reduce(lambda t1, t2: t1 + float(t2["totaltime"]), filtered_list, 0)
avg_total_time = tot_time / len(filtered_list)
print(f"Average total time: {avg_total_time}")