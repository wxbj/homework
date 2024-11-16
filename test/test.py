mttf_component = 360
failure_rate_component = 1 / mttf_component
num_components = 2700
failure_rate_system = num_components * failure_rate_component

# 整个系统的MTTF（平均无故障时间），单位：天
mttf_system = 1 / failure_rate_system
print("%0.1f" % mttf_system)
