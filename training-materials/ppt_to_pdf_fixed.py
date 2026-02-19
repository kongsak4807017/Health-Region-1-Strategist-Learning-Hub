#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
แปลงไฟล์ PowerPoint (.ppt, .pptx) เป็น PDF (Lossless)
ใช้ PowerPoint COM Interface บน Windows
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Union, List

PP_FORMAT_PDF = 32


def ppt_to_pdf(input_path: str, output_path: str = None, show_window: bool = True) -> str:
    """แปลงไฟล์ PowerPoint (.ppt/.pptx) เป็น PDF"""
    import win32com.client
    
    input_path = Path(input_path).resolve()
    
    if not input_path.exists():
        raise FileNotFoundError(f"ไม่พบไฟล์: {input_path}")
    
    if input_path.suffix.lower() not in ['.ppt', '.pptx', '.pptm']:
        raise ValueError(f"ไฟล์ต้องเป็น .ppt, .pptx หรือ .pptm: {input_path.suffix}")
    
    if output_path is None:
        output_path = input_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path).resolve()
    
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    ppt_app = None
    presentation = None
    
    try:
        ppt_app = win32com.client.Dispatch("PowerPoint.Application")
        ppt_app.DisplayAlerts = False
        
        presentation = ppt_app.Presentations.Open(
            str(input_path),
            WithWindow=show_window,
            ReadOnly=True
        )
        
        presentation.SaveAs(
            str(output_path),
            FileFormat=PP_FORMAT_PDF
        )
        
        print(f"[OK] {input_path.name}")
        return str(output_path)
        
    except Exception as e:
        print(f"[FAIL] {input_path.name} - {str(e)}")
        raise
        
    finally:
        if presentation:
            presentation.Close()
        if ppt_app:
            ppt_app.Quit()


def batch_convert(folder_path: str, recursive: bool = False, show_window: bool = True) -> List[str]:
    """แปลงไฟล์ PowerPoint ทั้งหมดในโฟลเดอร์"""
    folder = Path(folder_path).resolve()
    
    if not folder.exists():
        raise FileNotFoundError(f"ไม่พบโฟลเดอร์: {folder}")
    
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
        print(f"[{i}/{len(ppt_files)}] ", end="", flush=True)
        try:
            pdf_path = ppt_to_pdf(ppt_file, show_window=show_window)
            results.append(pdf_path)
        except Exception as e:
            continue
    
    print("-" * 50)
    print(f"แปลงสำเร็จ {len(results)}/{len(ppt_files)} ไฟล์")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="แปลงไฟล์ PowerPoint (.ppt/.pptx) เป็น PDF",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('input', nargs='?', help='ไฟล์ PowerPoint ที่ต้องการแปลง')
    parser.add_argument('output', nargs='?', help='ไฟล์ PDF ที่ต้องการ (optional)')
    parser.add_argument('--folder', '-f', help='แปลงไฟล์ทั้งหมดในโฟลเดอร์')
    parser.add_argument('--recursive', '-r', action='store_true', help='ค้นหาในโฟลเดอร์ย่อยด้วย')
    parser.add_argument('--show-window', '-w', action='store_true', help='แสดงหน้าต่าง PowerPoint')
    
    args = parser.parse_args()
    
    if not args.input and not args.folder:
        parser.print_help()
        sys.exit(1)
    
    try:
        if args.folder:
            batch_convert(args.folder, args.recursive, args.show_window)
        else:
            ppt_to_pdf(args.input, args.output, args.show_window)
            
    except FileNotFoundError as e:
        print(f"ข้อผิดพลาด: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ข้อผิดพลาด: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
