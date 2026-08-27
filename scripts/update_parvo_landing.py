import os

landing_path = r'c:\Users\master\parvogel_landing\src\pages\Landing.jsx'

with open(landing_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. import ParvogelClinicalDocumentary 추가
if 'ParvogelClinicalDocumentary' not in content:
    target_import = "import ClinicalEvidence from '../components/ClinicalEvidence'"
    new_import = "import ClinicalEvidence from '../components/ClinicalEvidence'\nimport ParvogelClinicalDocumentary from '../components/ParvogelClinicalDocumentary'"
    content = content.replace(target_import, new_import)

# 2. JSX 내에 <ParvogelClinicalDocumentary /> 추가
if '<ParvogelClinicalDocumentary />' not in content:
    target_jsx = "<ClinicalEvidence />"
    new_jsx = "<ClinicalEvidence />\n\n            {/* 리얼 6단계 임상 다큐멘터리 (일자별 치료 순서 동기화) */}\n            <ParvogelClinicalDocumentary />"
    content = content.replace(target_jsx, new_jsx)

# 3. 네비게이션 메뉴에 임상 다큐 앵커 추가
if '#parvogel-clinical-doc' not in content and 'clinical' in content:
    # 기존 네비게이션 메뉴 항목 찾기
    pass

with open(landing_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Landing.jsx updated with ParvogelClinicalDocumentary successfully!')
