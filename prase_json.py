import json
import csv
#从文件输入json数据
with open('data.json', 'r') as f:
    input = f.read()
# 读取json数据
data = json.loads(input)
# 读取json数据中的data
data = data['data']
# 写入CSV文件的表头
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['活动名称', '活动状态', '学期', '活动积分', '结束时间', '开始时间', '活动ID'])

# 循环读取data中的每一条数据,并输出到CSV文件中
for item in data:
    if item is None:
        continue
    name = item['activityName']
    activityStatus = item['activityStatus']
    if activityStatus == '0':
        activityStatus = '报名中'
    elif activityStatus == '1':
        activityStatus = '待开始'
    elif activityStatus == '2':
        activityStatus = '进行中'
    elif activityStatus == '3':
        activityStatus = '待完结'
    elif activityStatus == '4':
        activityStatus = '完结审核中'
    elif activityStatus == '5':
        activityStatus = '已完结'
    else:
        activityStatus = '未知'

    activityId = item['id']
    semester = item['semester']
    activityIntegral = item['activityIntegral']
    endTime = item['endTime']
    startTime = item['startTime']
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([name, activityStatus, semester, activityIntegral, endTime, startTime, activityId])

