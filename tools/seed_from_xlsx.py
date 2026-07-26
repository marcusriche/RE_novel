#!/usr/bin/env python3
"""Extract a Unified_Seed_Row JSON from the Unified Seed Matrix workbook.

Stdlib-only (zipfile + ElementTree) so it runs in restricted environments.
Columns whose authored value is itself strict JSON (per §16.0, R21) are parsed
into structures; integer-typed columns are coerced. The sheet header is the
source of field names; column letters are output, never authority (§16.0).

Usage:
  python tools/seed_from_xlsx.py <matrix.xlsx> [row_index] > seed_row.json
"""
import json
import re
import sys
import xml.etree.ElementTree as ET
import zipfile

NS = '{http://schemas.openxmlformats.org/spreadsheetml/2006/main}'

# Fields whose cell text is strict JSON (arrays/objects) in the sheet.
JSON_FIELDS = {
    "Mandatory_Set_Pieces_with_Phase", "Central_Tropes", "Trope_Payoff_Schedule",
    "Antagonistic_Force", "Allies_Confidants", "Dominant_Pair", "Initial_CER_Seed",
    "Initial_Relationship_State", "Operational_Clock", "Continuity_Constraints",
    "Sentence_Rhythm_Targets", "Signature_Moves", "Taboo_List_and_Sensitive_Notes",
    "Brand_Lexicon", "Redundancy_Rules", "Platform_Hook_Profile", "Comparable_Titles",
    "Promo_Platform_Compatibility", "Locale_Signature", "Cover_Dimensions",
    "Content_Warnings_Public", "QA_Flags", "Sensitivity_Flags",
}
INT_FIELDS = {
    "Heat_Level", "First_Kiss_Phase", "First_Intimacy_Phase", "Age_A", "Age_B",
    "Dialogue_Ratio", "Comedy", "Darkness", "Suspense", "Cussing", "Violence",
    "Interiority_Ratio", "Lyricality", "Book_Number", "Pre_Order_Duration",
    "Word_Count_Target", "Word_Count_Actual", "Editor_Pass_Count",
}
BOOL_FIELDS = {"Epilogue_Included"}


def read_rows(path):
    z = zipfile.ZipFile(path)
    shared = []
    try:
        root = ET.fromstring(z.read('xl/sharedStrings.xml'))
        for si in root.findall(f'{NS}si'):
            shared.append(''.join(t.text or '' for t in si.iter(f'{NS}t')))
    except KeyError:
        pass
    root = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
    rows = []
    for row in root.iter(f'{NS}row'):
        vals = {}
        for c in row:
            ref, t = c.get('r'), c.get('t')
            v = c.find(f'{NS}v')
            txt = v.text if v is not None else ''
            if t == 's':
                txt = shared[int(txt)]
            col = re.match(r'[A-Z]+', ref).group(0)
            vals[col] = txt
        rows.append(vals)
    return rows


def main():
    path = sys.argv[1]
    row_index = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    rows = read_rows(path)
    header = rows[0]
    raw = rows[row_index]
    seed = {}
    for col, key in header.items():
        val = raw.get(col, '')
        if key in JSON_FIELDS and val:
            seed[key] = json.loads(val)
        elif key in INT_FIELDS and val:
            seed[key] = int(float(val))
        elif key in BOOL_FIELDS and val:
            seed[key] = val.strip().upper() in ("TRUE", "1")
        else:
            seed[key] = val
    json.dump(seed, sys.stdout, indent=2, ensure_ascii=False)
    sys.stdout.write('\n')


if __name__ == '__main__':
    main()
