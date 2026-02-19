---
name: thai-health-strategist
description: Health strategy and policy analysis for Thailand's public health system. Use when working with Thai health data sources, analyzing health policy problems, conducting root cause analysis for public health issues, verifying health data reliability, or developing evidence-based policy recommendations for Thailand's healthcare system.
---

# Thai Health Strategist

Guide for health strategy analysis focusing on Thailand's public health system, data integration from multiple sources, and evidence-based policy recommendation development.

## Core Workflows

### 1. Data Discovery & Collection

Identify and access relevant Thai health data sources based on analytical needs:

| Data Need | Primary Sources | Data Types |
|-----------|----------------|------------|
| Population health status | MOPH Health Statistics, NSO, ThaiHealthStat | Mortality, morbidity, risk factors |
| Healthcare utilization | NHSO, MOPH Service Statistics | Claims, visits, procedures |
| Health resources | MOPH, HA | Facilities, workforce, equipment |
| Financial flows | NHSO, IHPP, NHA | Expenditures, budgets, UCS claims |
| Behavioral risk factors | NSO Health Behavior Survey, DDC | Smoking, drinking, exercise |
| Disease surveillance | DDC, BOD Thailand | Infectious diseases, NCDs |

**Key Data Sources:**
- **MOPH Health Statistics**: https://spd.moph.go.th/health-data/ - สถิติสาธารณสุขประจำปี
- **ThaiHealthStat**: https://www.hiso.or.th/thaihealthstat/ - สถิติสุขภาพเชิงประเด็น
- **NHSO Dashboard**: เข้าถึงข้อมูลสิทธิบัตรทอง (UCS) claims
- **NSO Health Data**: https://www.nso.go.th/nsoweb/nso/statistics_and_indicators - สำรวจพฤติกรรมสุขภาพ
- **Government Data Catalog**: https://gdcatalog.go.th - ชุดข้อมูลเปิดภาครัฐ
- **BOD Thailand**: https://bodthai.net - ภาระโรคประเทศไทย

### 2. Data Verification & Validation

Before analysis, verify data reliability using the TRUST framework:

**T - Timeliness**: ข้อมูลเป็นปัจจุบันหรือไม่? ปีใด?
**R - Representativeness**: ตัวอย่างมีความหลากหลายและครอบคลุมประชากรเป้าหมายหรือไม่?
**U - Uniformity**: วิธีการเก็บข้อมูลและนิยามเป็นมาตรฐานเดียวกันหรือไม่?
**S - Source**: แหล่งที่มาเป็นองค์กรที่น่าเชื่อถือหรือไม่?
**T - Transparency**: มีเอกสารอธิบายวิธีการเก็บและประมวลผลหรือไม่?

**Cross-Validation Methods:**
1. Compare multiple sources for same indicator (e.g., compare MOPH vs NHSO mortality data)
2. Check time-series consistency - มีการเปลี่ยนแปลงผิดปกติหรือไม่?
3. Verify against international benchmarks (WHO, World Bank)
4. Consult subject matter experts for face validity

### 3. Root Cause Analysis (RCA)

For public health problems, apply systematic RCA:

**Step 1: Problem Definition**
- ระบุปัญหาอย่างชัดเจน (SMART definition)
- กำหนดขอบเขตการวิเคราะห์

**Step 2: Data Collection**
- รวบรวมข้อมูลเชิงปริมาณ (magnitude, trends, distribution)
- รวบรวมข้อมูลเชิงคุณภาพ (stakeholder perspectives, case studies)

**Step 3: Causal Analysis**
Apply appropriate frameworks:

*5 Whys Technique:*
```
ปัญหา: อัตราตายมารดาสูงในจังหวัด X
ทำไม? → การตั้งครรภ์ไม่พร้อม
ทำไม? → การเข้าถึงการคุมกำเนิดไม่เพียงพอ
ทำไม? → ขาดบุคลากรด้านอนามัยการเจริญพันธุ์
ทำไม? → การกระจายบุคลากรไม่สอดคล้องกับความต้องการ
ทำไม? → ระบบวางแผนกำลังคนไม่มีข้อมูลพื้นที่เสี่ยง
```

