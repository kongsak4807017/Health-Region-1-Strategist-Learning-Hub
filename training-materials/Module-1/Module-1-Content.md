# Module 1: การจัดการข้อมูลสุขภาพ (Data Management)

เอกสารฉบับนี้ขยายรายละเอียดเนื้อหาตามหัวข้อใน `README.md` ของโมดูล 1 เพื่อใช้เป็นคู่มือการสอนแบบลงลึก (Teaching Notes) และเป็นแนวทางเตรียมกิจกรรม

---

## หัวข้อการสอน

### 1.1 แหล่งข้อมูลสุขภาพไทย (3 ชั่วโมง)

**วัตถุประสงค์การเรียนรู้**
- รู้จักแหล่งข้อมูลสุขภาพไทยหลักและข้อจำกัดของแต่ละแหล่ง
- เลือกแหล่งข้อมูลให้สอดคล้องกับคำถามเชิงนโยบายและระดับการวิเคราะห์
- แยกแยะข้อมูลภาครัฐ ข้อมูลวิจัย และข้อมูลระหว่างประเทศได้อย่างเป็นระบบ

**โครงสร้างเนื้อหา**
- ภาพรวมระบบข้อมูลสุขภาพไทยและเหตุผลที่ต้องใช้หลายแหล่ง (triangulation)
- แหล่งข้อมูลภาครัฐที่สำคัญ
- แหล่งข้อมูลระหว่างประเทศ
- ข้อมูลเปิดภาครัฐและการขอข้อมูลเพิ่มเติม (FOI)
- ตารางสรุปการเลือกใช้แหล่งข้อมูลตามประเด็น

**สาระสำคัญเชิงปฏิบัติ**
- แหล่งข้อมูลภาครัฐหลัก ได้แก่ MOPH, NHSO, NSO, DDC, HSRI, IHPP
- MOPH ให้ข้อมูลด้านสถิติสาธารณสุขและ HDC ซึ่งมี 43 แฟ้มข้อมูลมาตรฐาน
- NHSO ให้ข้อมูล claims และตัวชี้วัด QOF ที่ใช้ประเมินคุณภาพบริการ
- NSO ให้ข้อมูลสำรวจพฤติกรรมสุขภาพและ SES เพื่อเชื่อมมิติสังคมเศรษฐกิจ
- WHO และ World Bank ใช้เพื่อเปรียบเทียบระหว่างประเทศและ benchmark
- BOD Thailand ใช้เพื่อตีความภาระโรคเชิงระบบ (DALYs, YLLs, YLDs)

**ตัวอย่างการเลือกแหล่งข้อมูลตามคำถาม**
- อัตราตายมารดา: MOPH Death Registry เป็นแหล่งหลัก และ cross-validate กับ WHO
- การเข้าถึงบริการตามสิทธิ: NHSO Claims เป็นแหล่งหลัก และเทียบกับ MOPH
- พฤติกรรมเสี่ยง: NSO Survey เป็นแหล่งหลัก และเทียบกับ DDC

**จุดที่ต้องเน้นในการสอน**
- นิยามตัวแปรในแต่ละแหล่งอาจไม่เหมือนกัน ให้ชี้ให้เห็นด้วยตัวอย่างจริง
- ความล่าช้าของข้อมูลและผลกระทบต่อการตัดสินใจ
- การอ่าน metadata และการใช้ data dictionary เพื่อป้องกันการตีความผิด

**สื่อแนะนำ**
- ใช้ `M1-Handout-Data-Sources.md` เป็นเนื้อหาหลัก
- ใช้ case study ใน `M1-Case-Thai-Health-Data.md` เพื่ออภิปรายการเลือกข้อมูล

---

### 1.1 Slide Deck (20-26 slides) สำหรับหัวข้อ “แหล่งข้อมูลสุขภาพไทย”

Slide 1 — Title
Goal: เปิดบทเรียนและตั้งกรอบว่า “แหล่งข้อมูล” คือฐานของการวิเคราะห์นโยบาย
Key points: ชื่อหัวข้อ, ภาพรวม 3 กลุ่มข้อมูล (รัฐ, วิจัย, ระหว่างประเทศ)
Visual: แผนที่ประเทศไทย + ไอคอนหน่วยงานหลัก

Slide 2 — Learning Objectives
Goal: ระบุผลลัพธ์การเรียนรู้ใน 1 ชั่วโมง
Key points: ระบุแหล่งข้อมูลหลัก, เลือกแหล่งให้ตรงคำถาม, เข้าใจข้อจำกัดข้อมูล
Visual: กล่อง 3 เป้าหมาย

Slide 3 — ทำไมต้อง “เลือกแหล่งข้อมูล” ให้ถูก
Goal: เชื่อมโยงการเลือกแหล่งข้อมูลกับคุณภาพการตัดสินใจ
Key points: แหล่งต่างกันให้ตัวเลขต่างกัน, การเลือกผิดทำให้ข้อเสนอแนะผิด
Visual: ตัวเลขจาก 2 แหล่งที่ไม่เท่ากัน

