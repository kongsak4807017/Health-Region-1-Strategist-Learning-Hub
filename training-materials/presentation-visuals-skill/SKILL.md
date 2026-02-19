---
name: slide-visuals-curator
description: Curate open-source slide visuals (icons, illustrations, charts) and presentation templates from GitHub; enforce license/attribution; apply a consistent visual system to PPTX/Google Slides/Reveal/Marp decks.
metadata:
  short-description: Curate slide visuals + licenses
---

# Slide Visuals Curator

ใช้สกิลนี้เมื่อผู้ใช้ต้องการ “เพิ่มภาพ/ไอคอน/อินโฟกราฟิก” ให้สไลด์, คัดเลือกแหล่งภาพโอเพนซอร์สจาก GitHub, หรือกำหนดมาตรฐานการใช้ภาพในสไลด์ให้ดูเป็นระบบ

## Quick Start

1. ระบุ “บทบาทของภาพ” ของแต่ละสไลด์: Hero image, icon, diagram, data chart, หรือ process flow
2. เลือกแหล่งภาพจาก `references/repo_catalog.md` ให้ตรงงานและถูกลิขสิทธิ์
3. ตรวจสอบเงื่อนไขลิขสิทธิ์ก่อนใช้ (โดยเฉพาะ CC BY/CC BY-SA)
4. แปลงภาพเป็น `SVG` (ถ้าเป็นไปได้) เพื่อคมชัดเมื่อขยาย
5. ปรับสีให้สอดคล้องกับโทนหลักของคอร์ส
6. บันทึกเครดิตแหล่งภาพตามเทมเพลตใน `references/attribution_template.md`

## Workflow มาตรฐาน

### 1) เลือกประเภทภาพให้ตรงสไลด์
- **Concept/Idea**: ใช้ illustration หรือ icon
- **ตัวเลขหลัก**: ใช้ chart หรือ big number
- **กระบวนการ**: ใช้ diagram หรือ flow
- **เปรียบเทียบ**: ใช้ table + icon

### 2) เลือกแหล่งภาพจาก GitHub
ดูรายการแนะนำใน `references/repo_catalog.md` แยกตามประเภท

### 3) เช็คลิขสิทธิ์
- **CC0**: ใช้ได้โดยไม่ต้องระบุเครดิต (แต่แนะนำให้ให้เครดิต)
- **MIT/ISC/BSD/Apache-2.0**: ใช้ได้เชิงพาณิชย์; ควรเก็บเครดิตและไฟล์ลิขสิทธิ์อ้างอิง
- **CC BY / CC BY-SA**: ต้องระบุเครดิต; ถ้า BY-SA ต้องแชร์งานต่อภายใต้เงื่อนไขเดียวกัน
- **ข้อควรระวัง**: หลีกเลี่ยงชุดภาพที่ห้าม “bulk download / repackage / scraping”

### 4) สร้างความสอดคล้องทางภาพ
- ไอคอนใช้ชุดเดียวทั้งเด็ค
- สีหลัก 1-2 สี + สีเน้น 1 สี
- 1 สไลด์ = 1 ประเด็นภาพ

### 5) บันทึกเครดิต
ใช้ `references/attribution_template.md` เพื่อจดลิขสิทธิ์/แหล่งที่มา

## Output ที่คาดหวัง
- รายการภาพ/ไอคอนที่เลือกต่อสไลด์
- อธิบายเหตุผลการเลือก
- เครดิตภาพครบถ้วนตามลิขสิทธิ์
- สไลด์มีภาพช่วยสื่อสาร ไม่ใช่ตัวหนังสืออย่างเดียว

## เมื่อไรควรโหลดไฟล์อ้างอิงเพิ่มเติม
- ต้องการรายการแหล่งภาพ/ไอคอน/เทมเพลต -> เปิด `references/repo_catalog.md`
- ต้องการฟอร์มเครดิต -> เปิด `references/attribution_template.md`
