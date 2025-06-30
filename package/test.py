from uavcan.diagnostic import Severity_1_0



record = Severity_1_0()
record.value = 4
print(record)
out = record.__serialize__()
print(out)
print(record.value)


record2 = Severity_1_0.__deserialize__(out)
print(record2.value)
print(record2)