Slide 4 — แผนที่ระบบข้อมูลสุขภาพไทย (Data Ecosystem Map)
Goal: เห็นภาพรวมหน่วยงานและบทบาท
Key points: MOPH/NSO/NHSO/DDC/HSRI-IHPP/ข้อมูลเปิด/ข้อมูลระหว่างประเทศ
Visual: Ecosystem map แบบ hub-and-spoke

Slide 5 — MOPH Public Health Statistics
Goal: แหล่งสถิติสรุปภาพรวมสุขภาพประเทศรายปี
Key points: เป็นเอกสารสถิติสุขภาพที่จัดทำเป็นรายปี; ใช้เป็นฐานการอ้างอิงภาพรวม
Visual: หน้าปกสถิติสาธารณสุข + ตารางตัวอย่าง
Source: `https://planning.anamai.moph.go.th/th/public-health-statistics`

Slide 6 — MOPH Standard 43 Files (โครงสร้างมาตรฐานข้อมูลสุขภาพ)
Goal: เข้าใจฐานข้อมูลมาตรฐานของหน่วยบริการ
Key points: 43 แฟ้มเป็นมาตรฐานข้อมูลสุขภาพที่หน่วยบริการต้องส่ง; เชื่อมกับ HDC
Visual: Diagram “หน่วยบริการ -> 43 แฟ้ม -> HDC”
Source: `https://healthkpi.moph.go.th/kpi2/kpi/index/?id=3240`

Slide 7 — HDC (Health Data Center)
Goal: ทำความเข้าใจ “คลังข้อมูลกลาง” ของระบบสุขภาพ
Key points: HDC เป็นคลังข้อมูลการแพทย์และสุขภาพที่รองรับการส่งข้อมูล 43 แฟ้ม
Visual: สถาปัตยกรรมชั้นจังหวัด-เขต-ส่วนกลาง (conceptual)
Source: `https://healthkpi.moph.go.th/kpi2/kpi/index/?id=3240`

Slide 8 — NHSO Dashboard และ Claims Data (UCS)
Goal: แหล่งข้อมูลการใช้บริการและค่าใช้จ่ายของสิทธิหลักประกันสุขภาพถ้วนหน้า
Key points: ข้อมูลมาจากระบบเบิกจ่ายและพอร์ทัล MOPH; ครอบคลุมประชากรจำนวนมาก
Visual: Screenshot dashboard + ไอคอน OPD/IPD
Source: `https://eng.nhso.go.th/nhso-Dashboard/`

Slide 9 — ทำไม NHSO สำคัญต่อการวิเคราะห์นโยบาย
Goal: อธิบายคุณค่าของ claims data
Key points: เหมาะสำหรับวิเคราะห์การใช้บริการ/ค่าใช้จ่าย/coverage แต่มีข้อจำกัดเฉพาะสิทธิ UCS
Visual: “Use case” 3 กล่อง

Slide 10 — DDC Disease Surveillance (R506)
Goal: แหล่งข้อมูลเฝ้าระวังโรคติดต่อ
Key points: DDC มีระบบรายงานโรคติดต่อ (R506) ในแพลตฟอร์ม Digital Disease Surveillance
Visual: ไทม์ไลน์รายงานรายวัน/รายสัปดาห์
Source: `https://ddc.moph.go.th/dsc/`

Slide 11 — ใช้ข้อมูล DDC อย่างไร
Goal: การใช้ข้อมูลเฝ้าระวังเพื่อการตัดสินใจเชิงนโยบาย
Key points: เหมาะกับ early warning, outbreak response, และการประเมิน trend โรค
Visual: กราฟ epidemic curve (ตัวอย่าง)

Slide 12 — NSO Health Behavior Survey
Goal: แหล่งข้อมูลพฤติกรรมสุขภาพระดับประชากร
Key points: NSO มีการสำรวจพฤติกรรมด้านสุขภาพและการสูบบุหรี่/ดื่มสุรา
Visual: แผนภาพ survey -> indicator
Source: `https://www.nso.go.th/nsoweb/nso/statistics_and_indicators`

Slide 13 — NSO Health & Welfare Survey
Goal: ข้อมูลสุขภาพเชิงสังคมเศรษฐกิจและสวัสดิการ
Key points: ใช้เชื่อมมิติพฤติกรรม/การเข้าถึงบริการกับฐานะครัวเรือน
Visual: ตัวอย่างตารางตัวแปรจากแบบสำรวจ
Source: `https://www.nso.go.th/nsoweb/nso/statistics_and_indicators`

Slide 14 — ThaiHealthStat / HISO (HSRI)
Goal: แหล่งรวมข้อมูลสุขภาพเชิงประเด็นและดัชนีสุขภาพ
Key points: ThaiHealthStat รวบรวมข้อมูลสุขภาพจากหลายแหล่งภายในและระหว่างประเทศ
Visual: หน้าเว็บ ThaiHealthStat + ไอคอนหลายแหล่งข้อมูล
Source: `https://www.hiso.or.th/hiso/`

