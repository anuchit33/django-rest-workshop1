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
- Params: [username,email,first_name,is_active,group,page,page_size]
- Body: []
- Response: {
  results:[],count: (int),next: (String),previous: (String)}
- Status Code: [200-ดึงข้อมูลได้สำเร็จ,403-FORBIDDEN]
- AC:
  - สร้างกลุ่มผู้ใช้มีดัง (admin,user,customer)
  - จำลองข้อมูลผู้ใช้งานมา 20คน เป็น admin 1คน user 4คน customer 15คน
  - Generic views: ดึงรายกผู้ใช้งาน 
  - Serializers : ข้อมูลแต่ละ item ต้องมีดังนี้ (id,username,first_name,email,groups)
  - Permissions: ผู้ใช้งานต้องมี Session เข้าสู่ระบบ 
  - Pagination: ต้องสามารถดึงรายชื่อผู้ใช้งานได้ โดยดึงข้อมูล page ละ 5itemได้
  - Filtering : สามารถ Search ด้วย (username,email,first_name) แบบ contains
  - Filtering: สามารถ Filtering ด้วย (is_active,group)
  - Filtering : สามารถ OrderingFilter (ASC,ESC) ดังนี้ (id,username,email)

 ===========================

2. API /users/{id}/
- Method: GET
- Params: []
- Body: []
- Response: {'id', 'username', 'email', 'groups','first_name'}
- Status Code: [200-ดึงข้อมูลได้สำเร็จ,403-FORBIDDEN]
- AC:
  - Generic views: ดึงข้อมูลผู้ใช้งานโดย user id
  - Serializers : (id,username,first_name,email,groups,date_joined,last_name)
  - Permissions: ผู้ใช้งานต้องมี Session เข้าสู่ระบบ

 ===========================

3. API /shop
- Method: GET
- Params: [name,email,phone,category,status,is_active,category,page,page_size]
- Body: []
- Response: {}
- Status Code: [200-ดึงข้อมูลได้สำเร็จ,401-UNAUTHORIZED,403-FORBIDDEN]
- AC:
  - สร้าง Model Category ประกอบไปด้วยรายการหมวดหมู่ดังนี้ เสื้อผ้า,รองเท้า,กระเป๋า
  - สร้าง Model Shop (id,name,detail,email,phone,category,status(เปิด,ปิด),is_active)
  - จำลองข้อมูลผู้ร้านค้ามา 15ร้าน แบ่งเป็นแต่ละหมวด 15ร้าน
  - Generic views: ดึงรายร้านค้า
  - Serializers : ข้อมูลแต่ละ item ต้องมีดังนี้ (id,name,email,phone,category_id,status,status_display)
  - Permissions: ผู้ใช้งานต้องเป็น Admin เท่านั้น
  - Pagination: ต้องสามารถดึงรายชื่อผู้ใช้งานได้ โดยดึงข้อมูล page ละ 10itemได้
  - Filtering : สามารถ Search ด้วย (name,email) แบบ contains
  - Filtering: สามารถ Filtering ด้วย (is_active,status,category_id)
  - Filtering : สามารถ OrderingFilter (ASC,ESC) ดังนี้ (id,name,email,phone,is_active)

 ===========================

 4. API /shop/{id}/
- Method: GET
- Params: []
- Body: []
- Response: {}
- Status Code: [200-ดึงข้อมูลได้สำเร็จ,401-UNAUTHORIZED,403-FORBIDDEN]
- AC:
  - Generic views: ดึงข้อมูลร้านค้าโดย shop id
  - Serializers : ข้อมูลแต่ละ item ต้องมีดังนี้ (id,name,email,phone,category(id,name),status,status_display,is_active)
  - Permissions: ผู้ใช้งานต้องเป็น Admin เท่านั้น

 ===========================