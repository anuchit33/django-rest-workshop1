# django-rest-workshop1

## Keyword
- Model
- APIViews
- Generic views
- Serializers , Serializer fields,Serializer relations
- Validators
- Authentication
- Permissions
- Filtering
- Pagination
- Format suffixes
- Exceptions
- Status Codes

## Topic 
1. API /users
- Method: GET
- Params: [username,email,first_name]
- Body: []
- Response: {}
- Status Code: [200-ดึงข้อมูลได้สำเร็จ,401-UNAUTHORIZED]
- AC:
  - สร้างกลุ่มผู้ใช้มีดัง (admin,user,customer)
  - จำลองข้อมูลผู้ใช้งานมา 20คน เป็น admin 1คน user 4คน customer 15คน
  - ต้องสามารถดึงรายชื่อผู้ใช้งานได้ โดยดึงข้อมูล page ละ 5itemได้
  - สามารถ filter ด้วย (username,email,first_name) แบบ contains
  - ข้อมูลแต่ละ item ต้องมีดังนี้ (id,username,first_name,email,groups)

 ===========================