Slide 15 — IHPP National Health Accounts (NHA)
Goal: ข้อมูลการเงินสุขภาพระดับประเทศ
Key points: NHA ใช้กรอบบัญชีสุขภาพสากลและติดตามการใช้จ่ายด้านสุขภาพ
Visual: Sankey ของกระแสเงินสุขภาพ
Source: `https://www.ihppthaigov.net/health_service/national-health-accounts/`

Slide 16 — BOD Thailand (DALYs, YLLs, YLDs)
Goal: แหล่งข้อมูลภาระโรคเพื่อจัดลำดับความสำคัญ
Key points: ให้ข้อมูล DALYs/YLLs/YLDs เพื่อเทียบภาระโรคและแนวโน้ม
Visual: ภาพ stack bar DALYs ตามกลุ่มโรค
Source: `https://bodthai.net/en/`

Slide 17 — WHO Global Health Observatory (GHO)
Goal: ใช้ข้อมูลมาตรฐานสากลเปรียบเทียบข้ามประเทศ
Key points: GHO รวมตัวชี้วัดสุขภาพระดับโลกและข้อมูล SDGs
Visual: แผนที่โลก + ตัวชี้วัดหลัก
Source: `https://www.who.int/data/gho`

Slide 18 — World Bank Data (WDI)
Goal: ข้อมูลเศรษฐกิจและสุขภาพสำหรับการเทียบประเทศ
Key points: ใช้ตัวชี้วัดด้านเศรษฐกิจ-สุขภาพ เช่น health expenditure, life expectancy
Visual: กราฟเส้นเทียบประเทศ
Source: `https://data.worldbank.org/indicator`

Slide 19 — Open Government Data (Data.go.th)
Goal: แหล่งข้อมูลเปิดของภาครัฐ
Key points: Data.go.th เป็นแพลตฟอร์มข้อมูลเปิดของรัฐและมีนิยาม Open Data ที่ชัดเจน
Visual: Screenshot portal + ไอคอน download
Source: `https://www.dga.or.th/our-services/one-stop-service/open-government-data/`

Slide 20 — Government Data Catalog (GDCatalog)
Goal: ค้นหา metadata ของชุดข้อมูลภาครัฐ
Key points: GDCatalog เป็นระบบจัดการบัญชีข้อมูลภาครัฐและ metadata กลาง
Visual: Diagram “หน่วยงาน -> metadata -> GDCatalog”
Source: `https://gdhelppage.gdcatalog.go.th/gdcatalog/`

Slide 21 — การเข้าถึงข้อมูลที่ไม่เปิดเผย (FOI)
Goal: รู้ช่องทางขอข้อมูลที่ไม่ได้เปิด
Key points: ใช้ พ.ร.บ.ข้อมูลข่าวสารของราชการ ผ่านช่องทางของ OIC
Visual: Flow “คำร้อง -> หน่วยงาน -> การพิจารณา”
Source: `https://www.oic.go.th/WEB2017/eng/40/`

Slide 22 — Checklist การเลือกแหล่งข้อมูล
Goal: สรุปเกณฑ์การคัดเลือกแหล่งข้อมูลให้ผู้เรียนใช้ได้จริง
Key points: Coverage, Granularity, Timeliness, Access, Cost, Comparability
Visual: Checklist 6 ช่อง

Slide 23 — ตัวอย่าง Mapping คำถามกับแหล่งข้อมูล
Goal: ให้ผู้เรียนเห็นการใช้หลายแหล่งร่วมกัน
Key points: ใช้ MOPH + NHSO + NSO + WHO ในโจทย์เดียวเพื่อ triangulation
Visual: ตาราง 3 คอลัมน์ (คำถาม -> ตัวแปร -> แหล่ง)

Slide 24 — สรุปและเชื่อมโยงไปหัวข้อถัดไป
Goal: ปิดบทเรียนและปูไปสู่การค้นหา/รวบรวมข้อมูล (1.2)
Key points: แหล่งข้อมูลคือฐานของการออกแบบคำถามและการรวบรวมข้อมูล
Visual: Roadmap Module 1 (1.1 -> 1.2 -> 1.3)

### 1.2 การค้นหาและรวบรวมข้อมูล (2 ชั่วโมง)

**วัตถุประสงค์การเรียนรู้**
- แปลงปัญหานโยบายเป็นคำถามวิจัยที่ SMART
- วางแผนการค้นหาและรวบรวมข้อมูลเชิงกลยุทธ์
- ออกแบบการรวมข้อมูลจากหลายแหล่งและจัดทำ data dictionary

**โครงสร้างเนื้อหา**
- SMART Questions และการแตกคำถามหลักเป็นคำถามย่อย
- การกำหนดตัวแปรสำคัญตามกรอบ input-process-output-outcome-impact
- การกำหนดระดับการวิเคราะห์และช่วงเวลา
- การรวมข้อมูลหลายแหล่งและการแก้ปัญหานิยามต่างกัน
- การสร้าง data dictionary และบันทึกข้อจำกัด

