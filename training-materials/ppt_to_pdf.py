#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
แปลงไฟล์ PowerPoint (.ppt, .pptx) เป็น PDF (Lossless)
ใช้ PowerPoint COM Interface บน Windows (ให้คุณภาพสูงสุด)

Requirements:
    pip install pywin32

Usage:
    python ppt_to_pdf.py <input.ppt> [output.pdf]
    python ppt_to_pdf.py --folder <folder_path>  # แปลงทุกไฟล์ในโฟลเดอร์
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Union, List

# PowerPoint constants
PP_FORMAT_PDF = 32  # ppSaveAsPDF


def ppt_to_pdf(input_path: str, output_path: str = None, show_window: bool = False) -> str:
    """
    แปลงไฟล์ PowerPoint (.ppt/.pptx) เป็น PDF
    
    Args:
        input_path: พาธของไฟล์ .ppt หรือ .pptx
        output_path: พาธของไฟล์ PDF ที่ต้องการ (optional)
        show_window: แสดงหน้าต่าง PowerPoint ขณะแปลง (default: False)
    
    Returns:
        พาธของไฟล์ PDF ที่สร้างขึ้น
    """
    import win32com.client
    from win32com.client import constants
    
    input_path = Path(input_path).resolve()
    
    if not input_path.exists():
        raise FileNotFoundError(f"ไม่พบไฟล์: {input_path}")
    
    # ตรวจสอบนามสกุลไฟล์
    if input_path.suffix.lower() not in ['.ppt', '.pptx', '.pptm']:
        raise ValueError(f"ไฟล์ต้องเป็น .ppt, .pptx หรือ .pptm เท่านั้น: {input_path.suffix}")
    
    # กำหนด output path
    if output_path is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path).resolve()
    
    # สร้างโฟลเดอร์ถ้ายังไม่มี
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    ppt_app = None
    presentation = None
    
    try:
        # สร้าง instance ของ PowerPoint
        ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        ppt_app.Visible = show_window
        ppt_app.DisplayAlerts = False  # ปิด alert เพื่อความเร็ว
        
        # เปิด presentation
        presentation = ppt_app.Presentations.Open(
            str(input_path),
            WithWindow=show_window,
            ReadOnly=True
        )
        
        # Export เป็น PDF (คุณภาพสูงสุด)
        presentation.SaveAs(
            str(output_path),
            FileFormat=PP_FORMAT_PDF  # ppSaveAsPDF
        )
        
        print(f"✓ แปลงสำเร็จ: {input_path.name} → {output_path.name}")
        return str(output_path)
        
    except Exception as e:
        print(f"✗ แปลงไม่สำเร็จ: {input_path.name} - {str(e)}")
        raise
        
    finally:
        # Cleanup
        if presentation:
            presentation.Close()
        if ppt_app:
            ppt_app.Quit()


def batch_convert(folder_path: str, recursive: bool = False, show_window: bool = False) -> List[str]:
    """
    แปลงไฟล์ PowerPoint ทั้งหมดในโฟลเดอร์
    
    Args:
        folder_path: พาธของโฟลเดอร์
        recursive: ค้นหาไฟล์ในโฟลเดอร์ย่อยด้วย (default: False)
        show_window: แสดงหน้าต่าง PowerPoint (default: False)
    
    Returns:
        รายการพาธของไฟล์ PDF ที่สร้างขึ้น
    """
    folder = Path(folder_path).resolve()
    
    if not folder.exists():
        raise FileNotFoundError(f"ไม่พบโฟลเดอร์: {folder}")
    
    # หาไฟล์ .ppt และ .pptx
    pattern = "**/*" if recursive else "*"
    ppt_files = [
        f for f in folder.glob(pattern) 
        if f.suffix.lower() in ['.ppt', '.pptx', '.pptm']
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
            pdf_path = ppt_to_pdf(ppt_file, show_window=show_window)
            results.append(pdf_path)
        except Exception as e:
            print(f"ข้อผิดพลาด: {e}")
            continue
    
    print("-" * 50)
    print(f"แปลงสำเร็จ {len(results)}/{len(ppt_files)} ไฟล์")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="แปลงไฟล์ PowerPoint (.ppt/.pptx) เป็น PDF (Lossless)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python ppt_to_pdf.py presentation.ppt
  python ppt_to_pdf.py presentation.ppt output.pdf
  python ppt_to_pdf.py --folder ./presentations
  python ppt_to_pdf.py --folder ./presentations --recursive
        """
    )
    
    parser.add_argument('input', nargs='?', help='ไฟล์ PowerPoint ที่ต้องการแปลง')
    parser.add_argument('output', nargs='?', help='ไฟล์ PDF ที่ต้องการ (optional)')
    parser.add_argument('--folder', '-f', help='แปลงไฟล์ทั้งหมดในโฟลเดอร์')
    parser.add_argument('--recursive', '-r', action='store_true', help='ค้นหาในโฟลเดอร์ย่อยด้วย')
    parser.add_argument('--show-window', '-w', action='store_true', help='แสดงหน้าต่าง PowerPoint')
    
    args = parser.parse_args()
    
    # ตรวจสอบ arguments
    if not args.input and not args.folder:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.folder:
            # Batch convert
            batch_convert(args.folder, args.recursive, args.show_window)
        else:
            # Single file
            ppt_to_pdf(args.input, args.output, args.show_window)
            
    except FileNotFoundError as e:
        print(f"ข้อผิดพลาด: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ข้อผิดพลาด: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
