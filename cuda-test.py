import torch
print(torch.cuda.is_available())       # ควรได้ True
print(torch.version.cuda)
print(torch.cuda.device_count())       # จำนวน GPU ที่ตรวจพบ
print(torch.cuda.get_device_name(0))   # ชื่อการ์ดจอ