**สาระสำคัญเชิงปฏิบัติ**
- ขั้นตอนแปลงปัญหา: ปัญหานโยบาย -> คำถามหลัก -> คำถามย่อย -> ตัวแปร
- การเลือกช่วงเวลา: ควรมี baseline และช่วงเวลาหลัง intervention ที่ชัดเจน
- การรวมข้อมูลควรเริ่มจากการสร้าง master key และตรวจสอบความสอดคล้อง
- ควรหลีกเลี่ยง many-to-many merge โดยไม่ทำ aggregation หรือใช้ตารางกลาง
- data dictionary ต้องระบุ field, type, source, calculation และข้อจำกัด

**ตัวอย่างที่ใช้สอน**
- ตัวอย่างคำถามเรื่องอัตราตายมารดาและตัวแปรที่ต้องใช้
- ตัวอย่างปัญหานิยามเบาหวานที่ต่างกันระหว่าง MOPH และ NHSO
- ตัวอย่าง mapping รหัสจังหวัด 2 หลัก vs 3 หลัก

**กิจกรรมย่อยแนะนำ**
- ให้ผู้เรียนเขียน SMART questions จากโจทย์นโยบายจริง
- ให้ผู้เรียนออกแบบแผนการค้นหาและขอข้อมูลตามแหล่งจริง

**สื่อแนะนำ**
- ใช้ `M1-Handout-Data-Collection.md` เป็นโครงหลัก
- ใช้ `M1-Workshop-Data-Search.md` สำหรับ workshop การทำ data source mapping

---

### 1.2 Slide Deck (20-26 slides) สำหรับหัวข้อ “การค้นหาและรวบรวมข้อมูล”

Slide 1 — Title
Goal: เปิดหัวข้อการค้นหาและรวบรวมข้อมูลเชิงกลยุทธ์
Key points: การเริ่มจากคำถาม -> แผนค้นหา -> แผนเข้าถึง -> แผนรวมข้อมูล
Visual: Roadmap 4 ขั้นตอน

Slide 2 — Learning Objectives
Goal: ระบุผลลัพธ์การเรียนรู้ใน 1 ชั่วโมง
Key points: เขียน SMART questions, วางแผนค้นหา/เข้าถึง, ออกแบบการรวมข้อมูลและ data dictionary
Visual: กล่อง 3 เป้าหมาย

Slide 3 — Workflow ภาพรวม
Goal: เห็นกระบวนการทั้งระบบก่อนลงรายละเอียด
Key points: Define question -> Inventory -> Access -> Integrate -> Document
Visual: Process flow 5 กล่อง

Slide 4 — SMART Questions คืออะไร
Goal: อธิบายหลัก SMART สำหรับคำถาม/วัตถุประสงค์
Key points: Specific, Measurable, Achievable, Realistic, Time-bound
Visual: วงล้อ SMART
Source: `https://www.cdc.gov/healthy-schools-training/php/training-topic/phase-1-assessment.html`

Slide 5 — ตัวอย่าง SMART Question (Policy Problem -> SMART)
Goal: ทำให้เห็นการแปลงปัญหาเป็นคำถามที่ใช้วิเคราะห์ได้
Key points: ระบุ “ใคร-ที่ไหน-เมื่อไร-ตัวชี้วัด” ให้ครบ
Visual: ก่อน-หลัง (Bad vs SMART)

Slide 6 — แตกคำถามหลักเป็นคำถามย่อย
Goal: แสดงโครงสร้าง Main question -> Sub-questions -> Variables
Key points: คำถามย่อยต้อง map ไปที่ตัวแปรได้จริง
Visual: Question tree

Slide 7 — Mapping ตัวแปรตามกรอบ IPO/OI
Goal: จัดหมวดตัวแปรให้ครบทั้ง input-process-output-outcome-impact
Key points: ใช้ช่วยกันหลุดตัวแปรสำคัญ
Visual: ตาราง 5 หมวด

Slide 8 — ระดับการวิเคราะห์ (Granularity)
Goal: ชี้การเลือกระดับข้อมูลให้สอดคล้องกับคำถาม
Key points: บุคคล/หน่วยบริการ/อำเภอ/จังหวัด/ประเทศ
Visual: Pyramid แสดงระดับข้อมูล

Slide 9 — Search Strategy: เริ่มจาก Data Catalog
Goal: แนะนำแหล่งค้นหาชุดข้อมูลภาครัฐก่อน
Key points: Data.go.th และ GD Catalog เป็นจุดเริ่มต้นหลัก
Visual: ช่อง search + ไอคอน catalog
Source: `https://www.dga.or.th/en/our-services/digital-platform-services/open-government-data/`
Source: `https://gdcatalog.go.th/en/about`

