#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
แปลงไฟล์ PowerPoint (.ppt, .pptx) เป็น PDF โดยใช้ LibreOffice
เหมาะสำหรับกรณีที่ไม่มี Microsoft PowerPoint หรือต้องการ cross-platform

Requirements:
    - ติดตั้ง LibreOffice: https://www.libreoffice.org/download/
    - LibreOffice ต้องอยู่ใน PATH

Usage:
    python ppt_to_pdf_libreoffice.py <input.ppt> [output_folder]
    python ppt_to_pdf_libreoffice.py --folder <folder_path>
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path
from typing import List


def check_libreoffice() -> bool:
    """ตรวจสอบว่ามี LibreOffice ในระบบหรือไม่"""
    try:
        if os.name == 'nt':  # Windows
            result = subprocess.run(
                ['where', 'soffice'],
                capture_output=True,
                text=True
            )
        else:  # Linux/Mac
            result = subprocess.run(
                ['which', 'soffice'],
                capture_output=True,
                text=True
            )
        return result.returncode == 0
    except Exception:
        return False


def ppt_to_pdf_libreoffice(input_path: str, output_folder: str = None) -> str:
    """
    แปลงไฟล์ PowerPoint เป็น PDF โดยใช้ LibreOffice
    
    Args:
        input_path: พาธของไฟล์ .ppt หรือ .pptx
        output_folder: โฟลเดอร์สำหรับบันทึก PDF (default: เดียวกับไฟล์ต้นฉบับ)
    
    Returns:
        พาธของไฟล์ PDF ที่สร้างขึ้น
    """
    input_path = Path(input_path).resolve()
    
    if not input_path.exists():
        raise FileNotFoundError(f"ไม่พบไฟล์: {input_path}")
    
    if input_path.suffix.lower() not in ['.ppt', '.pptx', '.pptm', '.odp']:
        raise ValueError(f"ไฟล์ต้องเป็น .ppt, .pptx, .pptm หรือ .odp: {input_path.suffix}")
    
    # กำหนด output folder
    if output_folder is None:
        output_folder = input_path.parent
    else:
        output_folder = Path(output_folder).resolve()
        output_folder.mkdir(parents=True, exist_ok=True)
    
    # สร้างคำสั่ง LibreOffice
    cmd = [
        'soffice',
        '--headless',           # ไม่แสดง GUI
        '--convert-to', 'pdf',  # แปลงเป็น PDF
        '--outdir', str(output_folder),  # โฟลเดอร์ output
        str(input_path)         # ไฟล์ input
    ]
    
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=120  # timeout 2 นาที
        )
        
        if result.returncode != 0:
            raise RuntimeError(f"LibreOffice error: {result.stderr}")
        
        # หาไฟล์ PDF ที่สร้างขึ้น
        output_pdf = output_folder / f"{input_path.stem}.pdf"
        
        if output_pdf.exists():
            print(f"✓ แปลงสำเร็จ: {input_path.name} → {output_pdf.name}")
            return str(output_pdf)
        else:
            raise FileNotFoundError(f"ไฟล์ PDF ไม่ถูกสร้าง: {output_pdf}")
            
    except subprocess.TimeoutExpired:
        raise TimeoutError("การแปลงใช้เวลานานเกินไป (timeout)")
    except Exception as e:
        print(f"✗ แปลงไม่สำเร็จ: {input_path.name} - {str(e)}")
        raise


def batch_convert_libreoffice(folder_path: str, recursive: bool = False) -> List[str]:
    """
    แปลงไฟล์ PowerPoint ทั้งหมดในโฟลเดอร์โดยใช้ LibreOffice
    """
    folder = Path(folder_path).resolve()
    
    if not folder.exists():
        raise FileNotFoundError(f"ไม่พบโฟลเดอร์: {folder}")
    
    # หาไฟล์
    pattern = "**/*" if recursive else "*"
    ppt_files = [
        f for f in folder.glob(pattern)
        if f.suffix.lower() in ['.ppt', '.pptx', '.pptm', '.odp']
    ]
    
    if not ppt_files:
        print(f"ไม่พบไฟล์ PowerPoint ใน: {folder}")
        return []
    
    print(f"พบไฟล์ PowerPoint จำนวน {len(ppt_files)} ไฟล์")
    print("-" * 50)
    
    results = []
    for i, ppt_file in enumerate(ppt_files, 1):
        print(f"[{i}/{len(ppt_files)}] ", end="")
        try:
            pdf_path = ppt_to_pdf_libreoffice(ppt_file)
            results.append(pdf_path)
        except Exception as e:
            print(f"ข้อผิดพลาด: {e}")
            continue
    
    print("-" * 50)
    print(f"แปลงสำเร็จ {len(results)}/{len(ppt_files)} ไฟล์")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="แปลงไฟล์ PowerPoint เป็น PDF โดยใช้ LibreOffice",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Requirements:
    - ติดตั้ง LibreOffice: https://www.libreoffice.org/download/

Examples:
  python ppt_to_pdf_libreoffice.py presentation.ppt
  python ppt_to_pdf_libreoffice.py presentation.ppt ./output
  python ppt_to_pdf_libreoffice.py --folder ./presentations --recursive
        """
    )
    
    parser.add_argument('input', nargs='?', help='ไฟล์ PowerPoint ที่ต้องการแปลง')
    parser.add_argument('output', nargs='?', help='โฟลเดอร์สำหรับบันทึก PDF (optional)')
    parser.add_argument('--folder', '-f', help='แปลงไฟล์ทั้งหมดในโฟลเดอร์')
    parser.add_argument('--recursive', '-r', action='store_true', help='ค้นหาในโฟลเดอร์ย่อยด้วย')
    
    args = parser.parse_args()
    
    # ตรวจสอบ LibreOffice
    if not check_libreoffice():
        print("ข้อผิดพลาด: ไม่พบ LibreOffice ในระบบ")
        print("กรุณาติดตั้ง LibreOffice: https://www.libreoffice.org/download/")
        print("และเพิ่มไปยัง PATH (Windows: C:\\Program Files\\LibreOffice\\program)")
        sys.exit(1)
    
    if not args.input and not args.folder:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.folder:
            batch_convert_libreoffice(args.folder, args.recursive)
        else:
            ppt_to_pdf_libreoffice(args.input, args.output)
    except Exception as e:
        print(f"ข้อผิดพลาด: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
