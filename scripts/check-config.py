from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
assert '.env' in (root / '.gitignore').read_text().splitlines(), 'Local .env must be ignored'
violations = []
for name in ['docker-compose.yml', 'Config/dei/application.properties', 'Config/kibana/kibana.yml', 'Config/logstash/logstash.yml', 'Config/logstash/pipeline/logstash.conf', 'JavaBuild/Dockerfile']:
    for number, line in enumerate((root / name).read_text().splitlines(), 1):
        if line.strip().startswith('#'):
            continue
        if re.search(r'password|secret[._]?key|TOKEN_GITHUB', line, re.I) and '${' not in line:
            violations.append(f'{name}:{number}')
assert not violations, 'Literal credential assignments: ' + ', '.join(violations)
print('Configuration credential checks passed')