Slide 10 — Data.go.th: Open Data Portal
Goal: เข้าใจบทบาทศูนย์กลางข้อมูลเปิดของรัฐ
Key points: ใช้ค้นหา/ดาวน์โหลดชุดข้อมูลเปิด; มี metadata เบื้องต้น
Visual: Screenshot portal
Source: `https://www.dga.or.th/en/our-services/digital-platform-services/open-government-data/`

Slide 11 — GD Catalog: Government Data Catalog
Goal: ใช้ catalog เพื่อค้นหา “ข้อมูลที่ไม่เปิด” และ metadata เชิงลึก
Key points: ช่วยระบุเจ้าของข้อมูลและช่องทางเข้าถึง
Visual: Diagram “หน่วยงาน -> catalog -> ผู้ใช้”
Source: `https://gdcatalog.go.th/en/about`

Slide 12 — ช่องทางเข้าถึงข้อมูล (Access Pathways)
Goal: แยกประเภทการเข้าถึงข้อมูล
Key points: Open data / Request / Restricted + ข้อจำกัด
Visual: 3 กล่อง (Open/Request/Restricted)

Slide 13 — การขอข้อมูลตาม พ.ร.บ.ข้อมูลข่าวสาร
Goal: ให้ผู้เรียนเข้าใจสิทธิการเข้าถึงข้อมูลภาครัฐ
Key points: หลัก “เปิดเผยเป็นหลัก ปกปิดเป็นข้อยกเว้น”
Visual: Flow คำร้อง -> หน่วยงาน -> ผลการพิจารณา
Source: `https://oic.go.th/web2017/en/law_1.htm`

Slide 14 — Data Access Checklist
Goal: ทำให้การเข้าถึงข้อมูลเป็นระบบ
Key points: ผู้ถือครองข้อมูล, เงื่อนไขใช้ข้อมูล, timeline, ค่าใช้จ่าย, ช่องทางติดต่อ
Visual: Checklist

Slide 15 — Data Management Plan (DMP) แนวทางสากล
Goal: วางแผนการจัดการข้อมูลตั้งแต่ต้นทาง
Key points: อธิบายประเภทข้อมูล, การเก็บรักษา, การแบ่งปัน, metadata
Visual: DMP canvas 6 ช่อง
Source: `https://www.niehs.nih.gov/research/scientific-data/plan`

Slide 16 — Metadata และ Data Dictionary
Goal: ทำให้ข้อมูลตีความได้ซ้ำในอนาคต
Key points: ต้องมี metadata + data dictionary + เครื่องมือเก็บข้อมูล
Visual: ตัวอย่าง data dictionary
Source: `https://www.niehs.nih.gov/research/scientific-data/plan`
Source: `https://www.cdc.gov/epiinfo/user-guide/visual-dashboard/datadictionary.html`

Slide 17 — มาตรฐานและการทำ Harmonization
Goal: ลดปัญหานิยามไม่ตรงกันก่อน merge
Key points: ใช้มาตรฐานตัวแปร/หน่วยวัด/รหัสพื้นที่
Visual: ตาราง before/after standardization
Source: `https://www.niehs.nih.gov/research/scientific-data/plan`

Slide 18 — Data Integration คืออะไร
Goal: เข้าใจการรวมข้อมูลหลายแหล่งเชิงสถิติ
Key points: Integration = linking + merging + governance
Visual: Diagram 3 ขั้น
Source: `https://statisticaldataintegration.abs.gov.au/about-3/what-is-statistical-data-integration`

Slide 19 — Linking Methods: Deterministic vs Probabilistic
Goal: อธิบายหลักการเชื่อมข้อมูลด้วยตัวระบุ
Key points: Deterministic ใช้ unique ID; Probabilistic ใช้หลายตัวแปรระบุร่วมกัน
Visual: Two-column comparison
Source: `https://www.statcan.gc.ca/en/sdle/overview`

Slide 20 — Separation of Identifiers
Goal: แสดงการแยกข้อมูลระบุตัวตนออกจากข้อมูลวิเคราะห์
Key points: เก็บ identifiers แยกจาก analysis variables แล้วใช้ key เชื่อม
Visual: Diagram “Index file / Data file / Key registry”
Source: `https://www.statcan.gc.ca/en/sdle/overview`

Slide 21 — Privacy & Purpose Limitation
Goal: เน้นหลักจริยธรรมและความเป็นส่วนตัวในการเก็บข้อมูล
Key points: เก็บเท่าที่จำเป็น, ระบุวัตถุประสงค์ชัดเจน, ป้องกันการใช้ผิดวัตถุประสงค์
Visual: 3 หลักการ
Source: `https://www.oecd.org/en/publications/oecd-guidelines-on-the-protection-of-privacy-and-transborder-flows-of-personal-data_9789264196391-en.html`

Slide 22 — สรุปและเชื่อมไปหัวข้อ 1.3
Goal: ปิดบทเรียนและส่งต่อไปการตรวจสอบคุณภาพข้อมูล
Key points: เมื่อมีข้อมูลแล้ว ต้องเข้าสู่ขั้นตอนตรวจสอบความน่าเชื่อถือ
Visual: Roadmap 1.1 -> 1.2 -> 1.3