*Fishbone Diagram (4Ps/4Ms):*
- People: ปัจจัยด้านประชากร/ผู้รับบริการ
- Process: กระบวนการบริการ/ระบบส่งต่อ
- Policy: นโยบายและการจัดสรรทรัพยากร
- Place: บริบททางภูมิศาสตร์และสังคม

*Social Determinants Framework:*
- ปัจจัยโครงสร้าง: นโยบาย เศรษฐกิจ สังคม
- ปัจจัยระดับชุมชน: สภาพแวดล้อม การเข้าถึงบริการ
- ปัจจัยระดับบุคคล: พฤติกรรม ความรู้ ทักษะ

**Step 4: Priority Setting**
ใช้ Impact-Effort Matrix หรือ Pareto Analysis เลือกสาเหตุหลักที่จะแก้ไข

### 4. Policy Analysis Framework

Apply structured policy analysis using the following frameworks:

**Policy Triangle Framework:**
```
        Content
       /       \
  Context ---- Process
```

**Walt & Gilson Framework:**
- **Content**: นโยบายว่าด้วยเรื่องใด เป้าหมายคืออะไร
- **Context**: บริบทการเมือง เศรษฐกิจ สังคม
- **Process**: กระบวนการร่าง ผลักดัน ปฏิบัติ
- **Actors**: ใครมีส่วนได้ส่วนเสีย ใครมีอำนาจตัดสินใจ

**Health in All Policies (HiAP):**
พิจารณาผลกระทบทางสุขภาพจากนโยบายภาคส่วนอื่น (การศึกษา ที่อยู่อาศัย สิ่งแวดล้อม)

### 5. Evidence-Based Recommendation Development

**Policy Recommendation Structure:**

1. **Problem Statement**: อธิบายปัญหา พร้อมหลักฐานข้อมูล
2. **Root Causes**: สาเหตุเชิงลึกที่พบจากการวิเคราะห์
3. **Policy Options**: ทางเลือกนโยบายที่เป็นไปได้ พร้อม SWOT แต่ละทางเลือก
4. **Recommended Option**: ทางเลือกที่แนะนำ พร้อมเหตุผลเชิงหลักฐาน
5. **Implementation Considerations**: ปัจจัยสำคัญสำหรับการนำไปปฏิบัติ
6. **Monitoring Indicators**: ตัวชี้วัดติดตามผล

**Quality Check for Recommendations:**
- Feasibility: เป็นไปได้ในบริบทไทยหรือไม่
- Evidence-based: มีหลักฐานจากงานวิจัย/การปฏิบัติที่ผ่านมาหรือไม่
- Stakeholder-aligned: สอดคล้องกับความต้องการของผู้มีส่วนได้ส่วนเสีย
- Resource-conscious: พิจารณาทรัพยากรที่มีอยู่

## Data Integration Best Practices

**When merging data from multiple sources:**
1. ตรวจสอบปีข้อมูลให้ตรงกันหรือใกล้เคียง
2. ตรวจสอบนิยามตัวแปร (เช่น การนับผู้ป่วย NCD อาจต่างกันระหว่างแหล่งข้อมูล)
3. ใช้รหัสพื้นที่มาตรฐาน (รหัสจังหวัด, รหัสอำเภอ)
4. สร้าง data dictionary บันทึกแหล่งที่มาและนิยาม
5. Document limitations and assumptions

## Common Health Data Challenges in Thailand

| Challenge | Mitigation Strategy |
|-----------|---------------------|
| Under-reporting in rural areas | Triangulate with multiple sources |
| Definition changes over time | Document version changes; analyze trends with caution |
| Delayed data availability | Use proxy indicators; clearly state data vintage |
| Inconsistent geographic boundaries | Use standard codes; map to current boundaries |
| Missing data | Apply appropriate imputation; document methodology |

## References

- [Thai Health Data Sources](references/thai-health-data-sources.md) - Comprehensive directory of Thai health databases
- [Policy Analysis Methods](references/policy-analysis-methods.md) - Detailed frameworks and methodologies
- [Root Cause Analysis Guide](references/root-cause-analysis.md) - RCA techniques for public health
- [Policy Recommendation Template](references/policy-recommendation-template.md) - Standardized format for recommendations
