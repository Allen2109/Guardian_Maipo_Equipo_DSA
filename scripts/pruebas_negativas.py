"""Confirma que los escáneres detecten tres fallas inyectadas SIN ejecutarlas.

Útil después de instalar Gitleaks, Semgrep y Trivy. Guarda informes sin secretos
ni payloads reveladores en la consola. El resultado del guion debe ser VERDE
cuando los controles rechazan satisfactoriamente los fallos temporales.
"""
import json
import subprocess
import tempfile
from pathlib import Path
from generar_caso_ejercicio import crear


def ejecutar(cmd, *, codigo_esperado=1):
    proceso = subprocess.run(cmd, text=True, capture_output=True, check=False)
    if proceso.returncode != codigo_esperado:
        raise RuntimeError(f'El control {cmd[0]} no detectó el caso previsto: '
                           f'código {proceso.returncode}, esperado {codigo_esperado}; '
                           f'error reducido: {proceso.stderr[-350:]}')
    return proceso


def verificar():
    reports = Path('reports')
    reports.mkdir(exist_ok=True)
    base = Path.cwd()
    with tempfile.TemporaryDirectory(prefix='maipo-casos-') as directorio:
        lab = Path(directorio)
        caso_secreto = lab/'secreto'
        crear(caso_secreto, 'fallo')
        ejecutar(['gitleaks','dir','--redact','--config',str(base/'.gitleaks.toml'),
                  '--report-format','json','--report-path',str(base/'reports/fallo-secreto.json'),
                  str(caso_secreto)])
        caso_codigo = lab/'codigo'
        caso_codigo.mkdir()
        # Fragmento de texto SOLO para análisis estático, NO es importado ni ejecutado.
        (caso_codigo/'codigo_de_ejemplo.py').write_text(
            'import subprocess\nimport requests\n'
            'def simulacion(entrada):\n'
            '    comando = "lector-demo " + entrada\n'
            '    subprocess.run(comando, shell=True)\n'
            '    requests.post("https://ejemplo.invalid", data="ficticio", verify=False)\n',
            encoding='utf-8')
        ejecutar(['semgrep','scan','--metrics','off','--no-git-ignore','--error',
                  '--config',str(base/'.semgrep.yml'),'--json',
                  '--output',str(base/'reports/fallo-codigo.json'),str(caso_codigo)])
        resultados = json.loads((reports/'fallo-codigo.json').read_text(encoding='utf-8'))
        ids = {r['check_id'].split('.')[-1] for r in resultados.get('results',[])}
        if not {'maipo-python-shell','maipo-tls'}.issubset(ids):
            raise RuntimeError('Las reglas de Semgrep no localizaron ambos problemas')
        caso_red = lab/'red'
        caso_red.mkdir()
        (caso_red/'panel.yaml').write_text(
            'sistema: panel-operacional-laboratorio\n'
            'origenes_permitidos: [0.0.0.0/0]\n', encoding='utf-8')
        ejecutar(['trivy','config','--misconfig-scanners','yaml','--config-check',str(base/'policies'),
                  '--check-namespaces','builtin,user','--severity','HIGH,CRITICAL',
                  '--exit-code','1','--format','json','--output',
                  str(base/'reports/fallo-red.json'),str(caso_red)])
        hallazgos = json.loads((reports/'fallo-red.json').read_text(encoding='utf-8'))
        fallos = [m for r in hallazgos.get('Results',[]) for m in r.get('Misconfigurations',[])
                  if m.get('Status') == 'FAIL']
        if not any(m.get('ID') == 'MAIPO-NET-001' for m in fallos):
            raise RuntimeError('Trivy no notificó la regla de red MAIPO-NET-001')
    (reports/'resultados_negativos.json').write_text(json.dumps({
        'gitleaks':'FALLA_DETECTADA', 'semgrep_shell':'FALLA_DETECTADA',
        'semgrep_tls':'FALLA_DETECTADA','trivy_red':'FALLA_DETECTADA',
        'codigo_peligroso_ejecutado':False}, indent=2),encoding='utf-8')
    print('OK: Gitleaks, Semgrep y Trivy detectaron defectos sembrados sin ejecutarlos')


if __name__ == '__main__':
    verificar()