### 1.3 การตรวจสอบความน่าเชื่อถือของข้อมูล (3 ชั่วโมง)

**วัตถุประสงค์การเรียนรู้**
- ประเมินคุณภาพข้อมูลสุขภาพด้วยกรอบ TRUST
- ใช้เทคนิค cross-validation เพื่อลดความเสี่ยงจากข้อมูลผิดพลาด
- ตรวจสอบและจัดการปัญหาคุณภาพข้อมูลที่พบบ่อย

**โครงสร้างเนื้อหา**
- กรอบ TRUST และการตีความในบริบทข้อมูลไทย
- เทคนิค cross-validation แบบ triangulation, internal checks, benchmarking
- การตรวจสอบ missing data, outliers, logical consistency และ range checks
- การสรุปผลในรูปแบบ Data Quality Report

**สาระสำคัญเชิงปฏิบัติ**
- Timeliness ต้องระบุปีข้อมูลและความล่าช้าอย่างชัดเจน
- Representativeness ให้ตรวจ coverage และ bias ที่เกิดจากวิธีเก็บข้อมูล
- Uniformity ต้องตรวจนิยามที่เปลี่ยนตามเวลา และผลกระทบต่อ trend
- Source ต้องพิจารณาระดับความน่าเชื่อถือของหน่วยงาน
- Transparency ต้องมี metadata, data dictionary และข้อจำกัดที่อธิบายได้

**เทคนิคตรวจคุณภาพที่ต้องสอน**
- Missing data: MCAR, MAR, MNAR และแนวทางจัดการ
- Outliers: IQR, Z-score และการทำ sensitivity analysis
- Logical checks: อายุครรภ์, วันที่ตาย, ค่า lab ที่เป็นไปไม่ได้
- Cross-validation: เทียบกับ WHO หรือแหล่งรองที่เชื่อถือได้

**สื่อแนะนำ**
- ใช้ `M1-Handout-Data-Verification.md` เป็นแกนหลัก
- ใช้แบบฝึก `M1-Workshop-Data-Integration.md` เพื่อฝึกตรวจคุณภาพหลัง merge

---

### 1.3 Slide Deck (20-26 slides) สำหรับหัวข้อ "การตรวจสอบความน่าเชื่อถือของข้อมูล"

Slide 1 — Title
Goal: เปิดหัวข้อการตรวจสอบความน่าเชื่อถือของข้อมูลสุขภาพ
Key points: Data quality เป็นฐานของการตัดสินใจเชิงนโยบาย
Visual: ไอคอนแว่นขยาย + ฐานข้อมูล

Slide 2 — Learning Objectives
Goal: ระบุผลลัพธ์การเรียนรู้ใน 1 ชั่วโมง
Key points: เข้าใจมิติคุณภาพข้อมูล, ใช้กรอบ DQR/Trust, ออกแบบการตรวจสอบและรายงานผล
Visual: กล่อง 3 เป้าหมาย

Slide 3 — ทำไม Data Quality สำคัญ
Goal: เชื่อมคุณภาพข้อมูลกับความถูกต้องของข้อเสนอเชิงนโยบาย
Key points: หากข้อมูลผิดหรือไม่ครบ จะทำให้ข้อสรุปคลาดเคลื่อน
Visual: before/after ของการตัดสินใจ

Slide 4 — DQR Framework (WHO) ภาพรวม
Goal: เห็นกรอบมาตรฐานการประเมินคุณภาพข้อมูล
Key points: 4 มิติหลัก: completeness & timeliness, internal consistency, external consistency, population data
Visual: 4-box framework
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 5 — Dimension 1: Completeness & Timeliness
Goal: เข้าใจการตรวจความครบถ้วนและความทันเวลา
Key points: วัดการส่งรายงานครบ/ทันเวลา ทั้งระดับหน่วยบริการและระดับพื้นที่
Visual: calendar + checklist
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 6 — Completeness ที่ต้องตรวจ (Reporting vs Data Element)
Goal: แยกความครบถ้วนของรายงานกับความครบถ้วนของตัวแปร
Key points: รายงานครบแต่ตัวแปรขาดก็ยังไม่ผ่านคุณภาพ
Visual: ตารางเปรียบเทียบ 2 แบบ
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 7 — Timeliness: นิยามและตัวอย่างตัวชี้วัด
Goal: ทำให้เห็นการกำหนดเส้นตายและการประเมินทันเวลา
Key points: วัด % รายงานที่ส่งก่อน deadline ตามรอบรายเดือน/รายไตรมาส
Visual: timeline + cutoff
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 8 — Dimension 2: Internal Consistency
Goal: ตรวจความสอดคล้องภายในของข้อมูล
Key points: ตรวจแนวโน้มผิดปกติ, outliers, ความสัมพันธ์ของตัวแปรที่ควรสัมพันธ์กัน
Visual: line chart + outlier highlight
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 9 — Dimension 3: External Consistency
Goal: เทียบกับแหล่งข้อมูลอื่นเพื่อยืนยันความสมเหตุสมผล
Key points: เปรียบเทียบกับ survey หรือแหล่งข้อมูลภายนอกที่เชื่อถือได้
Visual: two datasets comparison
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 10 — Dimension 4: Population Data (Denominator Check)
Goal: ตรวจความเหมาะสมของตัวหารในการคำนวณอัตรา
Key points: ตรวจความสอดคล้องของข้อมูลประชากรที่ใช้เป็นตัวหาร
Visual: numerator/denominator graphic
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 11 — CAT: Completeness, Accuracy, Timeliness (CDC)
Goal: อธิบายชุดคุณลักษณะข้อมูลหลักในงาน surveillance
Key points: completeness, accuracy, timeliness เป็นแกนหลักของ data quality
Visual: CAT acronym
Source: `https://archive.cdc.gov/www_cdc_gov/ncbddd/birthdefects/surveillancemanual/chapters/chapter-7/chapter7.5.html`

Slide 12 — Accuracy/Validity ในเชิงปฏิบัติ
Goal: ทำให้เห็นตัวอย่างข้อมูลที่ถูกต้อง vs ผิด
Key points: ความถูกต้องขึ้นกับนิยามเคสและการเข้ารหัสที่ถูกต้อง
Visual: ตัวอย่าง record ถูก/ผิด
Source: `https://archive.cdc.gov/www_cdc_gov/ncbddd/birthdefects/surveillancemanual/chapters/chapter-7/chapter7.5.html`

Slide 13 — Representativeness และมิติคุณภาพอื่น
Goal: ชี้ว่าข้อมูลต้องสะท้อนประชากรเป้าหมายจริง
Key points: คุณภาพข้อมูลควรประเมินความเป็นตัวแทนและความเหมาะสมต่อวัตถุประสงค์
Visual: sample vs population
Source: `https://www.cdc.gov/mmwr/volumes/73/su/su7303a1.htm`

Slide 14 — Desk Review vs Data Verification (WHO DQA)
Goal: แยกงานตรวจเอกสารและการตรวจแหล่งต้นทาง
Key points: Desk review ตรวจชุดข้อมูลรายงาน; data verification ตรวจเอกสารต้นทาง
Visual: 2-layer audit diagram
Source: `https://www.who.int/data/data-collection-tools/health-service-data/data-quality-assurance-dqa/module-2-desk-review`

Slide 15 — Data Verification ที่ระดับหน่วยบริการ
Goal: เน้นขั้นตอนการตรวจเอกสารจริงในระดับบริการ
Key points: ตรวจ completeness ของเอกสารและรายงาน, ใช้ tracer indicators
Visual: checklist + tracer indicators
Source: `https://platform.who.int/docs/default-source/mca-documents/qoc/quality-of-care/country-level-holistic-data-quality-assurance.pdf`

Slide 16 — Desk Review: โครงสร้างการประเมิน
Goal: เห็นองค์ประกอบหลักของ desk review
Key points: completeness/timeliness, internal consistency, external comparison, population data
Visual: 4-step desk review
Source: `https://www.who.int/data/data-collection-tools/health-service-data/data-quality-assurance-dqa/module-2-desk-review`

Slide 17 — Missing Data: MCAR, MAR, MNAR
Goal: เข้าใจสมมติฐานหลักของ missing data
Key points: MCAR/MAR/MNAR ส่งผลต่อการตีความและการแก้ไขข้อมูลที่หาย
Visual: 3-column comparison
Source: `https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2776905`

Slide 18 — ตรวจ Outliers และความผิดตรรกะ
Goal: สาธิตการตรวจค่าที่ผิดปกติและไม่สมเหตุสมผล
Key points: ใช้ range check, logic check, trend check เป็นมาตรฐาน
Visual: boxplot + rule list
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 19 — Cross-Validation กับแหล่งอื่น
Goal: ยืนยันผลด้วยการเทียบหลายแหล่งข้อมูล
Key points: เปรียบเทียบกับ survey/benchmark เพื่อหาความต่างที่ต้องอธิบาย
Visual: bar chart comparison
Source: `https://iris.who.int/bitstream/handle/10665/259224/9789241512725-eng.pdf`

Slide 20 — Data Quality Improvement Plan
Goal: เปลี่ยนผลการประเมินเป็นแผนปรับปรุงคุณภาพข้อมูล
Key points: ใช้ผล DQR เพื่อกำหนดกิจกรรมปรับปรุงก่อนเริ่มแผนงาน
Visual: action plan timeline
Source: `https://platform.who.int/docs/default-source/mca-documents/qoc/quality-of-care/country-level-holistic-data-quality-assurance.pdf`

Slide 21 — Data Quality Dashboard/Report (CDC)
Goal: แสดงเครื่องมือรายงานผลคุณภาพข้อมูลเชิงปฏิบัติ
Key points: รายงานคุณภาพข้อมูลมักติดตาม completeness, timeliness, validity
Visual: dashboard mockup
Source: `https://www.cdc.gov/nssp/php/onboarding-toolkits/data-quality.html`

Slide 22 — สรุปและเชื่อมไปการใช้งานจริง
Goal: ปิดบทเรียนและเชื่อมไปกิจกรรมตรวจคุณภาพข้อมูล
Key points: ใช้กรอบ DQR + Trust แล้วสรุปผลเป็นรายงานคุณภาพข้อมูล
Visual: checklist + report icon

## ไฟล์ที่ควรมีในโฟลเดอร์นี้

### Slides
- `M1-01-Data-Sources.pptx` ใช้เปิดภาพรวมและจัดกลุ่มแหล่งข้อมูล
- `M1-02-Data-Collection.pptx` ใช้สรุป SMART questions และขั้นตอนการรวมข้อมูล
- `M1-03-Data-Verification.pptx` ใช้ทบทวน TRUST และ quality checks

### Handouts
- `M1-Handout-Data-Sources.md` ใช้เป็นเอกสารหลักสำหรับโมดูล 1.1
- `M1-Handout-Data-Collection.md` ใช้เป็นเอกสารหลักสำหรับโมดูล 1.2
- `M1-Handout-Data-Verification.md` ใช้เป็นเอกสารหลักสำหรับโมดูล 1.3
- `M1-Data-Dictionary-Template.md` ใช้เป็นแม่แบบบันทึกตัวแปรและนิยาม

### Worksheets / Workshops
- `M1-Workshop-Data-Search.md` ใช้ฝึกทำ data source mapping แบบเป็นขั้นตอน
- `M1-Workshop-Data-Integration.md` ใช้ฝึก merge และตรวจคุณภาพหลังรวมข้อมูล

### Case Studies
- `M1-Case-Thai-Health-Data.md` ใช้เป็นกรณีศึกษาเพื่ออภิปรายความเหลื่อมล้ำ

### Data Files
- `sample_moph_data.csv`, `sample_nhso_data.csv`, `sample_nso_data.csv` ใช้เป็นชุดฝึก

---

## กิจกรรมหลัก

### Workshop 1: Data Source Mapping
**เป้าหมาย**
- ให้ผู้เรียนเลือกปัญหาสุขภาพและระบุแหล่งข้อมูลที่จำเป็น
- ฝึกคิดเชิงระบบและประเมินความเป็นไปได้ของข้อมูล

**แนวทางดำเนินกิจกรรม**
- เลือกประเด็น 1 เรื่องจากรายการ
- เขียน problem statement และคำถามย่อย
- เติมตาราง data source mapping และสรุปแผนการขอข้อมูล

**ผลลัพธ์ที่คาดหวัง**
- ตารางแหล่งข้อมูลครบถ้วนตามคำถามย่อย
- แผนการเข้าถึงข้อมูลพร้อมข้อจำกัดและทางแก้

### Workshop 2: Data Integration
**เป้าหมาย**
- ฝึก merge ข้อมูลหลายชุดและแก้ปัญหาความสอดคล้อง
- สร้าง data dictionary และทำ quality checks หลังรวมข้อมูล

**แนวทางดำเนินกิจกรรม**
- ตรวจพบปัญหาในแต่ละ dataset
- สร้าง master key และรวมข้อมูล
- สรุป completeness และความสอดคล้องเชิงตรรกะ

**ผลลัพธ์ที่คาดหวัง**
- ตาราง merged dataset ที่ถูกต้อง
- data dictionary และบันทึกข้อจำกัด

### Exercise: Data Quality Check
**เป้าหมาย**
- ฝึกใช้ TRUST และตรวจคุณภาพข้อมูลแบบเป็นระบบ

**แนวทางดำเนินกิจกรรม**
- ระบุ missing data, outliers และค่าผิดตรรกะ
- สรุปการแก้ไขและข้อจำกัดในรูปแบบ report

**ผลลัพธ์ที่คาดหวัง**
- Data Quality Report แบบย่อ
- ข้อเสนอแนะสำหรับการใช้ข้อมูลอย่างปลอดภัย

---

## ลิงก์สำคัญ
- MOPH Health Data: https://spd.moph.go.th/health-data/
- NHSO Dashboard: https://www.nhso.go.th/
- NSO Statistics: https://www.nso.go.th/
- ThaiHealthStat: https://www.hiso.or.th/thaihealthstat/
- Government Data Catalog: https://gdcatalog.go.th/

---

## หมายเหตุสำหรับผู้สอน
- ควรเน้นให้ผู้เรียนเห็นความแตกต่างของนิยามและการตีความตัวเลข
- ให้ผู้เรียนฝึกเขียนข้อจำกัดของข้อมูลในทุกกิจกรรมเพื่อฝัง mindset ด้านความน่าเชื่อถือ
- ใช้กรณีศึกษาเพื่อเชื่อมโยงข้อมูลกับการตัดสินใจเชิงนโยบาย